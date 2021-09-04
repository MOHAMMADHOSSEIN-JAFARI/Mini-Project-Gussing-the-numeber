import random
f= 1
g= 99
a = random.randint(f,g)
print(a)
b= input("please inter: ")
while b != 'd':
    if b == 'k':
        g= a-1
        a = random.randint(f,a-1)
        print(a)
        b= input("please inter: ")
        continue   
    elif b == 'b':
        f= a+1
        a= random.randint(f,g)
        print(a)
        b= input("please inter: ")
        continue
print('it is corret')

    

    