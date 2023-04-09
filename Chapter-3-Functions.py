Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/sayes/OneDrive/Desktop/Python_Project_sample/Basic_Python/Automated the Boring stuff using python/Chapter - 2 - Write a Program.py
Hello World
What is your name
Sayee
It is good to meet you, Sayee
The length of your name is: 5
What is your age?
28
You will be 29 in a year.
>>> 
>>> 
>>> 
>>> # Functions
>>> # Print
>>> print ('Hello')
Hello
>>> 
>>> # input
>>> input()
Hello
'Hello'
>>> 
>>> 
>>> # len
>>> 
>>> len('Sayee')
5
>>> len('')
0
>>> len('Sayee')*10
50
>>> 
>>> 
>>> # Convert between data types
>>> str(13)
'13'

int(14
)
14
float('3.14')
3.14


int('26')+1
27

#string Concatenation cannot be performed on integers
26 + 'years'
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    26 + 'years'
TypeError: unsupported operand type(s) for +: 'int' and 'str'


#integers cannot be calculated if they are expressed as strings
'26'+1
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    '26'+1
TypeError: can only concatenate str (not "int") to str


#so it is important to convert the data type in order to perform the relative functionality
