# Python

## Compiled vs. Interpreted

* Python is a compiled language with a built-in compiler.
* Java gets compiled manually, so it's obvious. Python it's less obvious.  Java's compiler is more strict and sophisticated.  Java is statically typed, so the compiler is written in a way that it can verify types related errors during compile time. Basically, like with c++, if you do, "int a" - this variable a can only ever take on one value.
* Python is a dynamic language, meaning that, "a" variable can be changed. So, types are not known until the program is run.

Python has something called, "bytecode" which is on a program by program basis, which shows how things are loaded, even a helloworld program, line by line.

C programs compile down to machine code, as opposed to a bite code.

In the case of C/C++, the output is machine code, which can be directly read by an operating system, but bytecodes are language-specific. Python and Java have their own specific bytecodes, so there is something called a Virtual Machine (either a JVM in the case of Java or Cython/Jython in the case of Python).  Virtual Machines read the bytecode and run it on a given operating system. Python has multiple VM's available. Cpython is implemented in C, whereas Jython is a Java implementation.

### Decorators

I've gone through this before, this is a standard way of decorating a function on either side, before, after or both, it's a good way to standardize functions optionally, to quickly and easily call things that should happen, for example on a route call.

### Python, Web and Flask

* HTTP is a protocol that works over TCP. You can setup a TCP server and send an HTTP request and inspect the payload:

```
$ python
Python 3.9.5 (default, Sep 21 2021, 16:47:38) 
[Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import socket
>>> 
>>> HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
>>> PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
>>> 
>>> with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
...    s.bind((HOST, PORT))
...    s.listen()
...    conn, addr = s.accept()
...    with conn:
...        print('Connected by', addr)
...        while True:
...            data = conn.recv(1024)
...            if not data:
...                break
...            print(data)
... 
Connected by ('127.0.0.1', 63084)
b'GET / HTTP/1.1\r\nHost: localhost:65432\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nsec-ch-ua: "Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: "macOS"\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCookie: JSESSIONID=node0gb0gv5obfuj41u9gudk09me831.node0\r\n\r\n'
```
#### Flask

I have worked with this a significant amount in the past.

### The URL Shortening App

```
from flask import Flask, redirect, request

from hashlib import md5

app = Flask("url_shortener")

mapping = {}

@app.route("/shorten", methods=["POST"])
def shorten():
    global mapping
    payload = request.json

    if "url" not in payload:
        return "Missing URL Parameter", 400

    # TODO: check if URL is valid

    hash_ = md5()
    hash_.update(payload["url"].encode())
    digest = hash_.hexdigest()[:5]  # limiting to 5 chars. Less the limit more the chances of collission

    if digest not in mapping:
        mapping[digest] = payload["url"]
        return f"Shortened: r/{digest}\n"
    else:
        # TODO: check for hash collission
        return f"Already exists: r/{digest}\n"


@app.route("/r/<hash_>")
def redirect_(hash_):
    if hash_ not in mapping:
        return "URL Not Found", 404
    return redirect(mapping[hash_])


if __name__ == "__main__":
    app.run(debug=True)

"""
OUTPUT:


===> SHORTENING

$ curl localhost:5000/shorten -H "content-type: application/json" --data '{"url":"https://linkedin.com"}'
Shortened: r/a62a4


===> REDIRECTING, notice the response code 302 and the location header

$ curl localhost:5000/r/a62a4 -v
* Uses proxy env variable NO_PROXY == '127.0.0.1'
*   Trying ::1...
* TCP_NODELAY set
* Connection failed
* connect to ::1 port 5000 failed: Connection refused
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET /r/a62a4 HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.64.1
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 302 FOUND
< Content-Type: text/html; charset=utf-8
< Content-Length: 247
< Location: https://linkedin.com
< Server: Werkzeug/0.15.4 Python/3.7.7
< Date: Tue, 27 Oct 2020 09:37:12 GMT
<
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
* Closing connection 0
<p>You should be redirected automatically to target URL: <a href="https://linkedin.com">https://linkedin.com</a>.  If not click the link.
"""
```