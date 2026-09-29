Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype conversions
int(5)
5
int(5.6)
5
int("sai")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("sai")
ValueError: invalid literal for int() with base 10: 'sai'
int(5+9j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(5+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
float(8)
8.0
float(5.9)
5.9
float("sai")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float("sai")
ValueError: could not convert string to float: 'sai'
float(5+8j)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float(5+8j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
str(1)
'1'
str(4.9)
'4.9'
str("hi")
'hi'
str(5+7j)
'(5+7j)'
str(True)
'True'
str(False)
'False'
complex(1)
(1+0j)
>>> complex(5.8)
(5.8+0j)
>>> complex("hi")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    complex("hi")
ValueError: complex() arg is a malformed string
>>> complex("9+7j)
...         
SyntaxError: unterminated string literal (detected at line 1)
>>> complex(9+7j)
...         
(9+7j)
>>> ocmplex(True)
...         
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    ocmplex(True)
NameError: name 'ocmplex' is not defined. Did you mean: 'complex'?
>>> complex(True)
...         
(1+0j)
>>> complex(False)
...         
0j
>>> bool(1)
...         
True
>>> bool(5.8)
...         
True
>>> bool("hi)
...      
SyntaxError: unterminated string literal (detected at line 1)
>>> bool("hii")
...      
True
>>> bool(5+7k)
...      
SyntaxError: invalid decimal literal
bool(7+6j)
     
True
bool(True)
     
True
bool(False)
     
False
