# Linux Intermediate

### Running Docker

* Using RHEL

```
docker run --rm -it -registry.accesss.redhat.com/ubi8 /bin/bash
```
## Package Management

* Runs other programs and software, installing and maintaining software.
### Package:

* In early days of linux, you had to download, compile it to install and then run. "Packages" contain software, dependencies, and metatdata instructions about the package.
### Dependencies

* Rare that software is stand-alone. Some repo's can contain thousands of depdencnies hosted remotely.
### Repository

```
sh-4.4# sudo dnf repolist all
Updating Subscription Management repositories.
Unable to read consumer identity

This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.

repo id                                 repo name                                                                  status
ubi-8-appstream                         Red Hat Universal Base Image 8 (RPMs) - AppStream                          enabled
ubi-8-appstream-debug                   Red Hat Universal Base Image 8 (Debug RPMs) - AppStream                    disabled
ubi-8-appstream-source                  Red Hat Universal Base Image 8 (Source RPMs) - AppStream                   disabled
ubi-8-baseos                            Red Hat Universal Base Image 8 (RPMs) - BaseOS                             enabled
ubi-8-baseos-debug                      Red Hat Universal Base Image 8 (Debug RPMs) - BaseOS                       disabled
ubi-8-baseos-source                     Red Hat Universal Base Image 8 (Source RPMs) - BaseOS                      disabled
ubi-8-codeready-builder                 Red Hat Universal Base Image 8 (RPMs) - CodeReady Builder                  enabled
ubi-8-codeready-builder-debug           Red Hat Universal Base Image 8 (Debug RPMs) - CodeReady Builder            disabled
ubi-8-codeready-builder-source          Red Hat Universal Base Image 8 (Source RPMs) - CodeReady Builder           disabled
sh-4.4#
```

### High Level and Low-Level Package management tools

1. Low-level tools: This is mostly used for installing, removing and upgrading package files.

2. High-Level tools: In addition to Low-level tools, High-level tools do metadata searching and dependency resolution as well.

* Debian - Lowlevel is "dpkg" whereas highlevel is "apt-get"
* Fedora/Redhat - lowlevel is, "dnf" which also functions as high level.

## Storage Media

### Listing the mounted storage devices

* The format in which we see above output is:
* device on mount_point type file\_system\_type (options)

```
sh-4.4# mount
overlay on / type overlay (rw,relatime,lowerdir=/var/lib/docker/overlay2/l/Z55U2EILO4X42CBAUVQHEOYSSU:/var/lib/docker/overlay2/l/ALPI6JGDZIOLDXNBUEZRLIYYGQ:/var/lib/docker/overlay2/l/6DXH2EWOOHP5QYTJDUOPC5FVSV,upperdir=/var/lib/docker/overlay2/bccbb915728d73c2c9577fcf9a6b3983dbf67c11754fcc204fac2bf7eb044c45/diff,workdir=/var/lib/docker/overlay2/bccbb915728d73c2c9577fcf9a6b3983dbf67c11754fcc204fac2bf7eb044c45/work)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev type tmpfs (rw,nosuid,size=65536k,mode=755)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=666)
sysfs on /sys type sysfs (ro,nosuid,nodev,noexec,relatime)
tmpfs on /sys/fs/cgroup type tmpfs (rw,nosuid,nodev,noexec,relatime,mode=755)
cpuset on /sys/fs/cgroup/cpuset type cgroup (ro,nosuid,nodev,noexec,relatime,cpuset)
cpu on /sys/fs/cgroup/cpu type cgroup (ro,nosuid,nodev,noexec,relatime,cpu)
cpuacct on /sys/fs/cgroup/cpuacct type cgroup (ro,nosuid,nodev,noexec,relatime,cpuacct)
blkio on /sys/fs/cgroup/blkio type cgroup (ro,nosuid,nodev,noexec,relatime,blkio)
memory on /sys/fs/cgroup/memory type cgroup (ro,nosuid,nodev,noexec,relatime,memory)
devices on /sys/fs/cgroup/devices type cgroup (ro,nosuid,nodev,noexec,relatime,devices)
freezer on /sys/fs/cgroup/freezer type cgroup (ro,nosuid,nodev,noexec,relatime,freezer)
net_cls on /sys/fs/cgroup/net_cls type cgroup (ro,nosuid,nodev,noexec,relatime,net_cls)
perf_event on /sys/fs/cgroup/perf_event type cgroup (ro,nosuid,nodev,noexec,relatime,perf_event)
net_prio on /sys/fs/cgroup/net_prio type cgroup (ro,nosuid,nodev,noexec,relatime,net_prio)
hugetlb on /sys/fs/cgroup/hugetlb type cgroup (ro,nosuid,nodev,noexec,relatime,hugetlb)
pids on /sys/fs/cgroup/pids type cgroup (ro,nosuid,nodev,noexec,relatime,pids)
rdma on /sys/fs/cgroup/rdma type cgroup (ro,nosuid,nodev,noexec,relatime,rdma)
cgroup on /sys/fs/cgroup/systemd type cgroup (ro,nosuid,nodev,noexec,relatime,name=systemd)
mqueue on /dev/mqueue type mqueue (rw,nosuid,nodev,noexec,relatime)
shm on /dev/shm type tmpfs (rw,nosuid,nodev,noexec,relatime,size=65536k)
/dev/vda1 on /etc/resolv.conf type ext4 (rw,relatime)
/dev/vda1 on /etc/hostname type ext4 (rw,relatime)
/dev/vda1 on /etc/hosts type ext4 (rw,relatime)
devpts on /dev/console type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=666)
proc on /proc/bus type proc (ro,nosuid,nodev,noexec,relatime)
proc on /proc/fs type proc (ro,nosuid,nodev,noexec,relatime)
proc on /proc/irq type proc (ro,nosuid,nodev,noexec,relatime)
proc on /proc/sys type proc (ro,nosuid,nodev,noexec,relatime)
proc on /proc/sysrq-trigger type proc (ro,nosuid,nodev,noexec,relatime)
tmpfs on /proc/acpi type tmpfs (ro,relatime)
tmpfs on /proc/kcore type tmpfs (rw,nosuid,size=65536k,mode=755)
tmpfs on /proc/keys type tmpfs (rw,nosuid,size=65536k,mode=755)
tmpfs on /proc/timer_list type tmpfs (rw,nosuid,size=65536k,mode=755)
tmpfs on /proc/sched_debug type tmpfs (rw,nosuid,size=65536k,mode=755)
tmpfs on /sys/firmware type tmpfs (ro,relatime)
```
### Creating a FileSystem

* All the data stored in the disk is in the form of one large chunk, with nothing to figure out where the data ends and begins.
* Filesystem (fs) tells where data ends and begins.
* Examples - FAT, NTFS, ext, ext4, HFS, HFS+, NFS, etc.
### Mounting the device

On Ubuntu virtual machine...

```
root@a93522e30f3d:/# apt-get -y install util-linux
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
util-linux is already the newest version (2.36.1-8).
util-linux set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 1 not upgraded.
root@a93522e30f3d:/# mount | grep "sdb1"
root@a93522e30f3d:/# mkfs -t ext4 /dev/sdb1
mke2fs 1.46.2 (28-Feb-2021)
The file /dev/sdb1 does not exist and no size was specified.

root@a93522e30f3d:/# mkfs -t ext4 /dev/sdb1
mke2fs 1.46.2 (28-Feb-2021)
mkfs.ext4: Device size reported to be zero.  Invalid partition specified, or
	partition table wasn't reread after running fdisk, due to
	a modified partition being busy and in use.  You may need to reboot
	to re-read your partition table.

```

On a regular linux machine or with appropriate settings, we should get a message showing that tables were allocated properly.

Once you have a formatted, "device" (akin to a USB) you can mount it with a series of commands to create a, "mount point."
### Unmounting the device

```
cd /mount
unmount /mount

target is busy

cd ~/
unmount /mount
mount | grep "sdb1"
```

* The first attempt did not unmount /sdb1 because we were, "inside" the storage device being used.  Jumping back out makes it work.
### Making it easier with /etc/fstab file?

In a production environment, there are servers with storage devices that need to be mounted, and it's not feasible to manually mount all of them.

* fstab, found in /etc/fstab

```
root@a93522e30f3d:/# cat /etc/fstab
# UNCONFIGURED FSTAB FOR BASE SYSTEM
```
If it were configured, it would come up.

* mount -a to reload file after making changes

### Checking and Repairing FS

* Filesystems encounter issues in case of hardware failure, power failure, improper shutdown, etc. Linux checks for corrupted disks and repairs during startup.

* We can also manually check for filesystem corruption using the command fsck.

Error codes which correspond to the kind of system error.

1 - errors corrected, 2 - system should be rebooted, etc.
### RAID

"Redundant Arrays of Independent Disks" - distributes I/O across multiple disks to achieve increased performance and data redundancy. Prevents against disk failures.

Specialized processing to managed disks.

#### RAID levels

#### RAID 0 (Striping)

* Data is split into blocks, written across all disks present in the array.
* Multiple disks can access the file, resulting in faster read/write speeds.
* First disk not resued until equal amount of data is written to each of the other disks in the array.

```
  0
_____
|	|
|	|
|	|
|	|
1	2
```

* Easily implemented, no bottlenecks, but no redundancy.
* Raid0 can be used for videoaudio editing or gaming environments, non-critical data.

#### RAID 1 (Mirroring)

```
  0
_____
|	|
| = |
|	|
|	|
1	2
```

* Duplicates stack 1 to 2.
* Exact replica.
* Better read performance than Raid0
* Can survive multiple disk failures without need for special data recovery algorithms.
* Costly because storage is half the number of disks due to replication.

Use cases - applications with low downtime but can have a slight hit on write performance.
#### RAID 4 (Striping with dedicated parity)

```
  	  0
_____________
|	|	|	|
|   |	|   |
|	|	|   |
|	|	|   |
1	2	3	4
```

* Block-level stripping
* Dedicated drive used to store parity information
* Generated by an algorithm every time data is written to a disk
* Add checksums into data that can enable the target device to determine whether the data has been recieved correctly.
* Works in parallel, but can survive disk failures.
* Minimum 3 disks required for setup. Needs hardware support. Write speeds are slow.

Uses - operations with really large files.

#### RAID 5 (Striping with distributed parity)

* Similar to Raid4, but parity information is spread across all drives in array.
* Read data transactions are fast as compared to write transactions
* Data remains accessible even after drive failure, storage controller rebuilds data on new drive.

```
  	  0
_____________
|	|	|	p1
|   |	p2  |
|	p3	|   |
p4	|	|   |
1	2	3	4
```

* File storage and application servers, such as email, general storage servers, etc.
#### RAID 6 (Striping with double parity)

* Same as RAID5 but with double p's on each stack for fault tolerance up to 2 drives.
* Office automation, online customer service, and applications that require very high availability.
#### RAID 10 (RAID 1+0 : Mirroring and Striping)

```
  	  0
   _______
  |  	  |
_____   _____
|	|	|	|
|   |	|   |
|	|	|   |
|	|	|   |
1	2	3	4
```

* Transactional databases with sensitive information which require high 
performance and data security.
* Fast
* Good read-write performance, but costly.

#### Commands to monitor RAID

```
cat /proc/mdstat
```
### LVM

LVM stands for Logical Volume Management. In the above section we saw how we can create FS and use individual disks according to our need the traditional way but using LVM we can achieve more flexibility in storage allocation like we can stitch three 2TB disks to make one single partition of 6TB, or we can attach another physical disk of 4TB to the server and add that disk to the logical volume group to make it 10TB in total.
## Archiving and Backup

### Archiving

#### gzip

gunzup
#### tar

> tar program is a tool for archiving files and directories into a single file (often called tarball). This tool is usually used to prepare archives of files before it is transferred to a long term backup server. tar doesn’t replace the existing files and folders but creates a new file with extension .tar . It provides lot of flag to choose from for archiving.

### Backup

* Copying/duplicating existing data at a save point.
* Critical when referred to as a source of truth in the future.
#### Incremental backup

Backup of data since last backup, reduces data storage needs.
#### Differential backup

Backup of changes since last backup, similar to Github pointers.
#### Network backup

Sending out data over the network from source to backup destination - can be centralized or decentralized.

rsync
#### Cloud Backup

Widely used these days, AWS and Azure.
## Introduction to Vim

* Know about this already.
## Bash Scripting

* Use #/bin/bash

### Writing the first bash script

### Taking user input and working with variables

Use, "read"

* https://github.com/pwdelbloomboard/devopstools/practice-scripts/takesureinput.sh
### Exit status

* 0 denotes success

* $? gets the exit status of thelast executed script or command

### Command line arguments and understanding If … else branching

```
if [ $# -ne 1 ];
```

* Passes in an actual argument, being $# and -ne denotes the number of the argument, 1.

* Set variable name to FILE=$1, we can then operate on "$FILE" to check properties of this argument.
* if [ -f "$FILE"]; will check if it is a regular file.
* other flags will check for other statuses.

You just have to be careful about variables and inputs.
### Looping over to do a repeated task

You can for example, monitor a server.

```
#!/bin/bash
#Script to monitor the server

hosts=`cat host_list`

while true
do
    for i in $hosts
    do
        h="$i"
        ping -c 1 -q "$h" &>/dev/null
        if [ $? -eq 0 ]
        then
            echo `date` "server $h alive"
        else
            echo `date` "server $h is dead"
        fi
    done
    sleep 60
done
```

### Conclusion

Understanding package management is a critical part of SRE.
