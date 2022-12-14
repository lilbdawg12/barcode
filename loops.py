# What is iteration

#   Iteration is doing something,
#   again and again unitl a specific condition,
#   is satisfied

#Type of Iteration Statements

#1. FOR LOOPS
#2. WHILE LOOPS
#3. 


# FOR LOOP

#syntax;

#   for i in range(lower limit, upperlimit):
#       loop body

# in for loop the loop will only run till value of i is equal to
# i = upperlimit -1

#   for example

#   for I in range (0,5):
#        print(I)
# The program will print numbers from
# 0 (lower limit) to 4 (upper limit -1)

for blaize in range (0,20):
    print (blaize + 1)

#WHILE LOOPS

i = int(input('Enter the number: '))
while(i>5):
    print (i)
    i = i -1

blaize = int(input('hello please type a number here: '))
while(blaize>-1):
    print (blaize)
    blaize = blaize -1


    

nothing = int(input('you are very tiny so please enter your weight amount here: '))
while(nothing>=1):
    print (nothing)
    nothing =nothing - 1


poke = int(input('subjeccted numebr: '))
while(poke>=1):
    print(poke-1)
    poke = poke -1 

anim = int(input("please dont tell me your number"))
while(anim>=1):
    print(anim-1)
    anim=anim-1



num2 = int(input('hello give me a number'))
num1 = int(input('hello give me a number'))
output= str(input('hello give me a output'))

if (output=='+'):
    print(num1+num2)

elif (output=='-'):
    print(num1-num2)
elif (output=='/'):
    print(num1/num2)
elif(output=='*'):
    print (num1*num2)
else:
    print('needs to be a indicater')




blaize = int(input('hello bitch how you doing'))
while(blaize>=0):
    print(blaize-1)

blaize=blaize