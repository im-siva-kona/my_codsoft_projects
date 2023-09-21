print('***A Simple Calculator***')
print('1.Addition')
print('2.Subtraction')
print('3.Multipliication')
print('4.Division')
print('5.Modular Division')
def addition(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def modulo(a,b):
    return a%b
while True:
    choice=int(input('Enter your choice(1-5):'))
    n1=int(input('enter the first number:'))
    n2=int(input('enter the second number:'))
    if choice==1:
        print(n1,'+',n2,'=',addition(n1,n2))
    elif choice==2:
        print(n1,'-',n2,'=',subtract(n1,n2))
    elif choice==3:
        print(n1,'*',n2,'=',multiply(n1,n2))
    elif choice==4:
        print(n1,'/',n2,'=',divide(n1,n2))
    elif choice==5:
        print(n1,'%',n2,'=',modulo(n1,n2))
    next_calculation = input("Want to perform other calculation?(yes/no):")
    if next_calculation == "no":
        break
    
else:
    print("please enter a valid choice")
