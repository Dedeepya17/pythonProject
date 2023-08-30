def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a%b
print('select the operation')
print('1.add')
print('2.sub')
print('3.mul')
print('4.div')
choice=input('please enter the choice(1/2/3/4):')

num_1=float(input('enter the first value: '))
num_2=float(input('enter the second value:'))
if choice=='1':
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice == '2':
    print(num_1,"-",num_2,"=",sub(num_1,num_2))
elif choice == '3':
    print(num_1, "*", num_2, "=", mul(num_1, num_2))
elif choice == '4':
    print(num_1, "%", num_2, "=", div(num_1, num_2))
else:
    print('invalid input')