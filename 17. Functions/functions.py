def greet():
    print('Hello')

for i in range(5):
    greet()
print('-'*20)

# Defining the Scope of the Variables
g_var = 10
def scope():
    l_var = 5
    print(g_var,l_var)

scope()
# print(g_var,l_var)
print('-'*20)

# Passing the Prameters

def greet(name = '-----'):
    print('Hello',name)

greet('Ashish')
greet(name = 'Ashish')
greet()
print('-'*20)

# Passing the Prameters with print

def subm(a = 0,b = 0):
    print(a+b)
subm(5,10)
subm(a = 5,b = 10)
subm(b = 5)
subm()
subm(5,10)
print('-'*20)

# Return
def subm(a = 0,b = 0):
    return a+b

s = subm(10,5)
print(s)
print('-'*20)

# Multi-Return
def arithmetic(a = 0,b = 0):
    return a+b , a-b, a*b

s = arithmetic(10,5)
print(s)
print(type(s))

# Calling Different Functions
lst = [1,2,3,4,5]

def sq(lst):
    return [i**2 for i in lst]
def cu(lst):
    return [i**3 for i in lst]

def final(lst):

    lst_1 = sq(lst)
    lst_2 = cu(lst)

    return [lst_1[i] + lst_2[i] for i in range(len(lst_1))]


print(final(lst))

print('-'*20)
