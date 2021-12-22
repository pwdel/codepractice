### Source

* [Oops](https://oops.cmdchallenge.com/)

### Setup

### Commands in Order

The premise of this exercise is that /bin and /usr/bin have been deleted, so we only have access to a certain number of commands, basically bash builtins.

* [Bash Builtins](https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html)

* alias
* bind
* builtin
* caller
* command
* declare
* echo
* enable
* help
* let
* local
* mapfile
* printf
* read
* readarray
* source
* type
* typeset
* ulimit
* unalias
#### pwd

> For now, all you need to do is figure out where you are, print the current working directory.

$ pwd

> /var/challenges/oops_cwd
#### https://oops.cmdchallenge.com/#/oops_list_files

> List all of the files on a single line, in the current working directory.
> Hint: You won't be able to use the ls command, instead you will need to use a bash builtin

```
echo *
```

result: 

```
another-file.txt my-dissertation.txt
```


* Explination: the "echo" command is a bash builtin. Doing, "echo *" evidently just uses the greedy search operator.

#### https://oops.cmdchallenge.com/#/oops_print_file_contents

> Oh no! You now remember there is a very important file in this directory. Display its contents before the data is lost for forever!

* Using, "echo" we can start to look in the directory with greedy search:

```
echo *.*

another-file.txt my-dissertation.txt
```

* How do we print out the contents of a file with a bash builtin however?
* there's a, "printf" command built-in.

"printf [-v var] format [arguments]"

```
printf format *.*
```

However this does not appear to work. We can use the same command as in the last step:

```
echo "$(< my-dissertation.txt)"
```

or simply:

```
echo "$(< m*)"
```

This is because the name of the file we were trying to print was, "my-dissertation.txt" (it must have been obvious that a dissertation would be important as opposed to, "anothe file," so the question was asking to print out this specific file).

```
echo "$(< my-dissertation.txt)"
```

* The "$" symbol creates a system memory variable.
* < presumably outputs the contents of whatever is in it into the variable.
* my-dissertation.txt or m* is the file itself.
* Putting everything in quotes creates a string for echo to use.

### https://oops.cmdchallenge.com/#/oops_print_process

> You know there is a process on machine that is deleting files, the first thing you want to do is identify the name of it. Print the name of the process.  Hint: process information is stored in /proc, maybe there is a something there that will help?

```
echo $(</proc/42/cmdline)
```
result:

```
oops-this-will-delete-bin-dirs
```

* Why does /proc/42 specifically and why is /42/cmdline the right location?

* [The Linux Kernal](https://www.kernel.org/doc/html/latest/filesystems/proc.html)
* [1.14. /proc](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/proc.html)

> /proc is very special in that it is also a virtual filesystem. It's sometimes referred to as a process information pseudo-file system. It doesn't contain 'real' files but runtime system information (e.g. system memory, devices mounted, hardware configuration, etc). For this reason it can be regarded as a control and information centre for the kernel. In fact, quite a lot of system utilities are simply calls to files in this directory. For example, 'lsmod' is the same as 'cat /proc/modules' while 'lspci' is a synonym for 'cat /proc/pci'. By altering files located in this directory you can even read/change kernel parameters (sysctl) while the system is running.

> Each of the numbered directories corresponds to an actual process ID. Looking at the process table, you can match processes with the associated process ID. For example, the process table might indicate the following for the secure shell server:

Information from [man5](https://man7.org/linux/man-pages/man5/proc.5.html) tells more about the proc pid subdirectories.

```
       /proc/[pid] subdirectories
              Each one of these subdirectories contains files and
              subdirectories exposing information about the process with
              the corresponding process ID.

              Underneath each of the /proc/[pid] directories, a task
              subdirectory contains subdirectories of the form
              task/[tid], which contain corresponding information about
              each of the threads in the process, where tid is the
              kernel thread ID of the thread.

              The /proc/[pid] subdirectories are visible when iterating
              through /proc with getdents(2) (and thus are visible when
              one uses ls(1) to view the contents of /proc).

       /proc/[tid] subdirectories
              Each one of these subdirectories contains files and
              subdirectories exposing information about the thread with
              the corresponding thread ID.  The contents of these
              directories are the same as the corresponding
              /proc/[pid]/task/[tid] directories.

              The /proc/[tid] subdirectories are not visible when
              iterating through /proc with getdents(2) (and thus are not
              visible when one uses ls(1) to view the contents of
              /proc).
```

Further:

```
       /proc/[pid]/cmdline
              This read-only file holds the complete command line for
              the process, unless the process is a zombie.  In the
              latter case, there is nothing in this file: that is, a
              read on this file will return 0 characters.  The command-
              line arguments appear in this file as a set of strings
              separated by null bytes ('\0'), with a further null byte
              after the last string.

              If, after an execve(2), the process modifies its argv
              strings, those changes will show up here.  This is not the
              same thing as modifying the argv array.

              Furthermore, a process may change the memory location that
              this file refers via prctl(2) operations such as
              PR_SET_MM_ARG_START.

              Think of this file as the command line that the process
              wants you to see.
```

### https://oops.cmdchallenge.com/#/oops_kill_a_process

> You are doing great! You managed to save your important file. Now that you know the process name it will be good to kill it before it does any more damanage. Kill the running process

```
kill 42
```
