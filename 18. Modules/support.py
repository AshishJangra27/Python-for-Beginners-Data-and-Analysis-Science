def greet(name = '-----'):
    return 'Hello ' + name

def subm(a = 0,b = 0):
    return a+b

def arithmetic(a = 0,b = 0):
    return a+b , a-b, a*b

def sq(lst):
    return [i**2 for i in lst]
def cu(lst):
    return [i**3 for i in lst]

def final(lst):
    lst_1 = sq(lst)
    lst_2 = cu(lst)
    return [lst_1[i] + lst_2[i] for i in range(len(lst_1))]
