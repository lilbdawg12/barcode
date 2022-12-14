num1 = int(input('number 1: '))
num2 = int(input('number 2: '))
op = input('output: ')

if(op=='+'):
    print(num1+num2)

elif (op=='-'):
    print(num1-num2)
elif (op=='*'):
    print(num1*num2)
elif (op=='/'):
    print(num1/num2)

elif (op=='**'):
    print(num1**num2)

else: 
    print ('please use [+,-,*,**,/] for calculator to work')

