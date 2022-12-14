def food():
    print('chicken burgers for everyone')
food()
food()

def blaize():
    print('hey its blaize')

blaize()



def order(item):
    if(item=='chicken burger'):
        return 1
itemname=input('enter the item')
result=order(itemname)
print('result is ', result)
if(result == 1):
    print('5$ bitch')
elif(result==2):
    print('10$ bitch')
else:
    result<=3