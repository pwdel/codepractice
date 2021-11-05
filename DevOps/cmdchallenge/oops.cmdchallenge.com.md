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
echo "$(< m*)"
```


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
echo "$(< m*)"
```

This is because the name of the file we were trying to print was, "my-dissertation.txt" (it must have been obvious that a dissertation would be important as opposed to, "anothe file," so the question was asking to print out this specific file).

```
echo "$(< my-dissertation.txt)"
```
### https://oops.cmdchallenge.com/#/oops_print_process

