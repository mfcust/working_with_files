# Working With Files

Being able to read data and write data into files is an important skill to have in Python. In this assignment, you will learn how to do both. In your current directory, you have a text file called example.txt. Let's say I wanted to read what was inside that file without navigating to it and opening it up. I can first create a file object, as seen below:
```
f = open('example.txt')
```
The open function returns a file object, with a default to reading the file. In other words, the line of code above is exactly the same as the one below:
```
f = open('example.txt', 'r')
```
The second parameter 'r' means that you are opening the file to read it. You can change this to 'w' to write a new file, or to 'a' to append to an existing file. We'll touch base on those options more in your .py file.

Once you've opened your file by creating your file object f, you then need to use the .read() method on it and print that to the console in order to read your file. This looks like the following line of code:
```
print(f.read())
```
Lastly, you must always close your file! If you leave it open, it will make your program run slower and will take up more space in your RAM. Use the following line of code below to accomlpish this:
```
f.close()
```
There is a way to interact with files without having to explicity close them, and this method is probably best practice. It uses what's known as a context editor, and automatically closes the file after use. This looks like the following:
```
with open('example.txt', 'r') as f:
  print(f.read())
```
This accomplishes the same thing as the above code where you create a file object, open the file, read the file, and close the file. Anything that you want to do before closing the file must be indented like the print(f.read()) line. Once you stop indenting, the file closes. You can use whicheevr method you prefer, though this one may be easier to do in repl.it since you don't have to include a f.close() after every question.

Navigate to the python file to do more with files!





