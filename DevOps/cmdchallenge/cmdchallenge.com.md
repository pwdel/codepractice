#### https://cmdchallenge.com/#/hello_world

$ echo hello\ world

#### https://cmdchallenge.com/#/print_file_contents

> There is a file named access.log in the current directory. Print the contents.

$ cat access.log

#### https://cmdchallenge.com/#/last_lines

> print the last 5 lines of that previous file

$ tail -n 5 access.log

#### https://cmdchallenge.com/#/create_file

> Create an empty file named take-the-command-challenge in the current working directory.

$ touch take-the-command-challenge

#### https://cmdchallenge.com/#/create_directory

> Create a directory named tmp/files in the current working directory

* sol: use the p flag:

$ mkdir -p tmp/files

#### https://cmdchallenge.com/#/copy_file

> Copy the file named take-the-command-challenge to the directory tmp/files

$ cp take-the-command-challenge tmp/files

#### https://cmdchallenge.com/#/move_file

> Move the file named take-the-command-challenge to the directory tmp/files

$ mv take-the-command-challenge tmp/files

#### https://cmdchallenge.com/#/create_symlink

> Create a symbolic link named take-the-command-challenge that points to the file tmp/files/take-the-command-challenge.

* note: format is $ ln -s DESTINATION NAME

$ ln -s tmp/files/take-the-command-challenge take-the-command-challenge

#### https://cmdchallenge.com/#/delete_files

> Delete all of the files in this challenge directory including all subdirectories and their contents.

* note - the * symbol indicates greedy, similar to regex. .* would mean

$ rm * .* -rf

#### https://cmdchallenge.com/#/remove_files_with_extension

> There are files in this challenge with different file extensions. Remove all files with the .doc extension recursively in the current working directory.

$ find | grep ".doc" | xargs rm

* [xargs](https://en.wikipedia.org/wiki/Xargs) stands for, "extended arguments."
* Commands such as grep or awk can take input either as command line arguments from the standard input.
* So when you do, < find | grep ".doc" > above, this is going to [grep](https://en.wikipedia.org/wiki/Grep) (match a regular expression) with [find](https://en.wikipedia.org/wiki/Find_(Unix)) (which locates files as an ouput), using ".doc" as the regex, meaning the stdin output of each line will show those filenames.
* the [pipe](https://en.wikipedia.org/wiki/Vertical_bar#Pipe) simply directs the output of one line of commands to the next line, it's like connecting line after line of bash commands together.
* So "xargs" is basically the output on stdin, line by line, each as its own argument.
* Therefore when we do, "xargs rm" we're just repeating that command on each argument, one after another.

#### https://cmdchallenge.com/#/find_string_in_a_file

> There is a file named access.log in the current working directory. Print all lines in this file that contains the string "GET".

$ cat access.log | grep "GET"

#### https://cmdchallenge.com/#/search_for_files_containing_string

> Print all files in the current directory, one per line (not the path, just the filename) that contain the string "500".

* First off, "grep 500 *" will quickly filter out lines from every single file that include, "500" in it.  This command would be similar to, "ls | xargs cat | grep 500"
*

ls |xargs -I _  grep -l 500 _

grep 500 * | cut -d':' -f1 | uniq


##### Breakdown

[Pipe |](https://linuxhint.com/linux-pipe-command-examples/)
