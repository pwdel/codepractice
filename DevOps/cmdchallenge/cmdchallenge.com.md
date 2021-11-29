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

* [Using Awk - Geeks for Geeks](https://www.geeksforgeeks.org/awk-command-unixlinux-examples/)

What we can do with AWK:

* Scan files line by line.
* Splits each input line into fields.
* Compare input line/fields to a pattern.
* Perform actions on matched lines.

This is useful for:

* Transforming data files
* Producing formatted reports

Includes programming constructs:

* Formatting output lines
* Arithmetic and string operations
* Conditionals and loops

So if we start off by looking at the file:

```
cat sum-me.txt
1
2
3
5
7
11
13
```
It's exactly as described, one number per line.

The default behavior of awk is simply to just print every line, the same as cat would.

```
awk '{print}' sum-me.txt
1
2
3
5
7
11
13
```
...an equivalent command would be to print out the, "first row," of whatever is within the file, or:

"awk '{print $1}' sum-me.txt" which basically uses $1 to specify the first tab delimited row.

We can also count the number of lines in the file with:

```
awk 'END {print NR}' sum-me.txt
7
```
Given that we know the number of lines is 7, and not a, "general number of lines" we can do a for loop and hold a variable, "sum" and continue printing out the cumulative sum on each line as we move to each line, denoted by $1 (the column number).

```
awk 'BEGIN{sum=0} {sum=sum+$1} {print sum}' sum-me.txt
1
3
6
11
18
29
42
```
And if we want just the result at the end, without printing this out on every line, we add, "END" --
```
awk 'BEGIN{sum=0} {sum=sum+$1} END{print sum}' sum-me.txt
42
```
#### https://cmdchallenge.com/#/just_the_files

> Print all files in the current directory recursively without the leading directory path.

First off, if we list recursively, we get everything:

```
ls -R
.:
2038
beatae.flac
error.doc
libero.xls
necessitatibus.doc
totam
./2038:
01
./2038/01:
19
./2038/01/19:
animi.doc
corporis.xls
odit.doc

```
Howeever, we have to know apriori which one is a filename and which one is a directory prior to executing this code.

If we do the following, then we get a list of files with leading directory structures:

```
find -type f
./2038/01/19/animi.doc
./2038/01/19/corporis.xls
./2038/01/19/odit.doc
./beatae.flac
./error.doc
./libero.xls
./necessitatibus.doc
./totam
```
To take those out, we need to filter with, printf '%f\n'

* %f -> format specifier, removes floating point numbers
* \n -> special characters, newline/linefeed

```
find -type f | -printf '%f\n'
```
However, this only works without the pipe, which I don't understand why that would be.  Looking at a more understandable command:

```
find -type f | sed 's/.*\///'
```

* the, 'text to replace' is .*\/ which is basically, "anything" between . and including the character "/", which we are using the escape character \ to specify.
* Then we're replacing it with, "" which is nothing, as specified between the next / and /.

#### https://cmdchallenge.com/#/remove_extensions_from_files

> Rename all files removing the extension from them in the current directory recursively.

So first we can list off everything in the folder:

```
ls -R
.:
2038
beatae.flac
error.doc
libero.xls
necessitatibus.doc
totam
./2038:
01
./2038/01:
19
./2038/01/19:
animi.doc
corporis.xls
odit.doc
```
Then just the files:

```
find -type f
./2038/01/19/animi.doc
./2038/01/19/corporis.xls
./2038/01/19/odit.doc
./beatae.flac
./error.doc
./libero.xls
./necessitatibus.doc
./totam
```
Then we can pipe those results into a, "sed" and replace the extension of each file.

```
find -type f | sed 's/*.//'
```
However what the above does is just eliminates everything.

```
find -type f | sed 's/\..*//'
```
Working with different permutations of sed, we get the same result, where the entire file is eliminated.

Note...there is a specific command, "rename" which can be used with a filtering function to rename all files recursively.

```
rename 's/\..*//' **/*
```
* 's/.../' is the overall string
* **/* means, "within this directory, recursively.
* the \. is an escape character which looks for .
* .* tells us to do greedy search on anything after the .
* // <- shows to replace that end extension with nothing

### https://cmdchallenge.com/#/replace_spaces_in_filenames

> The files in this challenge contain spaces. List all of the files (filenames only) in the current directory but replace all spaces with a '.' character.

If we try the following with a regex:

```
rename 's/ /./' **/* 
```
We see that the search **/* finds nothing.

Using the command, "tr" we can do something a bit easier. "tr" is simply, translate or delete characters.

```
ls | tr ' ' '.'
```

### https://cmdchallenge.com/#/dirs_containing_files_with_extension

> In this challenge there are some directories containing files with different extensions. Print all directories, one per line without duplicates that contain one or more files with a ".tf" extension.

So first off, doing an, "ls" shows that there are two directories, so doing an ls -R:

```
.:
bin
terraform
./bin:
dostuff.sh
./terraform:
main.tf
modules
./terraform/modules:
load_balancer
virtual_machine
vpn
./terraform/modules/load_balancer:
main.tf
./terraform/modules/virtual_machine:
main.tf
outputs.tf
./terraform/modules/vpn:
files
main.tf
templates
./terraform/modules/vpn/files:
bootstrap.sh
./terraform/modules/vpn/templates:
config.template
```
In order to look at the end extension, we could do a sed.

```

ls -R | sed 's/.tf//' 
```
This does take the tf off of all of the files with the tf extension, but it also shows all of our other outputs:

```
.:
bin
terraform
./bin:
dostuff.sh
./terraform:
main
modules
./terraform/modules:
load_balancer
virtual_machine
vpn
./terraform/modules/load_balancer:
main
./terraform/modules/virtual_machine:
main
outputs
./terraform/modules/vpn:
files
main
templates
./terraform/modules/vpn/files:
bootstrap.sh
./terraform/modules/vpn/templates:
config.template
```
* Somehow we have to identify the files which have .tf within the extension before passing onto the next step.

So if we do:

```
ls -R | grep tf
main.tf
main.tf
main.tf
outputs.tf
main.tf
```
So passing this output to sed:

```
ls -R | grep tf | sed 's/.tf//'

main
main
main
outputs
main
```
However, we are also asked to disclude duplicates.

```
ls -R | grep tf | sed 's/.tf//' | sort -u
main
outputs
```
Note that the specification was asking for *directories which contain* the file with the specified extension, not the actual file extension. Hence we need to use a recursive search with, "dirname" and **/* and pipe that result to uniq (or sort -u)

```
dirname **/*tf | uniq

terraform
terraform/modules/load_balancer
terraform/modules/virtual_machine
terraform/modules/vpn
```

### https://cmdchallenge.com/#/files_starting_with_a_number

> There are a mix of files in this directory that start with letters and numbers. Print the filenames (just the filenames) of all files that start with a number recursively in the current directory.

* First off, we're looking for the "current directory," which means using "ls" rather than, "ls -R"
* We're searching for alphanumerics, so we can use a regex and [0-9]
* We're starting at the start of the string, so we can use an anchor match ^

```
ls | grep ^[0-9]

001dir
04Carrie Alexander
132Rebecca Rubio
25Brandon Mcdonald
293Linda Bennett
335John Joseph
388Andrew Carter
402Nancy Henson
42Robert Hill
436Teresa Owens
477Thomas Pierce MD
48Thomas Allen
511Tammy Welch
540Katherine Jones
593Brett Martin
639Charles Ferguson
670James Jacobs
682Terri Jones
737Jeffrey Davis
757Robert Marquez
778Holly Archer
78Michelle Spencer
974Michael Bowman
```
* In the above result, we can see that 001dir is included, which is actually a directory, whereas we are looking for the files.

There are many ways of filtering for just files, but one method is perhaps the most elegantly typed:

```
ls -p | grep -v /
```
So we could take that and add on our previous grep to filter further by number.

```
ls -p | grep -v / | grep ^[0-9]
04Carrie Alexander
132Rebecca Rubio
25Brandon Mcdonald
293Linda Bennett
335John Joseph
388Andrew Carter
402Nancy Henson
42Robert Hill
436Teresa Owens
477Thomas Pierce MD
48Thomas Allen
511Tammy Welch
540Katherine Jones
593Brett Martin
639Charles Ferguson
670James Jacobs
682Terri Jones
737Jeffrey Davis
757Robert Marquez
778Holly Archer
78Michelle Spencer
974Michael Bowman
```
However, this leaves out a few files. Instead running file with a grep of the 0-9 regex, we get:

```
find -type f -printf "%f\n" | grep ^[0-9]

```

* Running, "find -type f" will find the filenames and print everything out, including the ./ directory structure. There are multiple different options in place of, "f" which are possible including directories, links, sockets, etc.
* -printf is an option of find, "print formatted" which has its own set of options, including %f
* %f indicates any leading directories removed, the "./" stuff
* \n is newline

#### https://cmdchallenge.com/#/print_nth_line

> Print the 25th line of the file faces.txt

* sed is sort of like cat, sed being a stream editor and cat being a concatenator, we're treating the file like a stream.
* -n means silent for sed
* -e shows an expression or script to be taken in, with the next argument being said expression
* 25p means, "print the current pattern space, 25" which indicates the number of lines. [from this detailed documentation](https://man7.org/linux/man-pages/man1/sed.1.html)

```
sed -n -e 25p faces.txt
```

#### https://cmdchallenge.com/#/reverse_readme

> Print the lines of the file reverse-me.txt in this directory in reverse line order so that the last line is printed first and the first line is printed last.

Using sed, we might have something along the lines of:

```
sed -n -e r reverse-me.txt
```
However, "r" is not an option for -e.

There's a cleverly named, "tac" command which is, "cat in reverse."  So, we can simply cat the file, and then pipe it to tac.

```
cat reverse-me.txt | tac
```
#### https://cmdchallenge.com/#/remove_duplicate_lines

> Print the file faces.txt, but only print the first instance of each duplicate line, even if the duplicates don't appear next to each other. Note that order matters so don't sort the lines before removing duplicates.

It's fairly clear that we should use awk on this challenge. For detailed documentation we look [here](https://man7.org/linux/man-pages/man1/awk.1p.html).

* sed is a stream editor, it works on streams of characters on a per-line basis and includes a primitive programming language that includes loops and conditionals. There are only, "two variables," the pattern space and the hold space. Script readibility is tougher, math operations are awkward.
* awk is oriented towards fields on a line-by-line basis, it has much more robust programming constructs including if/else, while, do/while, and for for C-style array iteration. There is complete support for variables and single-dimension arrays. Math operations resemble C. There are other variations of awk including mawk and nawk.
* sed is used for patterns in text, it's kind of more of a regex thing.
* awk is used for the text that looks more like rows and columns.

In this instance, the faces are in rows, so awk is probably the best approach.

* Awk, being more of a programming language, is the one with BEGIN and END and puts commands in between {}.
* Awk also uses the $1, $2, fields to look at columns, with the -F field seperator option.

Finding duplicates:

```
awk 'c[$0]++; c[$0]==2' faces.txt
```
This prints out uniqe lines, line by line. How?

* c is a variable, we iterate it with ++
* we're using column 0, [$0]
* if we count at least c==2, then print it out, filter it out

So if we run this into unique:

```
awk 'c[$0]++; c[$0]==2' faces.txt | uniq
(◕‿◕)
٩◔̯◔۶
(¬_¬)
¯\_(ツ)_/¯
ヽ༼ຈل͜ຈ༽ﾉ
(︺︹︺)
```
But this is not the right answer. There is a simplier implementation:

```
awk '!c[$0]++' faces.txt
(◕‿◕)
(^̮^)
ʘ‿ʘ
ಠ_ಠ
ಠ⌣ಠ
ಠ‿ಠ
(ʘ‿ʘ)
(ಠ_ಠ)
¯\_(ツ)_/¯
(ಠ⌣ಠ
ಠಠ⌣ಠ)
```
Note that ! prior to the c.


#### https://cmdchallenge.com/#/find_primes

> The file random-numbers.txt contains a list of 100 random integers. Print the number of unique prime numbers contained in the file.

We can print out the number of unique numbers with:

```
cat random-numbers.txt | sort -u | wc -l
```
Of course, this is not the number of primes. While we can't put together a formula to discover primes, we can put together a formula to evaluate whether a number is a prime, below a particular value. So first off we could find the maximum within that above output.

```
cat random-numbers.txt | sort -u | sort -n

32119
```
The highest number then is, "32119" - so we could find the primes below this number. Of course the list is of fixed length as well, so knowing that number may not even be valuable.

It turns out that there is a command, "factor" which factors out numbers:

```
factor 20
2 2 5
```
So starting out with our sort -u command:

```
sort -u *

...

```
Gives us all of the unique numbers, sorted by the first digits.

Factoring these gives us:

```
sort -u * | factor

10148: 2 2 43 59
10403: 101 103
1053: 3 3 3 3 13
10546: 2 5273
10596: 2 2 3 883
10969: 7 1567
11744: 2 2 2 2 2 367

...

```
So if there is more than one factor result, it's not a prime for example, the prime, "31667: 31667" shows only itself as a factor.

Hence, if we can use awk to filter out any result that has more than one factor shown, these will be the primes:

```
sort -u *|factor|awk 'NF==2'

12379: 12379
14411: 14411
20897: 20897
21397: 21397
24533: 24533
24631: 24631
25537: 25537
30197: 30197
31667: 31667
32119: 32119
3697: 3697
7103: 7103

```
So to count these up, just add, "wc -l"

#### https://cmdchallenge.com/#/print_common_lines

> access.log.1 and access.log.2 are http server logs. Print the IP addresses common to both files, one per line.

Taking a look at the files:

```
cat access.log.1

108.68.174.15 - - [09/Jan/2017:22:32:19 +0100] "GET /foo/create HTTP/1.0" 200 2477
17.2.20.139 - - [09/Jan/2017:22:33:48 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 2477
28.151.137.59 - - [09/Jan/2017:22:37:57 +0100] "GET /foo/create HTTP/1.0" 200 1116
199.150.241.179 - - [09/Jan/2017:22:38:34 +0100] "GET /bar/create HTTP/1.0" 200 3240
2.71.250.27 - - [09/Jan/2017:22:41:26 +0100] "GET /pages/create HTTP/1.0" 500 2477
17.137.186.194 - - [09/Jan/2017:22:43:17 +0100] "GET /pages/create HTTP/1.0" 200 1116
151.84.119.34 - - [09/Jan/2017:22:47:51 +0100] "GET /posts/1/display HTTP/1.0" 404 3471
4.180.204.195 - - [09/Jan/2017:22:49:53 +0100] "GET /foo/create HTTP/1.0" 502 1116
9.230.96.54 - - [09/Jan/2017:22:52:58 +0100] "GET /bar/create HTTP/1.0" 200 1116
157.143.233.21 - - [09/Jan/2017:22:53:50 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 502 1083

cat access.log.2

89.148.148.238 - - [09/Jan/2017:22:33:09 +0100] "GET /posts/1/display HTTP/1.0" 502 2477
12.135.14.52 - - [09/Jan/2017:22:35:28 +0100] "GET /pages/create HTTP/1.0" 404 3471
81.196.171.245 - - [09/Jan/2017:22:37:53 +0100] "GET /posts/2/display HTTP/1.0" 200 2497
202.141.16.141 - - [09/Jan/2017:22:42:48 +0100] "GET /pages/create HTTP/1.0" 200 2477
132.202.73.71 - - [09/Jan/2017:22:45:23 +0100] "PUT /posts/foo?appID=xxxx HTTP/1.0" 200 2497
89.169.186.129 - - [09/Jan/2017:22:49:29 +0100] "POST /pages/create HTTP/1.0" 200 1116
17.137.186.194 - - [09/Jan/2017:22:53:54 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 3471
2.71.250.27 - - [09/Jan/2017:22:57:17 +0100] "POST /posts/foo?appID=xxxx HTTP/1.0" 404 1083
28.151.137.59 - - [09/Jan/2017:23:00:50 +0100] "GET /foo/create HTTP/1.0" 502 3471
108.68.174.15 - - [09/Jan/2017:23:03:35 +0100] "GET /posts/1/display HTTP/1.0" 200 2497

```
* So first off, this is tabular formatted data, so the first instinct is to use awk.

If you want to treat the contents of both files as one, you use the * marker, like so:

```
cat access.log.*
```
So with awk, you can run the command on the filespace, "access.log.*"

```
awk 's[$1]++{print $1}' a*
17.137.186.194
2.71.250.27
28.151.137.59
108.68.174.15
```
* the s variable operates on column 1, iterating and printing anything new on row $1.

#### https://cmdchallenge.com/#/print_line_before

> Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log", where the next line contains the string "404". Note that you will need to search recursively.

First, taking a recursive look at our file structure:

```
ls -R

.:
var
./var:
log
./var/log:
httpd
./var/log/httpd:
access.log
access.log.1
access.log.2
```

* Once again, awk is a programming language.

The following prints out everything from the file structure which matches the term /access.log and any pattern afterward.

```
awk '{print f}' **/access.log*
```
So if we add, f=$0, this will print out the entire line.

```
awk '{print f}{f=$0}' **/a*
...
163.56.115.58 - - [09/Jan/2017:22:29:57 +0100] "GET /posts/2/display HTTP/1.0" 200 3240
75.113.188.234 - - [09/Jan/2017:22:30:43 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 200 1116
69.16.40.148 - - [09/Jan/2017:22:34:33 +0100] "GET /pages/create HTTP/1.0" 500 3471
225.219.54.140 - - [09/Jan/2017:22:35:30 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 500 2477
```
Whereas {f=1} would print out the first column, with the ip addresses.

We can operate across the entire line on everything that has a 200 on the next line, with:

```
awk '/200/{print f}{f=$0}' **/access.log*
163.56.115.58 - - [09/Jan/2017:22:29:57 +0100] "GET /posts/2/display HTTP/1.0" 200 3240
225.219.54.140 - - [09/Jan/2017:22:35:30 +0100] "GET /posts/foo?appID=xxxx HTTP/1.0" 500 2477
207.243.19.2 - - [09/Jan/2017:22:38:03 +0100] "GET /bar/create HTTP/1.0" 200 1116
```
Similarly, we can find every line that has a 200 within it:

```
awk '200 {print f}{f=$0}' **/access.log*
```
So to do this with a 404, on the next line we do:
```
awk '/404/{print f}{f=$0}' **/access.log*
```

#### https://cmdchallenge.com/#/print_files_if_different

> Print all files with a .bin extension in the current directory that are different than the file named base.bin.

First, we can just look at the files in the folder:

```
base.bin
file1.txt
file2.txt
test1.bin
test2.bin
test3.bin
test4.bin
test5.bin
test6.bin
test7.bin
```
We can do a for loop, and print, "hello" for every file in t*

```
for f in t*; do echo "hello"; done
hello
hello
hello
hello
hello
hello
hello
```
This is using the, "f in t*; do", which counts the files that start with t, showing it to be 7, which corresponds to above. However if we do all files, "for f in *; do ..." we will see 10 counts for the entire 10 files.

We can now use this f also as a variable in a following function with the $f decorator filled in, so $f will be equal to test1.bin, test2.bin, test3.bin, etc. as we move forward throughout the list.

Meanwhile, the function, "cmp -s" compares two files, byte by byte. So for example if we do the following, we get a result:

```
cmp base.bin file1.txt
base.bin file1.txt differ: char 1, line 1

cmp -l base.bin file1.txt
cmp: EOF on file1.txt after byte 18
 1 130 124
 2  53 150
 3 362 151
 4 104 163
 5 214  40
 6   1 151
 7 276 163
 8 225  40
 9 374 152
10 264 165
11  66 156
12 373 153
13 334  40
14 272 146
15 300 151
16  40 154
17 324 145
18  46  56
```
This is a sort of, "diff" between two different files.

So comparing each file to base.bin would be:

```
for f in t*; do cmp base.bin $f; done
base.bin test2.bin differ: char 20, line 1
base.bin test4.bin differ: char 57, line 1
base.bin test5.bin differ: char 71, line 1
base.bin test7.bin differ: char 27, line 1
```
But we need to print out the file names, not the differences, so we do:

```
for f in t*; do cmp -s base.bin $f | echo $f; done

test1.bin
test2.bin
test3.bin
test4.bin
test5.bin
test6.bin
test7.bin
```
Strangly however, we just get a result showing all of the files, rather than the 4 files we had found above.

The double pipe gives us the answer we are looking for. Why is that? What is the double pipe doing?

* If the status of the first command, "cmp -s base.bin $f" is not zero, then do the second command, "echo $f. So basically, for each line that we get an answer, we echo the $f, and for each line there's no answer, nothing happens.
* Whereas with the single pipe, it's just printing out $f every time.
* If we had used && rather than || we would have printed out all of the opposite answers, because the second command only executes if the first command reports nothing.

```
for f in t*; do cmp -s base.bin $f || echo $f; done

test2.bin
test4.bin
test5.bin
test7.bin
```


#### https://cmdchallenge.com/#/nested_dirs

> There is a file: ./.../ /. .the flag.txt   Show its contents on the screen.

* In this situation, we have to search the entire filesystem to get something to show up.

So first starting out:

```
find / -name *.txt

/usr/share/doc/mount/mount.txt
/usr/share/perl/5.26.1/Unicode/Collate/allkeys.txt
/usr/share/perl/5.26.1/Unicode/Collate/keys.txt
/usr/share/perl/5.26.1/unicore/Blocks.txt
/usr/share/perl/5.26.1/unicore/NamedSequences.txt
...

```
We get a huge number of responses. Filtering this down:

```
find / -name *.txt | grep flag

/var/challenges/nested_dirs/.../  /. .the flag.txt
```
So if we try to cat the xargs:

```
find / -name *.txt | grep flag | xargs cat

cat: /var/challenges/nested_dirs/.../: Is a directory
cat: /.: Is a directory
cat: .the: No such file or directory
cat: flag.txt: No such file or directory
``
So somehow the directory is not being handed to us in such a way that we can print it out as an xargs, it's being given in a parsed manner.

A better way to operate on the result would be to use find's -exec [command] {} + option, which runs a command on the specified file, which is similar to how xargs works.

```
find / -name "*flag.txt" -exec cat {};

find: missing argument to `-exec'
```

However as we can see, we are missing an argument, which we can just use, "\" which seems to mean, the file in question.

```
find / -name "*flag.txt" -exec cat {} \;

you got it!
```

#### https://cmdchallenge.com/#/find_tabs_in_a_file

> How many lines contain tab characters in the file named file-with-tabs.txt in the current directory.

* "sed" - serial editor, with the input '/\t/!d' ... does \t for tab
* !d - delete the pattern space, only if the pattern does not match. So if there is no tab, delete it.
* * is the greedy search
* wc is the wordcount function - word and byte counts for each file.
* wc -l print newline counts

```
sed '/\t/!d' * | wc -l
```

#### https://cmdchallenge.com/#/remove_files_without_extension

> There are files in this challenge with different file extensions. Remove all files without the .txt and .exe extensions recursively in the current working directory.

```
find -type f ! -regex '.*\(exe\|txt\)$' -delete
```

#### https://cmdchallenge.com/#/remove_files_with_a_dash

> There are some files in this directory that start with a dash in the filename. Remove those files.

```
find -type f ! -regex '.*\(exe\|txt\)$' -delete
```

#### https://cmdchallenge.com/#/print_sorted_by_key

> There are two files in this directory, ps-ef1 and ps-ef2. Print the contents of both files sorted by PID and delete repeated lines.

```
sort -unk2 *
```
#### https://cmdchallenge.com/#/IPv4_listening_ports

> In the current directory there is a file called netstat.out. Print all the IPv4 listening ports sorted from the higher to lower.

```
grep tcp netstat.out|grep -i listen|grep -v tcp6|awk '{print$4}' |awk -F: '{print $2}'|sort -rn
```




##### Breakdown

[Pipe |](https://linuxhint.com/linux-pipe-command-examples/)

