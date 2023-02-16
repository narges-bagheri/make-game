import random
x=0
number=random.randint(0,10)
# print(number)
print('you have just 5 soul !!! ')
print('Enter your guess number : ')
while x<5:
    x=x+1
    me=int(input('enter a num : '))
    if number==me:
        break
if number==me:
    print(' you win whit '+str(x)+' tries')
else:
    print('you lose '+str(x)+' tries full ')
       
