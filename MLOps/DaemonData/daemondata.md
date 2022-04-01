# Create a Daemon


* On MacOS
* Download RPi Image
* https://www.raspberrypi.com/software/operating-systems/
* Unzip .img file
* Create .gitignore file and include .img
* Turn into .tar.gz file with:

```
tar -cvzf raspios-bullseye.tar.gz 2022-01-28-raspios-bullseye-armhf-lite.img
```
This takes a long time, so it would be better to have a progress bar:

```
tar cf - 2022-01-28-raspios-bullseye-armhf-lite.img -P | pv -s $(($(du -sk 2022-01-28-raspios-bullseye-armhf-lite.img | awk '{print $1}') * 1024)) | gzip > raspios-bullseye.tar.gz
```
Had to install, "pv" but it worked, showing:

```
$ tar cf - 2022-01-28-raspios-bullseye-armhf-lite.img -P | pv -s $(($(du -sk 2022-01-28-raspios-bullseye-armhf-lite.img | awk '{print $1}') * 1024)) | gzip > raspios-bullseye.tar.gz
 867MiB 0:00:25 [14.5MiB/s] [=============================>                                      ] 45% ETA 0:00:30
```
During the running of the command.

* Create a from scratch Docker image:

```
FROM scratch
ADD raspios-bullseye.tar.gz /
```

* Built image:

```
docker build -t raspios-bullseye-image .
```
* Ran Container:

```
docker run --name raspios-bullseye-container -it raspios-bullseye-image /bin/bash
```

Didn't work, used established RPi image from https://hub.docker.com/r/balenalib/raspberry-pi-debian/tags instead on Dockerfile, then ran:

```
docker run --name raspios-bullseye-container -it raspios-buster-image bin/bash
```

Used for managing fleets of IoT images. https://www.balena.io/what-is-balena/

Installing Go on RPi

```
apt-get update
```

Documentation:

https://www.balena.io/docs/reference/base-images/base-images/#balena-base-images?ref=dockerhub

```
FROM balenalib/raspberry-pi-debian:buster-20220224
```


# Restarting Project with DockerPi

https://github.com/lukechilds/dockerpi

Fully virtualized Raspberry Pi on Docker


```
docker run -it lukechilds/dockerpi

...
Extracting fresh filesystem...
Archive:  /filesystem.zip
  inflating: 2019-09-26-raspbian-buster-lite.img
image: /sdcard/filesystem.img

```

We can then log in with the default username and password:

```
raspberrypi login: pi
Password:
Linux raspberrypi 4.19.50+ #1 Tue Nov 26 01:49:16 CET 2019 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
pi@raspberrypi:~$
```

We can explore the pi:

```
pi@raspberrypi:/$ ls
bin   dev  home  lost+found  mnt  proc  run   srv  tmp  var
boot  etc  lib   media       opt  root  sbin  sys  usr
```

Creating a Daemon:

Firt check if Python works:

```
pi@raspberrypi:~$ python3
Python 3.7.3 (default, Apr  3 2019, 05:39:12)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

Then do:

```
sudo apt-get update
sudo apt-get install nano
```

Allow root permissions to be able to access I/O

```
sudo -i
GPIONUM=12
echo $GPIONUM > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio12/direction
```

However we get:

```
root@raspberrypi:~# echo $GPIONUM > /sys/class/gpio/export
-bash: /sys/class/gpio/export: No such file or directory
```

Hypothetically we would do the following to set the output level:

```
echo "1" > /sys/class/gpio/gpio12/value
echo "0" > /sys/class/gpio/gpio12/value
```

If we were to set up the same as an input, we would do:

```
echo $GPIONUM > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio12/direction
```

Read its state:

```
cat /sys/class/gpio/gpio12/value
```

There is also actually a gpio command:

```
gpio -g mode $GPIONUM out

# turn ON
gpio -g write $GPIONUM 1

# turn OFF
gpio -g write $GPIONUM 0
```


Here is a very simple standalone example that toggles an output pin on and off for 200 milliseconds, ten times. It also reports the level on input pin 31. If you put the commands in a file and make it executable, you can directly run it as a program.


```
#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

led = 18
switch = 31

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)

for i in range(10):
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.2)
    print('Switch status = ', GPIO.input(switch))

GPIO.cleanup()

```

We get an error regarding the RPi.GPIO library.

Install the library:

```
sudo apt-get update
sudo apt-get install rpi.gpio
```

When we try to run samplecode.py, we get the following:

```
  File "samplecode.py", line 3, in <module>
    import RPi.GPIO as GPIO
  File "/usr/lib/python3/dist-packages/RPi/GPIO/__init__.py", line 23, in <module>
    from RPi._GPIO import *
RuntimeError: This module can only be run on a Raspberry Pi!
```

So at this point, there is a general pathway forward for being able to read inputs on a Raspberry Pi, however we're not able to actually read any of the GPIO pins since this is all 100% simulated.

# Simulating a Daemon

So basically what we want to do is:

* Read a GPIO input from an ADC showing the voltage level on a battery over time.
* Output that voltage level to a database of some kind.

What we could do for now is monitor something else, perhaps a random number generator, and log those numbers 


https://pypi.org/project/python-daemon/

https://raspberrypi.stackexchange.com/questions/5371/whats-the-right-way-to-run-a-python-script-as-a-daemon-service-in-raspbian-o


Power concsumption with RPi

https://blog.rustprooflabs.com/2019/04/postgresql-pgbench-raspberry-pi


### Researching What Already Exists for Battery Monitoring Daemons for RPI

* There is a tool that checks whether a GPIO pin is working:

https://elinux.org/R-Pi_Troubleshooting#Testing

* There is a Daemon that can monitor GPIO

http://abyz.me.uk/rpi/pigpio/pigpiod.html

it's already written in C++, so it's probably better to use that rather than write an entirely new daemon.

Here's more info on it:

https://abyz.me.uk/rpi/pigpio/piscope.html

### Utilizing Python-Daemon to Create a Daemon

* It doesn't make sense to write a Daemon, given that a Daemon already exists for this purpose.
* It's better to look at the documentation, which takes a large amount of time already, and install and use the Daemon in question.

### Installing PigPi Daemon on Raspberry Pi Simulator

https://abyz.me.uk/rpi/pigpio/download.html

Python setup tools may be needed.

```
sudo apt install python-setuptools python3-setuptools
```
Then, do the actual installation:

```
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install
```
We're going to need to understand where to install this stuff, and how to keep it organized within the Rpi.

Once this is all installed using the above commands, we should be ready to get a daemon going that monitors a particular GPIO continously as a daemon.

Of course, if we attempt to test the library, we get the following error:

```
 sudo ./x_pigpio
2022-03-24 18:25:42 gpioHardwareRevision: unknown revision=0
2022-03-24 18:25:42 initCheckPermitted:
+---------------------------------------------------------+
|Sorry, this system does not appear to be a raspberry pi. |
|aborting.                                                |
+---------------------------------------------------------+


pigpio initialisation failed.
```

We get the same problem if we attempt to start the daemon: ```sudo pigpiod```

That being said, we can review some of the documentation to see what the output of the daemon would be, and hypothetically come up with a plan for what the output should be.
Further, we can build a script that is designed to install all or the majority of the tools we may need.

### Reveiwing the PigPio Documentation

https://abyz.me.uk/rpi/pigpio/pigpiod.html

Once launched the pigpio library runs in the background accepting commands from the pipe and socket interfaces.

#### pigpiod

```
sudo pigpiod -s 2 -b 200 -f
```

* Launch pigpiod
* 2 microseconds sample rate
* 200 millisecond buffer
* -f will disable fifo interface

Other interesting options:

* -n IP_ADDRESS ... allows an IP address to access the socket interface, otherwise all IP addresses allowed
* -l ... only allows local (non-remote) connections to GPIO pins
* -t is used as a clock peripheral to select either PWM or PCM for outputs

#### Features of pigpio in General

* GPIO sampling up to 5 us, hardware timed
* hardware timed PWM
* hardware timed servo pulses
* notifications via pipe on GPIO 0-31 level change
* reading/writing all of the GPIO as a single operation
* socket and pipe interfaces with the bulk of functionality

##### Socket Interface

* The socket is available whenever pigpio is running, either whether it has been started as a daemon, or linked to a running user program.
* By default the socket interface is running in the daemon, unless the -k flag is activated to disable it
* pigpio listens for connections on port 8888 (presumably on localhost) by default, this may be overwridden with -p on the daemon or gpcioCfgSocketPort function call.

#### Python Code Example

Function to instantly check the status of all of the GPIO's using the pigpio library:
https://abyz.me.uk/rpi/pigpio/examples.html#Python%20code

```
#!/usr/bin/env python

import time
import curses
import atexit

import pigpio 

GPIOS=32

MODES=["INPUT", "OUTPUT", "ALT5", "ALT4", "ALT0", "ALT1", "ALT2", "ALT3"]

def cleanup():
   curses.nocbreak()
   curses.echo()
   curses.endwin()
   pi.stop()

pi = pigpio.pi()

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

atexit.register(cleanup)

cb = []

for g in range(GPIOS):
   cb.append(pi.callback(g, pigpio.EITHER_EDGE))

# disable gpio 28 as the PCM clock is swamping the system

cb[28].cancel()

stdscr.nodelay(1)

stdscr.addstr(0, 23, "Status of gpios 0-31", curses.A_REVERSE)

while True:

   for g in range(GPIOS):
      tally = cb[g].tally()
      mode = pi.get_mode(g)

      col = (g / 11) * 25
      row = (g % 11) + 2

      stdscr.addstr(row, col, "{:2}".format(g), curses.A_BOLD)

      stdscr.addstr(
         "={} {:>6}: {:<10}".format(pi.read(g), MODES[mode], tally))

   stdscr.refresh()

   time.sleep(0.1)

   c = stdscr.getch()

   if c != curses.ERR:
      break

```
Function to monitor the GPIO's for level changes:
https://abyz.me.uk/rpi/pigpio/examples.html#Python%20code

```

#!/usr/bin/env python

# monitor.py
# 2016-09-17
# Public Domain

# monitor.py          # monitor all GPIO
# monitor.py 23 24 25 # monitor GPIO 23, 24, and 25

import sys
import time
import pigpio

last = [None]*32
cb = []

def cbf(GPIO, level, tick):
   if last[GPIO] is not None:
      diff = pigpio.tickDiff(last[GPIO], tick)
      print("G={} l={} d={}".format(GPIO, level, diff))
   last[GPIO] = tick

pi = pigpio.pi()

if not pi.connected:
   exit()

if len(sys.argv) == 1:
   G = range(0, 32)
else:
   G = []
   for a in sys.argv[1:]:
      G.append(int(a))
   
for g in G:
   cb.append(pi.callback(g, pigpio.EITHER_EDGE, cbf))

try:
   while True:
      time.sleep(60)
except KeyboardInterrupt:
   print("\nTidying up")
   for c in cb:
      c.cancel()

pi.stop()
```

In general there are lots of different capabilities from the code examples, anything that can happen within a 5us timeframe can be extended from pigpio, and functionized,
then translated into a Python function (rather than building something from scratch). Basically this gives easy extensibility for python code.

So in essence, there should be a way to run a python program which uses this daemon to check for GPIO levels, on whatever basis is needed, by making calls to pigpio.

#### Shutting Down the Rpi from Python

Python can import, "call" which can then call a shell script.

The shell script which poweroff's the rpi is:

```
sudo shutdown --poweroff
```
Which is unambiguous and does the software poweroff stuff (e.g. non-hardware kill).

The python script would be:

```
from subprocess import call
call("sudo shutdown --poweroff", shell=True)
```

#### Looking into Python Daemon Stuff

So given that we can access the GPIO's via the pigpio library (and we may be able to access them direclty anyway), and that we can actually shut down the Pi within Python:

* We could also create a Python daemon which watches pigpio and shuts down the Pi given certain conditions.

##### Creating a Python Daemon

https://stackoverflow.com/questions/473620/how-do-you-create-a-daemon-in-python

https://pypi.org/project/python-daemon/

Note, when checking out Python, note that we have Python 2 installed, which we should be careful about:

```
root@raspberrypi:/home/bin# python --version
Python 2.7.16
root@raspberrypi:/home/bin# python3 --version
Python 3.7.3
```
We should install pip3 with:

```
sudo apt-get update
sudo apt-get install python3-pip
```
This didn't work, so we try, after updating:

```
sudo apt-get install python3-pip --fix-missing
```
This appeared to clear some of the 404 errors we had and though there were some libraries that appeared to fail to be fetched, overall it worked.

From here we can install python-daemon:

```
sudo pip3 install python-daemon
```
Which worked successfully.

Then, writing the Daemon:

https://stackoverflow.com/questions/4637420/efficient-python-daemon

```
#!/usr/bin/python

import daemon
import time

def do_something():
    while True:
        with open("/tmp/current_time.txt", "w") as f:
            f.write("The time is now " + time.ctime())
        time.sleep(5)

def run():
    with daemon.DaemonContext():
        do_something()

if __name__ == "__main__":
    run()
```


Once we wrote the Daemon, we have to find it's PID number:

https://www.linuxquestions.org/questions/linux-general-1/how-do-i-find-the-pid-of-a-daemon-742027/

```
ps aux
root     17984  6.1  2.7  14616  6900 ?        S    03:37   0:38 python3 pythons
root     17988  5.8  2.7  14616  6868 ?        S    03:37   0:34 python3 pythons
```
There were two python3 daemons we started, one right after another, with PID's 17984 and 17988.

To tail the logs:

```
tail -f /proc/17984/fd/1
```
Nothing coming out.

Then there's trusty old strace:

```
strace -e trace=open -p 17988
```
Neither of which produce anything.

So, we need to modify our python code to output something to the log possibly to ensure that it's working.

We could just run the python code as a regular python script, before even running it as a daemon, to help simplify things.

We can kill the processes that are not working with:

```
sudo kill -9 PID
```
Turning the Daemon into a while loop that just runs:

```
#!/usr/bin/python

import daemon
import time

def do_something():
    while True:
        print(("The time is now " + time.ctime()))
        time.sleep(5)

# def run():
#    with daemon.DaemonContext():
#        do_something()

if __name__ == "__main__":
    do_something()
```
After verifying that the above works and does indeed print out the time to the shell, we can go ahead and create a file within the directory that we're in, and write the time.

So we write to a file that we created in our directory, and the time shows up as expected.

So next we can turn this into a daemon by calling, "run()" rather than, "dosomething()"

After making this change and running, "pythonstuffd.py" we are sent back to the command line.

Checking the current time text file, it does not actually update. Perhaps this is because the daemon is running on the CPU or something rather than in the directory we're in.

This might be why we attempt to write to something in the /tmp folder.

When we tail, /tmp/whatever.log we should be able to see the output.

So when we do this, and then we wait a bit for the process to get going, our python code looks like:

```
#!/usr/bin/python

import daemon
import time

def do_something():
    while True:
        with open("/tmp/test.log", "w") as f:
            f.write("The time is now " + time.ctime())
            # print(("The time is now " + time.ctime()))
            time.sleep(5)

def run():
    with daemon.DaemonContext():
        do_something()

if __name__ == "__main__":
    run()
```
And the tail output of the log looks like:

```
root@raspberrypi:/home/bin# tail -f /tmp/test.log
The time is now Fri Mar 25 04:19:54 2022tail: /tmp/test.log: file truncated
The time is now Fri Mar 25 04:20:00 2022tail: /tmp/test.log: file truncated
The time is now Fri Mar 25 04:20:05 2022tail: /tmp/test.log: file truncated
The time is now Fri Mar 25 04:20:10 2022tail: /tmp/test.log: file truncated
The time is now Fri Mar 25 04:20:15 2022tail: /tmp/test.log: file truncated
The time is now Fri Mar 25 04:20:20 2022tail: /tmp/test.log: file truncated
The time is now Fri Mar 25 04:20:25 2022tail: /tmp/test.log: file truncated
The time is now Fri Mar 25 04:20:30 2022tail: /tmp/test.log: file truncated
```
So basically this successfully is checking the time and printing it out to that log tail.

How much of the CPU and memory, etc. does this take up?

```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root     18134 24.4  2.7  14616  6936 ?        S    04:19   0:34 python3 pythons
```
This shows close to a quarter of the CPU, which might or might not be accurate.

However, we could lengthen the amount of time in between samples and sleep to see if this brings the CPU usage down.

CPU usage did appear to go down to 12.2% after an initial startup period.

#### Attempting to Monitor GPIO Pins with Python Only

https://forums.raspberrypi.com/viewtopic.php?t=43069

There does appear to be a way to monitor a pin directly, but the downside is that it only checks the input at the moment it runs the loop, so basically for a fraction of a
second once every second. This might differ from using pigpio and the pigpio library / daemon underneath, and calling on that, which has a buffer.

Essentially, using a python Daemon with a loop in combination with pigpio might be a superior solution, however the CPU usage may go up. Also pigpio is hardware-timed, which may
mean there is more accuracy.

#### Pushing Data from Raspberry Pi to a Remote Database

It doesn't seem to make sense to keep all of the data on a RPi, and maintain a database, as there isn't a lot of operation that's needed on the RPi itself, we're not building
edge intelligence as much as cloud intelligence with data gathered from the edge.

The edge unit could have some simple instructions based upon what the cloud determines - e.g. we could feed in a preventative shutdown signal.

We could test out https://www.elephantsql.com/

##### Attempting a Curl to ElephantSQL with Whatever Data

https://www.elephantsql.com/docs/python.html

```
pip3 install psycopg2
Successfully installed psycopg2-2.9.3
```

Then using Elephant SQL:

```
import os
import urllib.parse as up
import psycopg2

up.uses_netloc.append("postgres")
url = up.urlparse(os.environ["DATABASE_URL"])
conn = psycopg2.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
)
```
* We will have to set up a new table at the onset of working with a database after connecting to the database.
* Once the table is setup, we can pass data and commit it.

https://www.psycopg.org/docs/usage.html

* Our RPi will have the ability to write to this database.
* However another client could have the ability to read and display data from this database.

We get 20MB, so how much data is per row?  We can figure out how many posts we can get, calculating:

```
(D bytes per database) / ((N posts per timeperiod)*(S bytes per post)) = D/(N*S) = 200MB/(N*S) = timeperiods per database
```
#### Designing the Database

The database should be fairly simple:

* | Date/Time | Measured GPIO Input |

We could hypothetically also add an ID, but the timestamp itself could serve as an ID.

This does not assume any buffering if there is a lost WiFi connection, this just assumes the connection is always on.

Other ideas for things to add:

* Signal Strength - maybe over the last X timestamps, capture over time and send a batch of most recent measurements
* Temperature - there is an inaccurate onbaord temperature monitoring mechanism. https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#measuring-temperatures
* CPU - this shouldn't vary too much, but could be interesting to see if it changes with temperature, or if we remote into the RPi or something.

There is also EEPROM, so hypothetically a state could be stored.


### Writing a Simple Python Program to Send Data to ElephantSQL

```
#!/usr/bin/python

import os
import urllib.parse as up
import psycopg2

up.uses_netloc.append("postgres")
url = up.urlparse(os.environ["DATABASE_URL"])
conn = psycopg2.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
)
```
After running this, I get an error:

```
from psycopg2._psycopg import (                     # noqa
ImportError: libpq.so.5: cannot open shared object file: No such file or directory
```
However, I thought I had installed psycopg2, using ```pip3 install psycopg2```

After attempting to install it again, we get:

```
Requirement already satisfied: psycopg2 in /usr/local/lib/python3.7/dist-packages (2.9.3)
```
So first off, I should find the path:

```
find / -name libpq.so.5
```
This turns up with nothing.  However, it appears that we have to install postgres on our RPi, even if we are accessing a remote database.
Psycopg2 assumes that you have various postgres libraries installed.

However, installing postgres overall may be overcall, you may only need libpq5.

```
sudo apt install postgresql --fix-missing

sudo apt install libpq5 --fix-missing

```
Neither of these seemed to work!

Attempted to install the library via:

```
pip3 install libpq 
```
However, then we get a, "404 Client," not found for pypi.org.

So, we may not even be connected to the internet!

Somehow our attempt to connect via the URL may have caused a problem with our nameserver or something.

#### Attempting to Connect and Write Data

```
root@raspberrypi:/home/bin# cat /etc/resolv.conf
# Generated by resolvconf
nameserver 10.0.2.3
```
This means the container is obtaining an incorrect nameserver.  Rather than doing something fancy to fix this, just restart the container:

```
docker run --name rpi_container -it lukechilds/dockerpi
```
Of course we lost the previous state of the container, but we can go back and re-install stuff, we're still at the playing around point and don't really need everything yet.

After re-setting up the container, it worked and we were able to successfully install and fix errors. The setup method used was put into a setup script for the Rpi.

Attempting to connect again with our stock Python code shown above, I get a KeyError this time.

```
  File "/usr/lib/python3.7/os.py", line 678, in __getitem__
    raise KeyError(key) from None
KeyError: '[DATABASE_URL}'
```
With our database URL being the combination of our password.

We can also pipe data to a new database:

```
pg_dump postgres://user:pass@host/db | psql postgres://user:pass@host2/newdb
```

However, I was able to connect using the standard psycopg2.connect methodology:

```
conn = psycopg2.connect("dbname='my_dbname' user='my_user' host='my_host' password='my_password'")
```

Attempted to connect with the above through Google Colab notebooks, which threw a typeError, so it's likely prevented on CoLab.

Setting Up a Docker Debian to do the same thing (in order to manage the environment):

```
docker build -t sampledebianbullseye-slim .

(with)

# syntax=docker/dockerfile:1
FROM debian:bullseye-slim
```
Ran container:

```
docker run --name sampledebianbullseye-slim_container -it sampledebianbullseye-slim /bin/bash
```
Installing prerequisites:

(python already installed)

```
apt-get -y update
apt-get -y install python3-pip
apt-get install -y nano
pip install postgres
pip install psycopg2-binary
pip install config
```
However, running our code we still get the same error as in Colab.

https://www.postgresqltutorial.com/postgresql-python/insert/

Eventually, using CoLab, we get the database setup and write working, with the following procedures:

* Table Setup

```
#!/usr/bin/python

import psycopg2

def create_tables():
    """ create tables in the PostgreSQL database"""
    command = (
        """
        CREATE TABLE rpibatterydata (
            datapoint_id SERIAL PRIMARY KEY,
            battery_voltage NUMERIC NOT NULL,
            temperature NUMERIC NOT NULL,
            signal_strength NUMERIC NOT NULL,
            cpu_percent NUMERIC NOT NULL
        )
        """)
    conn = None
    try:
        # read the connection parameters
        # params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect("dbname='riobslkg' user='riobslkg' host='kashin.db.elephantsql.com' password='4JLeCneouzv2zA9p40L_xnnFZAj9rPAB'")
        cur = conn.cursor()
        # create table
        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

```
* Write One Piece of Data

```
import psycopg2
# from config import config

def insert_voltage(battery_voltage):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO rpibatterydata
             VALUES (%s,%s,%s,%s,%s) RETURNING datapoint_id;"""
    conn = None
    datapoint_id = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname='riobslkg' user='riobslkg' host='kashin.db.elephantsql.com' password='4JLeCneouzv2zA9p40L_xnnFZAj9rPAB'")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, battery_voltage)
        # get the generated id back
        datapoint_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("psycopg2.DatabaseError: ",error)
    finally:
        if conn is not None:
            conn.close()

    return datapoint_id


```

* I had to manually update the database_id in order to be able to write data. Since the data is time-series based, it might be better to just use a timeseries datapoint rather than an iterated key, which would require some kind of syncing to keep the database up to date, in which case it might better to use an ORM such as SQLAlchemy.

* Potentially, I could create local backups by just having the RPi write to a giant text file in .dumps format, which could be used to spin up a database at any point from scratch, so if there is ever a large gap in the data, we could recover it on the physical device.

* To simplify and start off with, the RPi could just be programmed to write data as it becomes available, writing to the backup file in parallel without verifying and buffering to ensure the remote postgres database is correct. Then I could manually extract the dumps file and ensure that all data is reported, or double check to see if there have ever been any drops in the data. If there are lots of drops due to losing WiFi connection, or for whatever other reason, we could always create some kind of buffering / syncing / update rule.

* For now, the larger priority is figuring out what time format should be used to write the data_id.


##### Time Formats in POSTGRESQL

https://www.postgresql.org/docs/9.1/functions-formatting.html

There are data type formatting functions:

* to_timestamp(text, text)	timestamp with time zone	convert string to time stamp	to_timestamp('05 Dec 2000', 'DD Mon YYYY')
* to_timestamp(double precision)	timestamp with time zone	convert Unix epoch to time stamp	to_timestamp(1284352323)

So the two main timestamps which have native-postres conversion functions available are:

* Epoch Time
* Time String, various formats.

Previously we had managed to print the time to the terminal with:

```
f.write("The time is now " + time.ctime())
```


* A better option would be to just write a string in ISO 8601 format, not worrying or thinking about daylight savings time, etc.
* This way we don't have the RPi do any extra work locally to convert anything, we just have it send data at a timestamp.


```
# datetime in 8601 format
import datetime
print(datetime.datetime.now().isoformat())
print(datetime.datetime.utcnow().isoformat())
# need to handle daylight savings time if reporting local timezone
```

### Handling Software and Deploying to RPi

* Hypothetically, it would be best to handle all of this software as a release on Github, and allow the Rpi to download whatever release to update its own software as necessary in the same way it installs other tools.
* It would be best to be able to temporarily shut down the old code, then download a release, and then restart the new code.
* If this could eventually be done as a command-line shell command remotely, that would be great too.

* This hypothetically means putting together a software package as a single Github repo, which the RPi will download and update based upon the release number on Github.

* Things like database secrets could be kept as environmental variables on the local machine, or on AWS-SSM Parameter store.
* It would be a good practice to get the RPi actually set up to communicate with Github via a publickey, as discussed elsewhere in this build document.


### Collecting Cloudcover Data

https://github.com/pwdel/rpizwsolar

We can set up an application which collects this data continuously and run it on an Ubuntu or Debian instance on Docker, until it later hopefully gets migrated to the web.

This application could also work on the principle of releases from Github.

```
list__dt which lists the time in postfix time
list__weather__main which lists out whether it's clear or cloudy
list__clouds__all which lists clouds as a numerical percentage of cover
wind speeds and directions
time in readible ISO format
list__dt_txt
sunrise and sunset for the location, listed in GPS coordinates.
```

* We could write 96 columns every hour on the hour, which gives 96 timestamps forecast for the following days.
* We could also write the actual vs. forecasted weather, perhaps to a different table.

* The limitation on the API call within the free plan is 1M/month, which is about one call every two seconds for a 31 month day.
* Based upon this, the limitation is likely the ElephantSQL database, not the OpenWeatherMap API.  We can count the number of bytes and determine how many, "years" worth of database we have.
* https://mothereff.in/byte-counter

Let's say we have:

1. Battery Voltage Level Coming In - 5 tabs, 3 charaters per tab, rounding up to 30 characters

* 30 bytes per row

2. OpenWeatherAPI data - 
2.1. Current Weather Data - 736 bytes raw API Call
2.2. Hourly Forecast, 4 Days (96 timestamps) - 66,223 or 66.2kb per raw API Call.


There is also a solar radiation API.

* https://openweathermap.org/api/solar-radiation


#### Creating a Cron Job

* Start out by creating a super simple python script which just writes, "hello world" to a file.

```
#!user/bin/python3
import time

# open file as f
# append text with 'a'
with open('readme.txt', 'a') as f:
    # get the time
    timenow = time.ctime()
    # create a string to input to f.write()
    entrystring = timenow + ' ' + 'hello world'
    # write the string
    f.write(entrystring)
    f.writelines('\n')    
```

Next, we create a chrontab expression with crontab guru. https://crontab.guru/

The following will execute, "at minute 1" - basically, every minute.  Recall that fractions can be used if sub-minute expressions are needed.

```
1 * * * *
```

We find out where python3 is with, "which python3"

```
which python3
/usr/bin/python3
```

We then use, "crontab -e" to enter the crontab editor.

If this doesn't work, we need to read about crontab files.  https://manpages.debian.org/jessie/cron/crontab.5.en.html

Basically, need to install, "cron" for the usage of, "crontab" :

```
sudo apt-get -y install cron
```
Then, using, "crontab -e" will open up a file:

```
# Edit this file to introduce tasks to be run by cron.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command

1 * * * * /usr/bin/python3 /home/bin/writetofile.py
```

* The format of the job added above is, "crontab_schedule command_path file_path"

The job can be listed with, "crontab -l" which is the same as cat'ing the cronfile.

Checking the file to see if it's being written to, you may have to verify that it's working.

```
update-rc.d cron defaults
/etc/init.d/cron start
```

We need to install systemctl

```
apt-get install -y systemctl

...

systemctl status cron
cron.service - Regular background program processing daemon
    Loaded: loaded (/lib/systemd/system/cron.service, enabled)
    Active: inactive (dead)

```

This shows that cron.service is dead.  So we need to activate it:

```
systemctl enable cron.service
systemctl start cron.service
```
This didn't seem to work.

```
systemctl enable cron.service
systemctl start cron.service
systemctl status cron.service
```

1. We may need to give write permission to the script.

```
chmod a+x writetofile.py
```

2. Need to add proper interrobang at start of python file:

```
#!/user/bin/python3
```
3. Find the realpath of the python file:

```
realpath writetofile.py
/home/bin/writetofile.py
```
4. Find the real path of python3 itself:

```
which python3
/usr/bin/python3
```

Wrong environment problem:

https://askubuntu.com/questions/23009/why-crontab-scripts-are-not-working

##### The PATH Variable

In order to understand why this is not working, we need to understand the concept of, "PATH."

Basically, $PATH is a list of directories, physical directories which act as a pointer for which, when we tell a shell to activate a script, it goes into $PATH and looks through a list of directories for the particular script name, in order, and executes the first script mathing the name in question.

The default setup for path in debian is:

```
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:
```

Which means that upon activating a script, the shell would look through, in order:

* /usr/local/sbin
* /usr/local/bin
* /usr/sbin
* /usr/bin
* /sbin
* /bin

...in order.

> PATH is an environmental variable in Linux and other Unix-like operating systems that tells the shell which directories to search for executable files (i.e., ready-to-run programs) in response to commands issued by a user. It increases both the convenience and the safety of such operating systems and is widely considered to be the single most important environmental variable.

Note that, "bin" is the most core, important folder, where the most system-critical elements are typically stored, whereas /usr/local/sbin are less system critical, like a package manager for applications, which are stored in /usr/local/bin

So the shell goes through less critical folders first before moving onto more critical folders - which is a safer way of operating.

We can add to a path by doing:

```
export PATH="$PWD:$PATH"
```
...which would add the current directory to $PATH, starting from the left, so basically in the safest and most recent position.  So if we had a script, such as writetofile.py, sitting in /home/bin, and we added it to path:

To add this permanently to the path, we would need to edit bashrc.

```
nano ~/.bashrc

export PATH="/home/bin/:$PATH"
```
Then we could restart this by running, "source ~/.bashrc"

...Which permanently adds /home/bin/ to the $PATH variable, after closing and restarting the terminal.

Also very important, is to make sure that the proper path is being used at the top of the python file to instruct which interpreter is to be used.  We must use, "#!/usr/bin/python3" and not "#!/user/bin/python3" otherwise the file won't know what interpretor to use.

So now that we know what the $PATH variable is, we need to understand that the crontab does not see the $PATH variable from withinside of it. Additionally, crontab does not interpret $VARIABLES, it only reads things literally. So we have to add a literal path variable into the crontab file:

```
# PATH VARIABLE TO APPLY TO ALL CRONJOBS
PATH=/home/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

Which will instruct the cron to look into all of these folders for the executable in question.

We can double check that this is what the cron understands is the path by adding the job:

```
* * * * * env > /tmp/env.output
```

and then looking at the file after it changes (after the cron job runs):

```
cat /tmp/env.output
PATH=/home/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

Once everything is fixed, the actual job itself calling the python script can run, adding to crontab -e:

```
* * * * * writetofile.py
```

Now it should work, but where is the file being sent?

By default, the crontab belongs to root, and a user can be selected with "-u" as well.

So, we look in the ~/root folder to see the readme.md file.

If we want the file to be written somewhere else, for example, an output file under /home/output we do:

```
* * * * * cd /home/output && writetofile.py
```
Now when we go cd into /home/output and look, there should be a readme.txt file in there with an actual timestamp, per what we programmed.

Note that everything after the function call * * * * * is essentially a shell function, and differing lines must be connected with a logical connector such as &&, but multiple actions and scripts could be set up to be run.

### Tying It All Together for Collecting Weather Data

* Since we have established the following abilities:

- Setup run a cron job
- Setup a custom /hom/bin and $PATH
- Setup remote postgres table
- Write to remote postgres table
- Call from OpenWeatherMap API

* Now it would seem to make sense to tie this all together in a deployable, "release," designed to turn into an application which deploys on a Heroku instance, for example, or just runs on whatever local machine, to do the work of adding data to the database on a regular basis.
* This application could be in a seperate repo from any software that runs on the RPi, which would be perhaps a Cron job that reads GPIO levels, translates it to voltage data and writes that to another database table.

The combination of the above would be the sum total of the data collection interfaces.

* Need to understand how to use SQLAlchemy to make organization of SQL Calls easier.
* Need to be able to install everything needed in Dockerfile, including cron job
* Need to be able to run an entrypoint script, which kicks off daemons, creates cron job, unfurls everything when Docker deployed.
* Use environmental variables throughout code to keep secure and allow code with releases - include ENV setup in readme.

### Having the RPi Read from Another Application

* Hypothetically, RPI could curl a Flask application endpoint, it doesn't even have to be an API, where the endpoint reports whether the RPi should stay on or turn off.
* Having it non-public would be more secure, having it as an API, or just having some kind of code that means off vs. ON or whatever behavior.
* Part of the problem is of course, we don't have a way to turn the RPi back on, we would need some other kind of microcontroller in the circuit to do that.
* We also would need some kind of understanding of what the RPi is going to be doing, what the payload is, what kind of on/off pattern we want in general.
* The most logical would be fore the RPi to just collect solar data and then shut down prior to sunset, to be turned back on prior to sunrise.
* In extreme circumstances where the battery didn't get enough power, we could opt to shut the RPi down, for it to be turned on the next day.
* The following day, it could report the battery voltage in the morning, and given a new calculation check the new, "Report" from the flask applciation, 
which could tell the RPi whether to stay shut off for another day (basically, skip a day of voltage monitoring).
* If the RPI skips a day of monitoring, the assumption would be that the battery voltage is going to go up if the forecast shows sunny.
* After reporting the new voltage again the following day, the RPI can wait again for a new report based upon the new battery voltage and upcoming weather, and be told to either 
skip another day, or to go ahead and monitor voltage for the day.

After running this algorithm for a while, it can always be refined for seasonality, battery age, and various other factors.

What we would be optimizing for is uptime and just maximum operation of being able to monitor solar input (via the battery voltage), given a solar panel size.

If the solar panel is too big and battery is too big, it will never need to shut down, we monitor 365 days.

We don't want to monitor 365 days, we can make statistical assumptions that certain years are going to be like past years, so we only need to monitor X number of days
in order to build improved models for future years.

There may be other unforseen factors such as capability to connct to WiFi, we may need to tell the RPI what to do in the scenario that it can't connect...basically a wait to
connect time.

### Hardware Used to Monitor Voltage

https://www.ti.com/lit/ds/symlink/ads1015.pdf


### Power Consumption

There are different strategies for reducing Raspberry Pi Power consumption which have to do with shutting down different interfaces, clocking down the CPU, etc.

https://blues.io/blog/tips-tricks-optimizing-raspberry-pi-power/

There are also hardware-oriented strategies.

Noteable as well, there are also ready-built solar battery optimization kits for Raspberry Pi.

https://www.arrow.com/en/research-and-events/articles/can-you-run-a-raspberry-pi-on-solar-power 


### Installing Ngrok

https://medium.com/@gaelollivier/connect-to-your-raspberry-pi-from-anywhere-using-ngrok-801e9fd1dd46

equinox certificate expired

https://www.mathewjenkinson.com/how-to-install-ngrok-on-a-raspberrypi/

This should be added to the setup script:

```
sudo apt-get update -y && sudo apt-get upgrade -y
```

Then:

```
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
The certificate of ‘bin.equinox.io’ is not trusted.
```
Use the --no-check-certificate flag.

We may need to change the mv command below.  Note!  The first time we tried this, we did not cd into /tmp, but is recommended to cd into /tmp first before running wget.

```
sudo wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
sudo unzip ngro*
sudo mkdir ~/ngrok
sudo mv ngrok ~/ngrok
```
We didn't seem to be able to make an executable, regardless of where we put ngrok. However, if we attempt to use it in the folder we're in:

```

grok by @inconshreveable                                       (Ctrl+C to quit)

Session Status                online
Session Expires               1 hour, 59 minutes
Version                       2.3.40
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://c613-207-153-48-94.ngrok.io -> http://local
Forwarding                    https://c613-207-153-48-94.ngrok.io -> http://loca

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```
When we attempted to tunnel in, we got:

```
The connection to https://c613-207-153-48-94.ngrok.io was successfully tunneled to your ngrok client, 
but the client failed to establish a connection to the local address localhost:3000.
```
So, we try this again, but instead of using port 3000, we use 4040.  In this situation, we got:

```
./ngrok http 4040
ERR_NGROK_6022
Before you can serve HTML content, you must sign up for a free ngrok account and install your authtoken.
```
Fair enough, at least the tunnel worked.

But can we tunnel in using ssh and not HTML?

Yes, we can, using, "tcp 22" rather than "html".

```
./ngrok tcp 22
TCP tunnels are only available after you sign up.
Sign up at: https://dashboard.ngrok.com/signup

If you have already signed up, make sure your authtoken is installed.
Your authtoken is available on your dashboard: https://dashboard.ngrok.com/get-started/your-authtoken

ERR_NGROK_302
```
So to setup our authtoken, there's a ready-made screen with the ngrok command ready and the authtoken listed:

```
sudo ngrok authtoken [AUTHTOKEN]
```
Now attempting the tcp command again:

It looks like there is actually a way to do an ngrok tunnel without even using the ngrok agent, by basically using an SSH public key.

When we attempt to connect, it doesn't let us, it does another 404 not found error and asks us to sign up for an account.

There is also advice, "restart the ngrok agent."

It seems that the ngrok agent is not picking up the auth token, probably because we're running it from a random location.

We can try the alternate tunneling method, rather than using the ngrok agent.

```
ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/pi/.ssh/id_rsa):
Could not create directory '/home/pi/.ssh': No space left on device
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Saving key "/home/pi/.ssh/id_rsa" failed: No such file or directory
```
Doing a fancier version that sets up folders ahead of time:

https://www.raspberrypi-spy.co.uk/2019/02/setting-up-ssh-keys-on-the-raspberry-pi/

Through a bunch of commands, I was able to connect.  However, then we get a different error:

```
socket: Address family not supported by protocol
connect_to localhost port 80: failed.
ERR_NGROK_3004
ngrok gateway error The server returned an invalid or incomplete HTTP response.
```

So this doesn't seem to work either.

Looking into the "Your Authentication" section of the ngrok website, we see that it mentions:

```
Alternatively, you can directly add the Authtoken to your ngrok.yml configuration file. By default this file is located at ~/.ngrok2/ngrok.yml.
```

When we look into this location, we can't find it on the raspberry pi.

Instead, the command is saying that the Authtoken is being saved to, "/root/.ngrok2/ngrok.yml"

Using the snapd store:

```
sudo apt update
sudo apt install snapd
sudo reboot
```

but rebooting kicked us out of the Rpi!

Otherwise, we should have been able to do:

```
sudo snap install core
sudo snap install ngrok
```

