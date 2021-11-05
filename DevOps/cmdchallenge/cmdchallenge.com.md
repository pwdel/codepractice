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

```
grep 500 * | cut -d':' -f1 | uniq
```

* First off, "grep 500 *" will quickly filter out lines from every single file that include, "500" in it.  This command would be similar to, "ls | xargs cat | grep 500"
* cut prints selected parts of lines from each FILE to standard output.
* cut -d DELIM uses the specified delimitor DELIM, other than the default tab as a delimiter to seperate parts of the file, so in this case, ':' is the delimitor, with : being the string.
* cut -f1 refers to field 1, basically only selecting this field.
* uniq filters adjacent matching lines from INPUT (or standard input),
writing to OUTPUT (or standard output).

0. So doing an ls, we see that we get multiple different files.

* cat'ing one of those files, you get a lot of lines of data. So how do you actually filter out, "500" from these three files with so much data in it?

```
access.log
access.log.1
access.log.2
```

1. So first, by, "grep 500 *" we grab everything with 500 in it:

```
access.log:69.16.40.148 - - [09/Jan/2017:22:34:33 +0100] "GET /pages/create HTTP/1.0" 500 3471
access.log:225.219.54.140 - - [09/Jan/2017:22:35:30 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 500 2477
access.log.1:2.71.250.27 - - [09/Jan/2017:22:41:26 +0100] "GET /pages/create HTTP/1.0" 500 2477
```
2. Then doing, a cut with delimiter -d ':' on the first field (the access.log) this gives us those filenames again, but this time it's not from the ls function, but rather from delimiting the output of the options from the previous command, and specifically within that first field, f1:

```
access.log
access.log
access.log.1
```

3. Run 'uniq' ... this simply eliminates all repeats. So in the above output, we see that access.log is printed twice. uniq just shows the two unique files.

#### https://cmdchallenge.com/#/search_for_files_by_extension

> Print the relative file paths, one path per line for all filenames that start with "access.log" in the current directory.

Basically a cheat for this is to just do, "ls" because all of the filenames have, "access.log" in the directory.

However if you wanted to be more explicit, you could do: "ls | grep access.log"

#### https://cmdchallenge.com/#/search_for_string_in_files_recursive

> Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log" that contain the string "500".
> Note that there are no files named access.log in the current directory, you will need to search recursively.

Doing, "find . 'access.log'" will show literally everything that has acccess.log in it, recursively:

```
.
./var
./var/log
./var/log/httpd
./var/log/httpd/access.log
./var/log/httpd/access.log.1
./var/log/httpd/access.log.2
find: 'access.log': No such file or directory
```

So, you can grep that out:

```
find . 'access.log' | grep access.log

./var/log/httpd/access.log
./var/log/httpd/access.log.1
./var/log/httpd/access.log.2
```
But now we're faced with three non-unique solutions, yet they are all in the same directory. Also, we have not sorted for, "500" yet:

```
find -name 'access.log' | grep -rh 500
```

* grep -r is --directories=recurse --- look through all directories.

This would print out:

```
access.log:69.16.40.148 - - [09/Jan/2017:22:34:33 +0100] "GET /pages/create HTTP/1.0" 500 3471
access.log:225.219.54.140 - - [09/Jan/2017:22:35:30 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 500 2477
access.log.1:2.71.250.27 - - [09/Jan/2017:22:41:26 +0100] "GET /pages/create HTTP/1.0" 500 2477
```

* grep -h gets rid of the prefixes on the filenames.

So if we do:


```
find -name 'access.log' | grep -rh 404

101.163.230.250 - - [09/Jan/2017:22:52:31 +0100] "DELETE /posts/2/display HTTP/1.0" 404 2477
151.84.119.34 - - [09/Jan/2017:22:47:51 +0100] "GET /posts/1/display HTTP/1.0" 404 3471
12.135.14.52 - - [09/Jan/2017:22:35:28 +0100] "GET /pages/create HTTP/1.0" 404 3471
225.210.137.169 - - [09/Jan/2017:22:57:17 +0100] "POST /posts/foo?appID=xxxx HTTP/1.0" 404 1083

find . 'access.log' | grep -r 404

var/log/httpd/access.log:101.163.230.250 - - [09/Jan/2017:22:52:31 +0100] "DELETE /posts/2/display HTTP/1.0" 404 2477
var/log/httpd/access.log.1:151.84.119.34 - - [09/Jan/2017:22:47:51 +0100] "GET /posts/1/display HTTP/1.0" 404 3471
var/log/httpd/access.log.2:12.135.14.52 - - [09/Jan/2017:22:35:28 +0100] "GET /pages/create HTTP/1.0" 404 3471
var/log/httpd/access.log.2:225.210.137.169 - - [09/Jan/2017:22:57:17 +0100] "POST /posts/foo?appID=xxxx HTTP/1.0" 404 1083

```

Observe that the file directory prefix is still visible without the -h flag.

Hence:

```
find -name 'access.log' | grep -rh 500
```
#### https://cmdchallenge.com/#/extract_ip_addresses

> Extract all IP addresses from files that start with "access.log" printing one IP address per line.

First off, there may be multiple files with a similar name here, so do a greedy search:

```
find . -name 'access.log*'

./var/log/httpd/access.log
./var/log/httpd/access.log.1
```
The * being, "greedy."

If we pipe this output to xargs and cat it, we get a big long print out of lines...

```
find . -name 'access.log*' | xargs cat

163.56.115.58 - - [09/Jan/2017:22:29:57 +0100] "GET /posts/2/display HTTP/1.0" 200 3240
75.113.188.234 - - [09/Jan/2017:22:30:43 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 1116
69.16.40.148 - - [09/Jan/2017:22:34:33 +0100] "GET /pages/create HTTP/1.0" 500 3471
225.219.54.140 - - [09/Jan/2017:22:35:30 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 500 2477
207.243.19.2 - - [09/Jan/2017:22:38:03 +0100] "GET /bar/create HTTP/1.0" 200 1116

...
```
Within that, the first field shows a long list of ip addresses.

```
find . -name 'access.log*' | xargs cat | cut -d '-' -f1

163.56.115.58 
75.113.188.234 
69.16.40.148 
225.219.54.140 
207.243.19.2 
199.37.62.156 
...

```

The interpreter did not exactly accept this answer, so looking at the answer, we see that the space was the delimitor rather than the '-' symbol.

```
find . -name "access.log*" | xargs cat | cut -d " " -f 1
```

#### https://cmdchallenge.com/#/count_files

> Count the number of files in the current working directory. Print the number of files as a single integer.

* the command, "wc" with option, "l" counts the number of new lines.
* If we wanted to generalize this solution, we could do, "ls -F" which grabs all files and directories, and appends a "/" at the end for any that are directories, as well as files, in case there are files and directories that have the same name.
* Doing, "wc -l" would count the number of lines, assuming you filtered out with, "grep -v" which is inverting the match against, "/" or whatever character.

```
ls -F | grep -v / | wc -l
```
However, if we do this, we don't get every single file, perhaps because we didn't search for hidden files.

* If we search with, "ls -R" this gives another entry, ".:" ... 
* "." is used for, "current directory
* ":" is used to seperate host's path from the container's path...source:destination.
* .: seems to mean, "current directory, host:container.

So it appears that the valid answer is:

```
ls -R | wc -l
```

Though it is not clear why this is the valid answer.

#### https://cmdchallenge.com/#/simple_sort

> Print the contents of access.log sorted.

* We can sort using the, "sort" command.
* Since we already know access.log is the filename, we can just do, "ls" and then "sort", understanding that access.log is the only file.
* We could explicitly specify, "sort access.log" since we know the file ahead of time.
* If we just wanted to sort, "any file in the directory" we could do, "sort *"
* If we wanted to filter by files, we could use the above methodology, "ls -F | grep -v / " and then sort the output of all with, "sort *"

```
ls -F | grep -v / | sort *
```
#### https://cmdchallenge.com/#/count_string_in_line

> Print the number of lines in access.log that contain the string "GET".

Again, knowing access.log ahead of time is helpful here, we can simply grep the term, "GET" and then do "wc -l" which counts the newlines remaining out of those filtered for GET.

```
cat access.log | grep GET | wc -l
```
#### https://cmdchallenge.com/#/split_on_a_char

* We can use the, "replace/filter" command, "sed"
* The syntax we use is, "sed [commandstring] [file]"

* The command string uses a flag, of which there are several, and then / as a character to seperate the various things being done according to that command string.

* For example, "s" is used to indicate, "seperate".  Breaking down our command:

* s/;/\n/g

* The, "s" means seperate.
* / character connects the next character
* ; is what we are seperating
* \n is what we are replacing it with (newline)
* /g refers to, "global"

Hence:

```
sed 's/;/\n/g' split-me.txt 
```

#### https://cmdchallenge.com/#/print_number_sequence

> Print the numbers 1 to 100 separated by spaces.

There are a few main ways to do this:

* echo {1..100}

This simply echos a range of integers from 1 to 100.

The above could also be accomplished line by line by counting and echo'ing the $i variable as shown:

```
for i in {1..10}; do echo $i; done
```

This can also be done using the sequence command:

* seq -s ' ' 100
* echo $(seq 1 100)

#### https://cmdchallenge.com/#/replace_text_in_files

* SED is a stream editor and can do lots of functions on files such as: searching, find and replace, insertion, deletion.
* This is commonly a substitute for find or replace.
* You can edit files without opening them.
* Much quicker than using VI/VIM/Nano, etc.

* "sed -i" is used to edit files in place.
* sed -i[SUFFIX] makses a backup if SUFFIX is supplied.
* sed -i 's/old-text/new-text/g' input.txt
* So if we have a file called, "helloworld.txt" with the line, "hi there world" and we want to repalce, "world" with "earth" we do:

```
sed -i 's/world/earth/g' helloworld.txt
```

So in this situation, we have several txt files and directories, so we need some kind of greedy, recusrive match.

> The wildcard * matches any file or directory (whose name doesn't start with .) in the current directory.
> ** may be equivalent to *; it could match zero or more characters followed by zero or more characters, which is the same as matching zero or more characters just once.
> But with some shells, with some settings, ** is a recursive version of *, matching all files and directories in the current directory and subdirectories.

So if we create another file, "fine.txt" and enter the line, "fine how are you" and then do a cat with that recursive wildcard, we get:

```
# cat *
oh hello how are you
hi there earth
```
Where basically we're cat'ing out every file in the entire directory. Similarly if we use, "cat *txt"

Hence, if we want to look in subdirectories, we can start out by making a subdirectory, test/ with a file, "ok.txt" in which we enter the line, "cool dude" - thereby allowing the command cat **/*txt to spit out the contents of anything within subdirectories and ending with txt.

```
cat **/*txt
cool dude
```

hence:

```
sed -i  's/challenges are difficult//g' **/*.txt
```
Will take anything with the expression, "challenges are difficult" and just eliminate it from any of the files in the subdirectories under the main folder.

#### https://cmdchallenge.com/#/sum_all_numbers

> The file sum-me.txt has a list of numbers, one per line. Print the sum of these numbers.



Hence:

```
awk '{n=n+$0}END{print n}' sum-me.txt
```

##### Breakdown

[Pipe |](https://linuxhint.com/linux-pipe-command-examples/)

