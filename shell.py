Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [4,5,7,2,9]
>>> b = [i*2 for i in a]
>>> b
[8, 10, 14, 4, 18]
>>> c = (i*2 for i in a)
>>> c
<generator object <genexpr> at 0x000001FFFFCD7F90>
>>> list(c)
[8, 10, 14, 4, 18]
>>> c
<generator object <genexpr> at 0x000001FFFFCD7F90>
>>> list(c)
[]
>>> c = (i*2 for i in a)
>>> next(c)
8
>>> next(c)
10
>>> next(c)
14
>>> list(c)
[4, 18]
>>> next(c)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    next(c)
StopIteration
>>> list(c)
[]
>>> c = (i*2 for i in a)
>>> for i in c:
	print(i,'is the value')

	
8 is the value
10 is the value
14 is the value
4 is the value
18 is the value
>>> 