Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python39'
>>> os.chdir('d:')
>>> os.getcwd()
'D:\\'
>>> os.chdir('c:\\Users\\hp\\Desktop\\UFT\\15novML')
>>> os.getcwd()
'c:\\Users\\hp\\Desktop\\UFT\\15novML'
>>> f = open('ekfile.txt','w')
>>> f.write('ek line likh dete hain')
22
>>> f.close()
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/15novML/day9/test.py
Hum file banayenge
>>> f = open('ekfile.txt','w')
>>> f.write('ek line likh dete hain')
22
>>> f.close()
>>> f.close()
>>> 
>>> 
>>> 
>>> f = open('ekfile.txt','r')
>>> content = f.read()
>>> f.close()
>>> content
'ek line likh dete hain'
>>> 
>>> 
>>> f = open('ekfile.txt','w')
>>> f.write('naya content aa gaya')
20
>>> f.close()
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/15novML/day9/file_handle.py
>>> r
'name,age,gender,city\nRahul Kumar,20,Male,Ajmer\nAmit Kumar,21,Male,Raipur\nNeha,20,Female,Jaipur\n\n\n\n'
>>> print(r)
name,age,gender,city
Rahul Kumar,20,Male,Ajmer
Amit Kumar,21,Male,Raipur
Neha,20,Female,Jaipur




>>> 
= RESTART: C:/Users/hp/Desktop/UFT/15novML/day9/file_handle.py
>>> print(r)
name,age,gender,city
Rahul Kumar,20,Male,Ajmer
Amit Kumar,21,Male,Raipur
Neha,20,Female,Jaipur
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/15novML/day9/file_handle.py
name,age,gender,city
Rahul Kumar,20,Male,Ajmer
Amit Kumar,21,Male,Raipur
Neha,20,Female,Jaipur
>>> d = {'name':['r','a','n'],'age':[]}
>>> r
'name,age,gender,city\nRahul Kumar,20,Male,Ajmer\nAmit Kumar,21,Male,Raipur\nNeha,20,Female,Jaipur'
>>> r1 = r.split('\n')
>>> r1
['name,age,gender,city', 'Rahul Kumar,20,Male,Ajmer', 'Amit Kumar,21,Male,Raipur', 'Neha,20,Female,Jaipur']
>>> k = r1[0].split(',')
>>> k
['name', 'age', 'gender', 'city']
>>> v = [i.split(',') for i in r1[1:]]
>>> v
[['Rahul Kumar', '20', 'Male', 'Ajmer'], ['Amit Kumar', '21', 'Male', 'Raipur'], ['Neha', '20', 'Female', 'Jaipur']]
>>> # enumerate, zip
>>> 