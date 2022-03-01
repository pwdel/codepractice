# Codeperform Project

The purpose of this project is to build a simple code performance measuring tool which includes an output that captures the relative time of execution of two different programs, ideally of similar output and purpose, to understand on a minute scale which execution path is faster.

The idea here is to create a benchmark which helps determine what type of program runs faster on a particular machine. Part of the impetus for this project is just basic computer language benchmarks, such as the [Computer Language Benchmarks Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/index.html).

Often times in benchmarking we may think of in terms of performance benchmarks which roughly compare two different languages across multiple different benchmark algorithms, such as [fannkuck-redux](https://benchmarksgame-team.pages.debian.net/benchmarksgame/description/fannkuchredux.html#fannkuchredux), and may compare two or more different languages against each other, such as [C++ and Rust](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/gpp-rust.html).

Well, what if you wanted just a quick tool to compare two little quick programs that you built yourself?

# Existing Tools

Of course it's always temping to think that one is the first one to have thought of an idea, but that is almost never the case.

### Built-in Timer Tools

Most languages likely have built-in timing functions. If you look at the built in [time](https://docs.python.org/3/library/time.html) module in Python, then you’ll notice several functions that can measure time:

* monotonic()
* perf_counter()
* process_time()
* time()

These types of programs can measure time within the interpretive language itself, but what about just a simple shell script which can measure the relative time of any program, regardless of the language it was written in?

# Rough Outline

* The command line tool, "strace" can be used to monitor application performance throughout the execution of a program.

The pseudocode version of what we wish to build would be the following:

```
# start program

# input files should have been inputs to the shell program

# run the first program using strace

# A do an awk or sed on the output on the first line to grab the timestamp

# B do an awk or sed on the output on the first line to grab the timestamp

# subtract the last_timestamp from the first_timestamp

# run the second porgram using strace

# repeat A and B above on the second program

# output metrics between the two programs

```

## Working through the Bash Script

### Creating the File, Initiating with #! Shebang Operator

* We can implement the above as a bash script by creating a file, "codeperform.sh," and adding the shebang "#!/bin/bash/" operator at the very start of the file to indicate that this script is going to run as bash (as opposed to zshell or /bin/sh).

Of course, this is easier said than done, as an absolute path is needed specifying from the root directory of a linux or unix based system, meaning that we can't just put, "#!/bin/bash" we have to put either:

```
#!/usr/bin/env bash
```
...which has the benefit of looking for whatever the default version of the program is running in your current environment, whereas: 

```
#!/usr/bin/bash
```
would be useful if it was a one-line command in which more than one argument needed to be passed in at the onset, with a command such as:

```
/user/bin/env awk -f
```
So basically, the form, "#!/usr/bin/env bash" is more portable, but has limitations in terms of what executables are called.

### Adding Arguments to the Bash Script

Bash uses a tool called, "positional parameters," to provide a means of etnering data into a Bash program when it is run from the command line. There are ten possible positional parameters that run from $0 to $9.

After entering in a simple positional parameter, "echo $0" (and making the script executable by applying chmod +x filename.sh), we run the script with no parameters to start off with:

```
$ ./codeperform.sh 1
./codeperform.sh
```
Basically, the $0 position is reserved for the predefined name of the running script and can't be used for anything else.  So instead starting with $1 as the positional parameter, and using two parameters to start off with:

```
$ ./codeperform.sh -h -f
-h
```

As you can see, the flag -h just repeats and the second parameter, -f does nothing because we only have one parameter input at this point.  If the code instead used two parameters and we inserted those paremters, we would get the actual output of both parameters as shown below:

```
#!/usr/bin/env bash
echo $1
echo $2
```
and then:
```
$ ./codeperform.sh -h -f
-h
-f
```

### Creating a Help Function

It's a best practice to always include a help function within a shell script.  Something to note about running functions on bash is that functions can be essentially inserted into memory as a variable enclosed within the {} brackets just like a variable.  Whereas a variable declaration may be something along the lines of:

```
EXAMPLE_VARIABLE=2
...
echo $EXAMPLE_VARIABLE
2
```
Which would store the EXAMPLE_VARIABLE, equaling 2 into memory for super fast access, the same can be done with a function itself using:

```
help(){ echo "This is the unhelpful help file. Goodbye."; }
```

Just as you could use, "printenv" to print all variables in an environment, you can do the same for functions with, "compgen -A function" and of course filter out the result with grep:

```
compgen -A function | grep help
help
```

Running the -help file itself would be just a matter adding the help function into the script, and then calling in the, "main" part of the script.

```
#!/usr/bin/env bash
# -------------------- help --------------------
help(){ echo "This is the unhelpful help file. Goodbye.";}

# -------------------- main --------------------
help
```

This will of course run the help file as a default rather than as an option flag.

### Turning Help into a Flag Rather than a Default

The help flag, as well as other flags, is accomplished with a while loop including different cases within the main part of the program.

```
# -------------------- main --------------------

while getopts ":h" option; do
   case $option in
      h) # display Help
         help
         exit;;
      *) # invalid cases
         echo 'Invalid option. Find options with flag: -h'
         exit;;
   esac
done
```
By including -h as a flag within the function, this access the help function, which prints out that help file we created above.

### Running strace on One Program

We have created a simple c program called, "hello.c" which essentially does the following:

```
#include <stdio.h>
int
main(int argc, char *argv[])
{
  printf("hi!\n");
  return 0;
}
```
We compile this into an executable called, "whatever" using the command, "gcc hello.c" and then we can run the outputted file (after changing its name) with 

```
./whatever
```
Basically all the program does is say, "hi."

So now if we want to run strace on this, a linux box is required.  Attempting to use this on MacOS fails, as attempting to isntall with brew results in:

```
strace: Linux is required for this software.
linux-headers@4.4: Linux is required for this software.
Error: strace: Unsatisfied requirements failed this build
```

So, we can simply set up a lightweight ubuntu docker distro and mount the shell script we are writing here as a volume (or rather, as a bind mount on our local machine so that as we change the code, we can keep re-running it, but it also saves locally in our github repo).

A perhaps more easily recognizeable name for this type of setup is a, "dev mode container."

In order to set up a dev mode container, we first have to establish a folder structure under which we can hold a Dockerfile and our application files, so that we can point to the source code to copy into the Image which will be the basis for the container. Secondly we set up a run command which bind mounts the appropriate folder which contains our code so that we can access and edit it within the running container.

So first off, our folder structure will look like the following:

```
project
│   codeperform.md
│   Dockerfile
│
└───app
    │
    └───codeperform.sh
    |___otherfiles.files
```
Basically, "/app" is where we we keep everything that needs to be, "bind mounted," meaning, we can change the files on our disk and it will reflect on the container, and vice-versa.

The Dockerfile itself, in order to copy the file from the local machine into the Docker Image during the build process, must include a, "COPY" clause, as follows:

```
# syntax=docker/dockerfile:1
FROM ubuntu:latest

# copy the local app file into the image
COPY app /usr/destination
```

So, "app" is the source file, whereas "/usr/destination" is the destination file. Of course without opening a container directory structure first, it's impossible to know what the best place to put these files might be on the destination Docker Image, so a good practice would be to simply build and run the image with an, "exec" funtion to essentially log in, or rather, exec in to the container to explore and find the right place first. From within the same directory as the Dockerfile:

```
docker build -t codeperform_ubuntu_image:latest .
docker run  -t -d --name codeperform_ubuntu_container codeperform_ubuntu_image
docker exec -t -i codeperform_ubuntu_container /bin/bash
```

From here we see that the directory structure is:

```
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

...and "home" seems like a good place, so we can copy our files to, "home/app" by modifying the Dockerfile:

```
# copy files from local directory
COPY app /home/app
```

After deleting the running Docker Container, running through the above commands again puts the files we need in, "home/app".

The Dockerfile defines how an image is built, not how it's used, so you can't specify the bind mount in a Dockerfile. We could create a declarative specification for including the Dockerfile in question, and including a bind mount or volume, allowing us to simply run, "docker-compose up -d" rather than a complex Docker command line, by including a docker-compose.yml file with the following:

```
version: '3.1'

services:
  codeperform_ubuntu_container:
    image: codeperform_ubuntu_image:latest
    build: .
    volumes:
      - type: bind
        source: ./app
        target: /home/app
```

We can run the above by navigating into the folder where this docker-compose.yml file sits and then running, "docker-compose up -d" - which follows the commands shown above and then runs the container, mounting the volume with at the specified directory noted as a cannonical path ending with the ./app folder (with the ./ included to indicate a relative path), and connecting that to /home/app on the container.

Of course, when we run, "docker-compose up -d" or "docker-compose up" the container exits after the process has completed.

If we look at the verbose version of this command, we get some feedback:

```
docker-compose --verbose up

...

 'Config': {'AttachStderr': False,
            'AttachStdin': False,
            'AttachStdout': False,
            'Cmd': ['bin/bash'],
            'Domainname': '',
            'Entrypoint': None,

...
```
Basically, there was a 'Cmd' being issued to use bin/bash, but no terminal, so trying to use bash without a terminal makes the container exit immediately. When bash starts up with no terminal attached, it has no script or command to by design, it exits.

In order to attach the terminal, we use tty: true.  We can also add, "command: 'bin/bash'" for good measure to be explicit to our docker-compose.yml:

```
    tty: true
    command: 'bin/bash'
```

After this was fixed successfully, we can run the following to get everything up and going:

```
docker-compose up -d
docker exec -t -i codeperform_ubuntu_container /bin/bash
```

This will compose the entire image, build it if not already built, and then exec into the container with bash.

Side note, we could have added a command or entrypoint to the Dockerfile itself rather than the compose file.  These commands would basically tell the image by default to run an entrypoint or to bash any time the image runs. If we make any changes to the Dockerfile, we may need to re-build the image with, "docker-compose up --build" e.g., using the --build option.

### Ensuring that Changes in the Container Reflect in the Code on Local

So the reason we have set up this fancy Dev Mode Container is to be able to make changes within our Container and have them save on our local so that we can push to Github, essentially to be able to save our work.

So to run a simple test, we can do the following from within the container:

```
/home/app# echo 'hello worlds' >> hellotest.txt
```
Which we can see saves a file on our local.  Removing this file also removes it on local.

### Checking the Shell Script with strace

So now we have a working Ubuntu container, so we should be able to install strace.  Once we have figured out how to install it manually within the container, we can go back and re-compose the container with "docker-compose build up -d".

So we can start out by running:

```
# apt-get update

...

# apt-get install strace

...

# strace -V
strace -- version 5.5
Copyright (c) 1991-2020 The strace developers <https://strace.io>.
```
When we opt to add this into our Dockerfile, we can opt in if we so choose to explicitly install strace 5.5 for compatibility purposes.

### Testing out Strace on Code

So having installed strace, we can install our, "whatever" pre-compiled C code on our new Ubuntu container.

```
strace -ttT ./whatever
19:26:11.555004 execve("./whatever", ["./whatever"], 0x7ffc856beb38 /* 9 vars */) = -1 ENOEXEC (Exec format error) <0.004814>
strace: exec: Exec format error
19:26:11.563988 +++ exited with 1 +++
```

However when we try to do this, we get the above error. This is because originally the file was compiled on a Mac with OSX rather than on a linux system, without a cross-compiler. There is a way to compile code such that it works across systems with the, "binutils" library and gcc and a string of commands. However since we have the Ubuntu container up and running, we can simply re-compile on Ubuntu with Gnu Compiler Collection.

```
apt-get update
...
apt-get install build-essential
...
gcc --version
gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
Copyright (C) 2019 Free Software Foundation, Inc.
```

GNU Compiler Collection (GCC)

We can now overwrite our, "whatever" file by using gcc and hello.c:

```
gcc hello.c -o whatever
```
Now having compiled the file properly according to Ubuntu's binary requirements, we can run, "./whatever" which just prints out, "hi!" - so we can then use strace:

```
strace -ttT ./whatever
19:34:22.804636 execve("./whatever", ["./whatever"], 0x7ffe65523658 /* 9 vars */) = 0 <0.001316>
...
```
Which does print out a timestamped output, one line of which is shown above.

### Using Strace and Awk to Output

Looking at, "strace -h" we can see that we also have the option of printing out just statistics with the -c flag:

```
strace -c ./whatever
hi!
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
 28.72    0.000407         407         1           execve
 20.54    0.000291          41         7           mmap
 12.00    0.000170          85         2         1 arch_prctl
  8.33    0.000118          19         6           pread64
  7.76    0.000110          36         3           brk
  6.49    0.000092          46         2           openat
  6.07    0.000086          43         2           close
  2.96    0.000042          42         1           munmap
  2.61    0.000037          12         3           mprotect
  1.69    0.000024           8         3           fstat
  1.13    0.000016          16         1         1 access
  0.99    0.000014          14         1           write
  0.71    0.000010          10         1           read
------ ----------- ----------- --------- --------- ----------------
100.00    0.001417                    33         2 total
```

Note that the total calculated seconds is shown at the bottom of, "seconds," with 0.001417 seconds to be precise, which may be a much easier piece of data to grab than actually subtracting and calculating the time to execute. Sure enough, with the right command we can directly extract that value onto the stdout:

```
strace -c ./whatever 2>&1 >/dev/null | awk 'END{print $2}'
0.001196
```
Note that the timed value, 0.001196 is different than 0.001417. Through the process of building the above command, it was obvious that each time strace was run, the timed value for the command was different. This makes sense because the load on the machine is constantly changing depending upon the processor's capability. Instead of a final value, we might wish to consider an average value after a certain number of executions. But - we'll ignore that for now.

### Turning the Strace Command into a Function and Output in our Shell Script


### Checking the Shell Script with Shellcheck


### Making the Shell Script Executable

```
chmod +x codeperform.sh
```
