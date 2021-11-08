# School of SRE

* [School of SRE - Linkedin Link](https://linkedin.github.io/school-of-sre/)
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

```
su shivam
[root@5bbb45ed5b82 /]# su shivam
[shivam@5bbb45ed5b82 /]$ whoami
shivam
[shivam@5bbb45ed5b82 /]$ tail /etc/shadow
tail: cannot open '/etc/shadow' for reading: Permission denied
```
* Only root can open /etc/shadow.


# Point Left Off At

https://linkedin.github.io/school-of-sre/level101/linux_basics/linux_server_administration/

# Resources

* [School of SRE - Linkedin Link](https://linkedin.github.io/school-of-sre/)
* [Switch to Kernal Mode from User Mode](https://stackoverflow.com/questions/11905934/how-to-switch-from-user-mode-to-kernel-mode)