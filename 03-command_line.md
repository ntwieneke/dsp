# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

touch - create a new empty file

push/pop - allows you to easily switch between paths

* - applies a wildcard to that character

apropos - help articles, but should only be used as a last resort (google is better)

pipe vs redirect:

Pipe (|) will take the output of one command and pipe it through another command

Redirect (>) will take a file and write it to another file

Find - This will require a -name argument, the search parameter, and -print or pipe into another command

grep - allows you to search through a file for a term, can be done recursively with -R

env - shows you your PATH and other environment variables

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  list files in this directory

`ls -a`  lists all files that matches name argument

`ls -l`  lists file in long format

`ls -lh`  same as bove but 'human readable'

`ls -lah`  lists all files in long human readable format

`ls -t`  shows timestamp

`ls -Glp`  prevents group info from being show, and shows file type


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

-f interprets name argument as a directory, so you can use this to search through directories

-q displays nonprinting characters as ? might be useful for messy data

-R recursive (display subdirectories)

-x organizes files as rows

-L displays files with symbolic link

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

some commands cannot accept stand input stream from pipe, and xargs allows you to do this by breaking the list into acceptable sub-lists

for instance

echo {1..9} | xargs -n1 will out put echo 1-9 with 1 number per row
 



