## About Linux Networking
### DNS

> Domain names are simply readable names.
 for practicality purposes.

 Pseudocode showing the DNS Process:

 ```
ip, err = getIPAddress(domainName)
if err:
  print(“unknown Host Exception while trying to resolve:%s”.format(domainName))
 ```

 Within that, "getIPAddress" function, we have something along the lines of:

 ```
 def getIPAddress(domainName):
    resp, fail = lookupCache(domainName)
    If not fail:
       return resp
    else:
       resp, err = gethostbyname(domainName)
       if err:
         return null, err
       else:
          return resp
 ```

 Basically:

 * Lookup the Cache, if it doesn't fail, return a response.
 * Else, gethostbyname() and if that fails, return error.

 This is all happening on operating systems, so the linux equivalent, the OS has a line:

 ```
hosts: files dns
 ```

 This means that the OS has to look up the first in /etc/hosts and then use DNS protocol to do a resoltuion if there is no match in /etc/hosts

 The /etc/hosts is of the format (with the last two lines added by us):

 ```
127.0.0.1	localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.17.0.4	5bbb45ed5b82
127.0.0.1 localhost.localdomain localhost
::1 localhost.localdomain localhost
 ```

 If a match exists for a domain in this file, then that IP address is returned by the OS, adding a line:

```
 127.0.0.1 test.linkedin.com
```

 and then ping (after installing, yum install ip-utils):

```
[root@5bbb45ed5b82 temp]# ping test.linkedin.com -n
PING test.linkedin.com (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.052 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.025 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.026 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.017 ms
64 bytes from 127.0.0.1: icmp_seq=5 ttl=64 time=0.041 ms
64 bytes from 127.0.0.1: icmp_seq=6 ttl=64 time=0.044 ms
64 bytes from 127.0.0.1: icmp_seq=7 ttl=64 time=0.057 ms
^C
--- test.linkedin.com ping statistics ---
7 packets transmitted, 7 received, 0% packet loss, time 6150ms
rtt min/avg/max/mdev = 0.017/0.037/0.057/0.015 ms
```

 If no match exists in /etc/hosts, then OS tries to do a DNS resolution using the DNS protocol. The linux system makes a DNS request to the first IP in /etc/resolv.conf.  If there is no response, requests are set to a subsequent servers in resolv.conf.

 Looking at this on our VM:

 ```
[root@5bbb45ed5b82 temp]# cat /etc/resolv.conf
# DNS requests are forwarded to the host. DHCP DNS options are ignored.
nameserver 192.168.65.5
 ```
* These servers in resolv.conf are called DNS resolvers.

 * DNS resolvers are populated by DHCP, Dynamic Host Configuration Protocol, which is used to automatically assign IP addresses and other parameters to devices using the client-server architecture.

* [Dig](https://linux.die.net/man/1/dig) is a DNS lookup utility. This is a tool for interrogating DNS nameservers.

 Runing a command on shell to capture all DNS requests (after installing with yum install tcpdump):

* Note - at this point I was unable to install tcpdump on Red Hat Linux, so I switched to a Debian VM, and went back and did the above commands.

```
#run this command in one shell to capture all DNS requests
tcpdump -s 0 -A -i any port 53

root@a93522e30f3d:/# tcpdump -s 0 -A -i any port 533
tcpdump: data link type LINUX_SLL2
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes



#make a dig request from another shell
dig linkedin.com

root@a93522e30f3d:/# dig linkedin.com

; <<>> DiG 9.16.22-Debian <<>> linkedin.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 8722
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;linkedin.com.			IN	A

;; ANSWER SECTION:
linkedin.com.		73	IN	A	13.107.42.14

;; Query time: 5 msec
;; SERVER: 192.168.65.5#53(192.168.65.5)
;; WHEN: Tue Nov 09 19:57:54 UTC 2021
;; MSG SIZE  rcvd: 46
```

Doing a trace...

```
root@a93522e30f3d:/# dig +trace linkedin.com

; <<>> DiG 9.16.22-Debian <<>> +trace linkedin.com
;; global options: +cmd
;; Received 17 bytes from 192.168.65.5#53(192.168.65.5) in 2 ms
```

#### Applications in SRE Role

1. Companies have to have DNS infrastructure / intranet sites and databases and other internal applications. Ther ehas to be a DNS infrastructure maintained for those domain names by the infrastructure team. This DNS infrastructure has to be optimized and scaled so it doesn't become a single point of failure.
2. DNS can be used to discover services, for example the hostame servicb.internal.example.com could list instances which run service b internally in example.com company.
3. DNS is used by cloud providers / CDN providers to scale their services. Load balancers are given a CNAME instead of IPAddress. They update IPAdress of the loadbalancers. This is one of the reasons why A records of such alias domains that are short lived like 1 minute.
4. DNS can be used to make clients get IP addresses closer to their location so that their HTTP calls can be responded faster if the company has a presence geographically distributed.
5. SRE also has to understand since there is no verification / DNS infrastructure, responses can be spoofed. This is a safeguarded by other protocols like HTTPS, DNSSEC protects from forged or manipulated DNS responses.
6. Stale DNS cache can be a problem. Some apps might still be using expired DNS records for their API calls.
7. DNS Loadbalancing and service discovery has to undestand TTL and the servers can be removed from the pool only after waiting till TTL post the changes are made to DNS records. If this is not done, a certain portion of the traffic will fail as the server is removed before the TTL.

### UDP

* DNS is an application that runs on top of UDP
* UDP is the transport layer.
* Multiple processes can run on a system and they can listen on any ports.

#### Sample UDP Note Post in Python3

https://wiki.python.org/moin/UdpCommunication

```sending
   1 import socket
   2 
   3 UDP_IP = "127.0.0.1"
   4 UDP_PORT = 5005
   5 MESSAGE = b"Hello, World!"
   6 
   7 print("UDP target IP: %s" % UDP_IP)
   8 print("UDP target port: %s" % UDP_PORT)
   9 print("message: %s" % MESSAGE)
  10 
  11 sock = socket.socket(socket.AF_INET, # Internet
  12                      socket.SOCK_DGRAM) # UDP
  13 sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
```
```receiving
   1 import socket
   2 
   3 UDP_IP = "127.0.0.1"
   4 UDP_PORT = 5005
   5 
   6 sock = socket.socket(socket.AF_INET, # Internet
   7                      socket.SOCK_DGRAM) # UDP
   8 sock.bind((UDP_IP, UDP_PORT))
   9 
  10 while True:
  11     data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
  12     print("received message: %s" % data)
```

### HTTP

* The HTML page of Linkedin.com is served by an HTTP protocol which the browser renders.
* HTTP requests have a, "verb" - GET, PUT, POST, followed by a path and query parameters and lines of key value pair which gives information about the client and capabilities.

You can always use, "curl -v" to see the entire HTTP request:

```
[root@5bbb45ed5b82 temp]# curl linkedin.com -v
* Rebuilt URL to: linkedin.com/
*   Trying 13.107.42.14...
* TCP_NODELAY set
* Connected to linkedin.com (13.107.42.14) port 80 (#0)
> GET / HTTP/1.1
> Host: linkedin.com
> User-Agent: curl/7.61.1
> Accept: */*
> 
< HTTP/1.1 301 Moved Permanently
< Location: https://www.linkedin.com/
< X-Li-Fabric: prod-lor1
< X-Li-Pop: afd-prod-lor1-x
< X-Li-Proto: http/1.1
< X-LI-UUID: AAXQYcaNG1NuBTMauoQBJQ==
< X-Cache: CONFIG_NOCACHE
< X-MSEdge-Ref: Ref A: 8D257CCD314C42FCA7BBA09AC3239A10 Ref B: MSP30EDGE0318 Ref C: 2021-11-09T21:27:25Z
< Date: Tue, 09 Nov 2021 21:27:24 GMT
< Content-Length: 0
< 
* Connection #0 to host linkedin.com left intact
```

* GET/ HTTP/1.1 shows the VERB and the path is 1.1 (the protocol version)
* Server responds back with the HTTP version, Status Code and Message.

Status codes can always be looked up, but 2xx is success, 3xx is redirect, 4xx client error while 5xx is server error.

If you do HTTP 1.0 you get something different:

```
root@a93522e30f3d:/# telnet www.linkedin.com 80
Trying 13.107.42.14...
Connected to l-0005.l-msedge.net.
Escape character is '^]'.
```
* One of the benefits of HTTP/2.0 over HTTP/1.1 is we can have multiple inflight requests on the same connection. We are restricting our scope to generic HTTP and not jumping to the intricacies of each protocol version but they should be straight forward to understand post the course.

* Overview of HTTPS vs HTTP - certificate of trust, etc.

### TCP

* TCP is a transport layer protocol like UDP but guarantees reliability, flow control and congestion control.
* TCP guarantees reliable delivery by using sequence numbers.
* A TCP connection is established by a three-way handshake. "Are you there? -> Yes! -> OK great!"

### Routing and Data Link Layer

Start out by installing net-tools to be able to do routing.

```
apt-get install net-tools

[root@5bbb45ed5b82 temp]# route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         172.17.0.1      0.0.0.0         UG    0      0        0 eth0
172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 eth0

```

* The Destination is bitwise AND'ed with the Genmask.
* If the result is destination part of the table then that gateway and interface is picked for routing.

For example:

* (108.174.10.10)AND(255.255.255.0) = 108.173.10.0
* This doesn't match any destination in the routing table.

(the rest of the explination here is not very good and gets confusing)

Notes:

Generally the routing table is populated by DHCP and playing around is not a good practice. There can be reasons where one has to play around the routing table but take that path only when it's absolutely necessary
Understanding error messages better like, “No route to host” error can mean mac address of the destination host is not found and it can mean the destination host is down
On rare cases looking at the ARP table can help us understand if there is a IP conflict where same IP is assigned to two hosts by mistake and this is causing unexpected behavior