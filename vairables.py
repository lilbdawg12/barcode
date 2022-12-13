myVariableName = "Blaize"
print (myVariableName)

myvariablename = 'john'
print(myvariablename)

my_variable_name = 'nim'
print(my_variable_name)


c, w, a, t, y, j, d= 'blue','red','dixxy','life','adw','adwwd','pop'
print (w)
print (a)
print (t)

# one value to multiple variables
x = w = a = 'blue'
print(w)
print(x)
print(a)


# unpacking a list

flowers = ['daisies', 'roses', 'peddels']

x,y,z = flowers

print (x)

# output vairables
x = 'Blaize you are so fucking awsome hahaha'
print(x)


x='a'
e='s'
g='p'
print(x,e,g)

a='blaize '
b='justin '
c='avrenim '
print(a + b + c)


x=3
y=9

print (x*y)
print(x-y)
print(x==y)
print(x<=y)


x='blaize'
l=1

print (x,+l)

# Gloabal vairables

x = 'awsome'

def myfuncq():
    print('python is ' + x)

myfuncq()


button = 'save'

def buttontype():
    print('you sure you wanna log out?:' + button)

buttontype()

# Gloabal keyword after defining your function will apply to every vairable attatch

def globalvair():
    global x
    x = 'amazing'

globalvair()

print ('python is '+ x)
print (x)



x='a '
a='c '
m='j '
j='h '
h='g '
g='f '
l='d '
f='s '

added=x+a+m+j+h+g+l+f
print (added)