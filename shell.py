Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open(r'C:\Users\hp\Desktop\UFT\15novML\day9\data.txt','r')
>>> f = open('C:\Users\hp\Desktop\UFT\15novML\day9\data.txt','r')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> f = open('C:\\Users\\hp\\Desktop\\UFT\\15novML\\day9\\data.txt','r')
>>> f = open(r'C:\Users\hp\Desktop\UFT\15novML\day9\data.txt','r')
>>> r = f.read()
>>> f.close()
>>> r1 = r.split('\n')
>>> k = r1[1].split(',')
>>> k = r1[0].split(',')
>>> c = [i.split(')]
	     
SyntaxError: EOL while scanning string literal
>>> c = [i.split(',') for i in r1[1:]]
>>> 
>>> k
['name', 'age', 'gender', 'city']
>>> c
[['Rahul Kumar', '20', 'Male', 'Ajmer'], ['Amit Kumar', '21', 'Male', 'Raipur'], ['Neha', '20', 'Female', 'Jaipur']]
>>> d = {i:[] for i in k}
>>> d
{'name': [], 'age': [], 'gender': [], 'city': []}
>>> for i in range(len(k)):
	print(i)

	
0
1
2
3
>>> for i in range(len(k)):
	for v in c:
		print(v[i])
	print(' ')

	
Rahul Kumar
Amit Kumar
Neha
 
20
21
20
 
Male
Male
Female
 
Ajmer
Raipur
Jaipur
 
>>> d = {}
>>> for i in range(len(k)):
	d[k[i]] = []
	for v in c:
		d[k].append(v[i])

		
Traceback (most recent call last):
  File "<pyshell#25>", line 4, in <module>
    d[k].append(v[i])
TypeError: unhashable type: 'list'
>>> d = {}
>>> for i in range(len(k)):
	d[k[i]] = []
	for v in c:
		d[k[i]].append(v[i])

		
>>> d
{'name': ['Rahul Kumar', 'Amit Kumar', 'Neha'], 'age': ['20', '21', '20'], 'gender': ['Male', 'Male', 'Female'], 'city': ['Ajmer', 'Raipur', 'Jaipur']}
>>> k
['name', 'age', 'gender', 'city']
>>> for i in enumerate(k):
	print(i)

	
(0, 'name')
(1, 'age')
(2, 'gender')
(3, 'city')
>>> r
'name,age,gender,city\nRahul Kumar,20,Male,Ajmer\nAmit Kumar,21,Male,Raipur\nNeha,20,Female,Jaipur'
>>> r1
['name,age,gender,city', 'Rahul Kumar,20,Male,Ajmer', 'Amit Kumar,21,Male,Raipur', 'Neha,20,Female,Jaipur']
>>> for i in enumerate(k):
	print(i)

	
(0, 'name')
(1, 'age')
(2, 'gender')
(3, 'city')
>>> for i,j in enumerate(k):
	print(i,j)

	
0 name
1 age
2 gender
3 city
>>> d = {}
>>> for i,j in enumerate(k):
	d[j] = []
	for v in c:
		d[j].append(v[i])

		
>>> d
{'name': ['Rahul Kumar', 'Amit Kumar', 'Neha'], 'age': ['20', '21', '20'], 'gender': ['Male', 'Male', 'Female'], 'city': ['Ajmer', 'Raipur', 'Jaipur']}
>>> 
>>> 
>>> 
>>> a = [45,78,96]
>>> b = [30,40,60]
>>> a+b
[45, 78, 96, 30, 40, 60]
>>> p = []
>>> for i,v in enumerate(a):
	p+= [(v,b[i])]

	
>>> p
[(45, 30), (78, 40), (96, 60)]
>>> q = list(zip(a,b))
>>> q
[(45, 30), (78, 40), (96, 60)]
>>> c
[['Rahul Kumar', '20', 'Male', 'Ajmer'], ['Amit Kumar', '21', 'Male', 'Raipur'], ['Neha', '20', 'Female', 'Jaipur']]
>>> r
'name,age,gender,city\nRahul Kumar,20,Male,Ajmer\nAmit Kumar,21,Male,Raipur\nNeha,20,Female,Jaipur'
>>> cc = [[30,'hello'],[40,'bye'],[50,'nice']]
>>> list(zip(cc))
[([30, 'hello'],), ([40, 'bye'],), ([50, 'nice'],)]
>>> list(zip(*cc))
[(30, 40, 50), ('hello', 'bye', 'nice')]
>>> list(zip(*c))
[('Rahul Kumar', 'Amit Kumar', 'Neha'), ('20', '21', '20'), ('Male', 'Male', 'Female'), ('Ajmer', 'Raipur', 'Jaipur')]
>>> c1 = list(zip(*c))
>>> k
['name', 'age', 'gender', 'city']
>>> dd = {}
>>> for i,v in enumerate(k):
	dd[v] = c1[i]

	
>>> dd
{'name': ('Rahul Kumar', 'Amit Kumar', 'Neha'), 'age': ('20', '21', '20'), 'gender': ('Male', 'Male', 'Female'), 'city': ('Ajmer', 'Raipur', 'Jaipur')}
>>> 
>>> 
>>> 
>>> 
>>> c
[['Rahul Kumar', '20', 'Male', 'Ajmer'], ['Amit Kumar', '21', 'Male', 'Raipur'], ['Neha', '20', 'Female', 'Jaipur']]
>>> k
['name', 'age', 'gender', 'city']
>>> list(zip(k,zip(*c)))
[('name', ('Rahul Kumar', 'Amit Kumar', 'Neha')), ('age', ('20', '21', '20')), ('gender', ('Male', 'Male', 'Female')), ('city', ('Ajmer', 'Raipur', 'Jaipur'))]
>>> ddd = dict(zip(k,zip(*c)))
>>> ddd
{'name': ('Rahul Kumar', 'Amit Kumar', 'Neha'), 'age': ('20', '21', '20'), 'gender': ('Male', 'Male', 'Female'), 'city': ('Ajmer', 'Raipur', 'Jaipur')}
>>> ### Please download and insall ANACONDA before MONDAY class
>>> 