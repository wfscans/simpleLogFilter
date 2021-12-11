# simpleLogFilter
diff view without all the obfuscated noise 

# usage
 * read diff from file: main.py \<filename\>
 * read diff from pipe: main.py -
 * pipe to 'less -R' for scrolling
 * print without color add nocolor after filename/pipe

# example
 * python3 main.py <filename>
 * git show | python3 main.py - | less -R
 * git show | python3 main.py - nocolor
