####Comment out your answers when you're done with each question###

#1a) Open your the example.txt file for reading, and print the contents of the file to the console. You can consult the markdown file for instructions on how to do this.





#1b) You can also print the file name by printing f.name. Do this above as well





#2) If you wanted to print only a certain number of characters from your file, you can pass an integer argument into f.read(). Copy and paste your code from question 1 and do that below.





#3)You can also read your file line by line, which is useful for larger files. You can do this by using f.readline(). If you do this multiple times, it will continue to the next line and read.
#Use f.readline() to read the first three lines of your file. In your print functions, include an end='' to remove the spacing between each line printed. (Example: print(f.readline(), end='')






#4) You can loop through the file to read each line one at a time rather than read the entire file at once. Use a for loop and readline to print each line of the example.txt file to the console:





#5) You can also append content to the end of an existing file by using 'a' instead of 'r' when opening the file. You can then use f.write("content here") inside to write a new line
#Use a for loop to append 10 new lines of content to the example.txt file. The content can be whatever you want.





###Writing files - If you write a file that already exists, it will overwrite the file. If you write a file that doesn't exist, it will create it.###
#6) Write a new file called example2.txt that includes at least 10 lines of content. You can create your content however you want by using f.write() (for loop, while loop, etc.).






###Bonus####

#1) You can open mutliple files at once, where you are reading one file and writing another file. This can be formated like so:
'''
with open('example.txt', 'r') as rf:
  with open('example_copy.txt', 'w') as wf:
'''
#Using a for loop  and the format above, create an exact copy of example.txt called example_copy.txt





#2) Delimination is a method programmers use to separate data in a uniform way. This helps to organize the data into easily parsable units.
#Two common forms of delimination are tab delimination ('\t') and new line ('\n') delimination. You may have used '\n' in question 6 to write each piece of data on a new line.

#Using a for loop, write a file that contains 10 pieces of data (if using numbers you may need to convert to string to add the'\t') that are separated by tabs on one line of code.






#3) So far you have just been reading and writing files. What if you want to perform a calculation in your python file, obtain some data, and then organize it in an easily readable way into a new file?

#Step 1 - Using a for loop  and the .append() method, populate an empty list with every multiple of 10 between 0 and 1000





#Step 2 - Open a new txt file and write this data into it, such that each data point (number) is tab-deliminated ('\t'), and each row as 10 values.
#HINT: You will need to use conditionals, a new variable to monitor when there are 10 data points added to a row, and the '\n' delimination to specify when to go to the next line.





#Step 3 - Read your new file and print to the console. You should be able to also copy and paste your data from your txt file into excel, and it will populate each cell in the exact format you have it in
#You can try that last bit on your own and let me know how it goes.














