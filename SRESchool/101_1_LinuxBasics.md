## About Linux
### New things learned about linux:

* There is a way to make kernal commands from user mode.
* [Creating a Hello World Kernal Module](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN121)

### Comamand Line Basics
#### File System Organization

* bin | The executable program of most commonly used commands reside in bin directory
* sbin | This directory contains programs used for system administration.
* home | This directory contains user related files and directories.
* lib | This directory contains all the library files
* etc | This directory contains all the system configuration files
* proc | This directory contains files related to the running processes on the system
* dev | This directory contains files related to devices on the system
* mnt | This directory contains files related to mounted devices on the system
* tmp | This directory is used to store temporary files on the system
* usr | This directory is used to store application programs on the system

#### Added Commands to Devops Tools Library

* sed
* sort

##### Comparing to a Desktop or Laptop Environment or Web Server Environment

* Note - the "usr" file is more like, "Applications" in MacOS. On a webserver this might be where var/www is placed.
* /home/ is more like the /home directory in MacOS, with perhaps Documents, Downloads or other files stored here.

### Linux Administration

Run the following to get started:

```
docker run -it --name test registry.access.redhat.com/ubi8 bash
```
#### Multi-User Operating Systems

* Whenever multiple users can log in and not affect one another's filesystems or preferences, it's multi-user.
* Server administration is mostly concerned with servers that are physically distant from our physical selves.
#### Group Management

##### id Command

Running command:

```
[root@5bbb45ed5b82 /]# id
uid=0(root) gid=0(root) groups=0(root)
```
gid/uid associated with root is 0.

##### /etc - files associated with users and groups

Stores the username, uid, gid, home directory, login shell, etc.

```
[root@5bbb45ed5b82 /]# cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:65534:65534:Kernel Overflow User:/:/sbin/nologin
tss:x:59:59:Account used for TPM access:/dev/null:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
systemd-coredump:x:999:997:systemd Core Dumper:/:/sbin/nologin
systemd-resolve:x:193:193:systemd Resolver:/:/sbin/nologin
```
stores password associated with users - [shadow file formats](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/shadow-file-formats.html)

Notes

* username:password:dayssince19700101:daysuntilpasswordchange:daysuntilpasswordmustchange

* after this point, these empty fields ::: --> 

* daystowarnuserpassword:daysafterpasswordexpiresdisable:dayssince19700101disabled:reserved

```
[root@5bbb45ed5b82 /]# cat etc/shadow
root:!locked::0:99999:7:::
bin:*:18367:0:99999:7:::
daemon:*:18367:0:99999:7:::
adm:*:18367:0:99999:7:::
lp:*:18367:0:99999:7:::
sync:*:18367:0:99999:7:::
shutdown:*:18367:0:99999:7:::
halt:*:18367:0:99999:7:::
mail:*:18367:0:99999:7:::
operator:*:18367:0:99999:7:::
games:*:18367:0:99999:7:::
ftp:*:18367:0:99999:7:::
nobody:*:18367:0:99999:7:::
tss:!!:18926::::::
dbus:!!:18926::::::
systemd-coredump:!!:18926::::::
systemd-resolve:!!:18926::::::
```
stores information about groups on the system

* username:passwordfield (x)::userid:groupid:fullname:homedirectory:shell

```
[root@5bbb45ed5b82 /]# cat /etc/group
root:x:0:
bin:x:1:
daemon:x:2:
sys:x:3:
adm:x:4:
tty:x:5:
disk:x:6:
lp:x:7:
mem:x:8:
kmem:x:9:
wheel:x:10:
cdrom:x:11:
mail:x:12:
man:x:15:
dialout:x:18:
floppy:x:19:
games:x:20:
tape:x:33:
video:x:39:
ftp:x:50:
lock:x:54:
audio:x:63:
users:x:100:
nobody:x:65534:
utmp:x:22:
utempter:x:35:
tss:x:59:
dbus:x:81:
input:x:999:
kvm:x:36:
render:x:998:
systemd-journal:x:190:
systemd-coredump:x:997:
systemd-resolve:x:193:
```
#### Important Commands for Managing Users

* useradd - Creates a new user
* passwd - Adds or modifies passwords for a user
* usermod - Modifies attributes of an user
* userdel - Deletes an user

##### useradd

```
[root@5bbb45ed5b82 /]# useradd shivam
[root@5bbb45ed5b82 /]# tail /etc/passwd | grep shivam
shivam:x:1000:1000::/home/shivam:/bin/bash

[root@5bbb45ed5b82 /]# useradd amit -s /bin/sh
[root@5bbb45ed5b82 /]# tail /etc/passwd | grep amit
amit:x:1001:1001::/home/amit:/bin/sh
```

##### passwd

```
[root@5bbb45ed5b82 /]# passwd shivam
Changing password for user shivam.

[root@5bbb45ed5b82 /]# tail /etc/shadow | grep shivam
shivam:$6$nVwJXfR.UlNAuks9$lXouOQs6tYAO5sTVH/dsqD6C5s2f2uObhsgI30jkYlhNIO89Eutn4alHkVVCYq/oBtIJ8u87TLBHj/vBGngCr0:18936:0:99999:7:::
```

##### usermod

```
[root@5bbb45ed5b82 /]# usermod amit -s /bin/bash
[root@5bbb45ed5b82 /]# tail /etc/passwd | grep amit
amit:x:1001:1001::/home/amit:/bin/bash
```
##### userdel

```
[root@5bbb45ed5b82 /]# userdel amit
[root@5bbb45ed5b82 /]# tail /etc/passwd | grep amit
[root@5bbb45ed5b82 /]# 
```
#### Managing Groups

* groupadd\(groupname) - create a new group
* groupdel\(groupname) - delete group
* gpasswd\(groupname) - modifies password for group

#### Superuser SU

Assigning SU capability to a user:

```
su shivam
[root@5bbb45ed5b82 /]# su shivam
[shivam@5bbb45ed5b82 /]$ whoami
shivam
[shivam@5bbb45ed5b82 /]$ tail /etc/shadow
tail: cannot open '/etc/shadow' for reading: Permission denied
[shivam@5bbb45ed5b82 /]$ exit
exit
[root@5bbb45ed5b82 /]# 
```
* Only root can open /etc/shadow.
* We can set up a password with the passwd command.
* Within RedHat machines, the capability to invoke sudo is not installed by default, so we can install sudo.

```
[root@5bbb45ed5b82 /]# yum install sudo
Updating Subscription Management repositories.
...
Complete!

[root@5bbb45ed5b82 /]# grep "root" /etc/sudoers
## the root user, without needing the root password.
## Allow root to run any commands anywhere 
root	ALL=(ALL) 	ALL
## cdrom as root
```
We can use the, "wheel" group, which gives an, "all command" privledge to a user.  We use, usermod -append -Group:

```
[root@5bbb45ed5b82 /]# grep "wheel" /etc/sudoers
## Allows people in group wheel to run all commands
%wheel	ALL=(ALL)	ALL
# %wheel	ALL=(ALL)	NOPASSWD: ALL

[root@5bbb45ed5b82 /]# usermod -a -G wheel shivam
[root@5bbb45ed5b82 /]# id shivam
uid=1000(shivam) gid=1000(shivam) groups=1000(shivam),10(wheel)
```
Switch back to shivam and view etc/shadow:

```
[shivam@5bbb45ed5b82 /]$ sudo tail /etc/shadow

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.


[sudo] password for shivam: 
mail:*:18367:0:99999:7:::
operator:*:18367:0:99999:7:::
games:*:18367:0:99999:7:::
ftp:*:18367:0:99999:7:::
nobody:*:18367:0:99999:7:::
tss:!!:18926::::::
dbus:!!:18926::::::
systemd-coredump:!!:18926::::::
systemd-resolve:!!:18926::::::
shivam:$6$nVwJXfR.UlNAuks9$lXouOQs6tYAO5sTVH/dsqD6C5s2f2uObhsgI30jkYlhNIO89Eutn4alHkVVCYq/oBtIJ8u87TLBHj/vBGngCr0:18936:0:99999:7:::
[shivam@5bbb45ed5b82 /]$ 
```
#### File Permissions

We can see the file permissions by listing as root:

```
[root@5bbb45ed5b82 /]# ls -l /etc/passwd
-rw-r--r-- 1 root root 810 Nov  5 23:35 /etc/passwd
```

Similar to users, the interpretation of the file permissions are listed in groups:

1. - Type of file... - denotes regular, d denotes directory.
2. rw- ... read, write, execute by the file owner.
3. r-- ... read, write and execute permissions of the group owner. Users in the group can only read the file.
4. r-- read, write and execute permissions of all other users.
5. root - name of the owner
6. root - name of the group owner of the file

##### chmod

* Used to modify files and directories permissions in linux.

There are different ways of presenting the permissions; rwx, Binary and Decnimal which are listed below.

* Read, write and execute	rwx	111	7
* Read and write	rw-	110	6
* Read and execute	r-x	101	5
* Read only	r--	100	4
* Write and execute	-wx	011	3
* Write only	-w-	010	2
* Execute only	--x	001	1
* None	---	000	0

###### Creating a New File and Changing Permissions

```
[root@5bbb45ed5b82 other]# touch test_file
[root@5bbb45ed5b82 other]# ls -l test_file
-rw-r--r-- 1 root root 0 Nov  8 22:22 test_file
[root@5bbb45ed5b82 other]# chmod 664 test_file
[root@5bbb45ed5b82 other]# ls -l test_file
-rw-rw-r-- 1 root root 0 Nov  8 22:22 test_file
```
So in the above we created a file and gave the group write permissisons.

Note:

* 6 rw- for the owner
* 6 rw- for the group
* 4 r-- for all other users.

##### chown

The chown command is used to change the owner of a file.

```
[root@5bbb45ed5b82 other]# ls -l test_file
-rw-rw-r-- 1 root root 0 Nov  8 22:22 test_file
[root@5bbb45ed5b82 other]# chown shivam test_file
[root@5bbb45ed5b82 other]# ls -l test_file
-rw-rw-r-- 1 shivam root 0 Nov  8 22:22 test_file
```

##### chgrp

* Used to change the group ownership.

```
[shivam@5bbb45ed5b82 other]$ chgrp shivam test_file
[shivam@5bbb45ed5b82 other]$ ls -l test_file
-rw-rw-r-- 1 shivam shivam 0 Nov  8 22:22 test_file
```

#### ssh

Passwordless authentication with SSH.

##### Generating Public-Private Keypair

> if we have a keypair stored in ~/.ssh directory, we don't need to generate keys again.

After installing:

```
[shivam@5bbb45ed5b82 other]$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/shivam/.ssh/id_rsa): 
Created directory '/home/shivam/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/shivam/.ssh/id_rsa.
Your public key has been saved in /home/shivam/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:skf6B8n7jH95aFDSEWrXpUt760zM8Kjlp1a5DeSkz0g shivam@5bbb45ed5b82
The key's randomart image is:
+---[RSA 3072]----+
|            ..  .|
|           ... o |
|          o...+  |
|         ...o.oo |
|      ..S. o *o o|
|       =+ . E O+.|
|      o .o o O.Bo|
|       o.o. X.Bo.|
|        o+++.+oo |
+----[SHA256]-----+
```
We can now see two keys present in the ~/.ssh directory.

```
[shivam@5bbb45ed5b82 other]$ ls -l ~/.ssh/
total 8
-rw------- 1 shivam shivam 2610 Nov  8 23:08 id_rsa
-rw-r--r-- 1 shivam shivam  573 Nov  8 23:08 id_rsa.pub
```
You have to be able to copy the rsa-id, for that we install:

```
sudo yum install -y openssh-clients
```
We now have a test host available.

```
[shivam@5bbb45ed5b82 other]$ ssh-copy-id test_host@121.39.9
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/shivam/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed

/usr/bin/ssh-copy-id: ERROR: ssh: connect to host 121.39.0.9 port 22: Connection refused

```
In this case, we don't have an example host set up, but we have connected to a remote host plenty of times in the past, so we will leave this be for now.

##### Running Commands on Remote Host

* use ssh

##### Transfer Files to Another Host

* use scp

#### Package Management

This is the process of installing and managing software set up on a system.  There are different packaging systems:

* Debian - .deb ... used in Debian, Ubuntu
* Red Hat Style - .rpm ... used in Fedora, CentOS, RHEL

Popular packaging systems:

* yum
* dnf

Usage:

* yum install \packagename
* yum update, yum search, yum remove, etc.

You can search for packages using, "yum search" - 

```
Last metadata expiration check: 5:45:21 ago on Mon Nov  8 17:43:13 2021.
==================================================== Name Exactly Matched: httpd ====================================================
httpd.x86_64 : Apache HTTP Server
======
```

So given there is an exact match, we can then install it and then remove it:

```
[shivam@5bbb45ed5b82 other]$ sudo yum install httpd
...
Complete!
...
sudo yum remove httpd
Complete!
```

#### Process Management

* ps is the default process inspector. If you don't have it, you can install it.

* You can use grep along with ps to filter out a specific process by name.

```
[shivam@5bbb45ed5b82 other]$ sudo yum install procps

[shivam@5bbb45ed5b82 other]$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0  19240  3688 pts/0    Ss   Nov05   0:00 bash
root       178  0.0  0.0 109060  5816 pts/0    S    23:05   0:00 su shivam
shivam     179  0.0  0.0  19240  3780 pts/0    S    23:05   0:00 bash
shivam     332  0.0  0.0  51856  3724 pts/0    R+   23:33   0:00 ps aux

[shivam@5bbb45ed5b82 other]$ ps -p 98
  PID TTY          TIME CMD

[shivam@5bbb45ed5b82 other]$ ps | grep -i 'bash'
  179 pts/0    00:00:00 bash

```

* top shows information about linux processes running on the system in real time.

```
top - 23:35:08 up 7 days,  4:54,  0 users,  load average: 0.24, 0.38, 0.52
Tasks:   4 total,   1 running,   3 sleeping,   0 stopped,   0 zombie
%Cpu(s):  4.8 us,  6.3 sy,  0.0 ni, 88.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :  16012.8 total,   3196.1 free,   2963.1 used,   9853.6 buff/cache
MiB Swap:   1024.0 total,   1024.0 free,      0.0 used.  12304.3 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                        
    1 root      20   0   19240   3688   3144 S   0.0   0.0   0:00.17 bash                                                           
  178 root      20   0  109060   5816   4960 S   0.0   0.0   0:00.00 su                                                             
  179 shivam    20   0   19240   3780   3220 S   0.0   0.0   0:00.08 bash                                                           
  338 shivam    20   0   56336   4228   3588 R   0.0   0.0   0:00.00 top    
```
For each process, top lists down the process ID, owner, priority, state, cpu utilization, memory utilization and much more information. It also lists down the memory utilization and cpu utilization of the system as a whole along with system uptime and cpu load average.

Since this is a virtual machine, the machine availability is set within the VM Runtime, in this case Docker.

#### Memory Management

* free

```
[shivam@5bbb45ed5b82 other]$ free
              total        used        free      shared  buff/cache   available
Mem:       16397084     3032984     3273908      458824    10090192    12600840
Swap:       1048572           0     1048572
```
* vmstat shows additional information about io and cpu usage.

```
[shivam@5bbb45ed5b82 other]$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 7  0      0 3274968 1001596 9088616    0    0     2    44   29   20  6  6 89  0  0
```


#### Checking Disk Space

* df - disk free

```
[shivam@5bbb45ed5b82 other]$ df
Filesystem     1K-blocks     Used Available Use% Mounted on
overlay        140105160 43841616  89116900  33% /
tmpfs              65536        0     65536   0% /dev
tmpfs            8198540        0   8198540   0% /sys/fs/cgroup
shm                65536        0     65536   0% /dev/shm
/dev/vda1      140105160 43841616  89116900  33% /etc/hosts
tmpfs            8198540        0   8198540   0% /proc/acpi
tmpfs            8198540        0   8198540   0% /sys/firmware
```

* du - disk use

```
[shivam@5bbb45ed5b82 other]$ du -h | head
4.0K	.
```
This only shows the directory that you are in at the moment.  If you move to the top directory, you can run the same command and see the top of the entire filesystem:

```
[shivam@5bbb45ed5b82 /]$ du -h | head
du: cannot read directory './home/amit': Permission denied
du: cannot read directory './var/lib/rhsm': Permission denied
du: cannot read directory './var/lib/portables': Permission denied
du: cannot read directory './var/lib/private': Permission denied
du: cannot read directory './var/db/sudo': Permission denied
4.0K	./home/other
12K	./home/shivam/.ssh
4.0K	./home/shivam/.config/procps
8.0K	./home/shivam/.config
40K	./home/shivam
4.0K	./home/amit
52K	./home
4.0K	./boot
4.0K	./opt
4.0K	./srv
```

#### Daemons

> A computer program that runs as a background process is called a daemon. Traditionally, the name of daemon processes ended with d - sshd, httpd etc. We cannot interact with a daemon process as they run in the background.

> Services and daemons are used interchangeably most of the time.

#### Systemd

* service manager for linux.
* Systemd units are the building blocks of systemd
* the below are unit configuration files available at /usr/lib/systemd/system which are distributed by installed RPM packages.

```
[shivam@5bbb45ed5b82 /]$ cd usr/lib/systemd/system
[shivam@5bbb45ed5b82 system]$ pwd
/usr/lib/systemd/system
[shivam@5bbb45ed5b82 system]$ ls | head
autovt@.service
basic.target
basic.target.wants
bluetooth.target
boot-complete.target
console-getty.service
container-getty@.service
ctrl-alt-del.target
dbus-org.freedesktop.hostname1.service
dbus-org.freedesktop.locale1.service
```

#### Managing System Services

* systemctl start name.service	Starts a service
* systemctl stop name.service	Stops a service
* systemctl restart name.service	Restarts a service
* systemctl status name.service	Check the status of a service
* systemctl reload name.service	Reload the configuration of a service

#### Logs

* Looking at, "cat /var/log/*" literally shows every single action on the machine, installation-wise.

Evidently it also contains:

* /var/log/* - system errors, booting/shutdown, configuration changes, etc.

* /var/log/authlog - contains system authorization related logs.

* /var/log/laslog - contains the recent login information of all users.

Kernel Logs - not permitted as a part of linux for the user to view or work with kernal commands.  This literally prints the message buffer of the terminal, including device commands.

It is possible to access this by changing settings.