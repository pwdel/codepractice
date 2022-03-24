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

