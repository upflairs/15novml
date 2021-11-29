######################################
##n = input('Enter name:')
##a = input('Enter age:')
##g = input('Enter gender:')
##c = input('Enter city:')
##f = open('data.txt','a')
##f.write(','.join([n,a,g,c])+'\n')
##f.close()
#####################################
f = open('data.txt','r')
r = f.read()
f.close()
print(r)
