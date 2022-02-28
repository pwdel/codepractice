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

### Checking the Shell Script with Shellcheck



### Making the Shell Script Executable

```
chmod +x codeperform.sh
```
