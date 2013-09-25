spellcheck
==========

Spell checking program. Python3

##Notice
While researching this problem I was able to find quite a few implementations of this in numerous languages. Not sure why people would pick Java but to each there own. I found that the best solution to this issue was located here: https://github.com/yuxinzhu/spellchecker.
I attempted to re-write this in Python 3 by hand but found that it produce some unforseen results, so I then used the built in 2to3 tool which was able to upgrade the program from a python2.7 to python3.x environment.

I thought I would be upfront with this, for there were two many examples online for my code to not be directly influenced/copied.

###Problem

Write a program that reads a large list of English words (e.g. from /usr/share/dict/words on a unix system) into memory, and then reads words from stdin, and prints either the best spelling suggestion, or "NO SUGGESTION" if no suggestion can be found. The program should print ">" as a prompt before reading each word, and should loop until killed.

Your solution should be faster than O(n) per word checked, where n is the length of the dictionary. That is to say, you can't scan the dictionary every time you want to spellcheck a word.

For example:

	> sheeeeep
	sheep
	> peepple
	people
	> sheeple
	NO SUGGESTION
	The class of spelling mistakes to be corrected is as follows:

Case (upper/lower) errors: "inSIDE" => "inside"
Repeated letters: "jjoobbb" => "job"
Incorrect vowels: "weke" => "wake"
Any combination of the above types of error in a single word should be corrected (e.g. "CUNsperrICY" => "conspiracy").

If there are many possible corrections of an input word, your program can choose one in any way you like. It just has to be an English word that is a spelling correction of the input by the above rules.

Final step: Write a second program that *generates* words with spelling mistakes of the above form, starting with correctly spelled English words. Pipe its output into the first program and verify that there are no occurrences of "NO SUGGESTION" in the output.
