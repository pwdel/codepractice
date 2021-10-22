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

##### Breakdown

[Pipe |](https://linuxhint.com/linux-pipe-command-examples/)
