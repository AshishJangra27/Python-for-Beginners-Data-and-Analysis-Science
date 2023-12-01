# Zip
lst1 = ['Ashish','Ankur','Avinash']
lst2 = [25,27,32]
print(list(zip(lst1,lst2)))
print('-'*50)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print([list(row) for row in zip(matrix)])
print([list(row) for row in zip(*matrix)])
print([list(row) for row in zip(*[list(row) for row in zip(*matrix)])])
print('-'*50)

lst_1 = [2,4,6]
lst_2 = [1,3,5]

print(sum([i*j for i,j in zip(lst_1,lst_2)]))

print('*'*(50))

# Filter
lst = [1,2,3,4,5,6,7,8,9]
def is_even(n):
    return n%2 == 0
print(list(filter(is_even,lst)))
print('*'*(50))

# Lambda
add_num = lambda x,y : x*y
print(add_num(5,10))
print('-'*(50))

num = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2 == 0, num)))
print('*'*(50))


# Map
num = [1,2,3,4,5,6,7,8,9]
def sqr(x):
    return x**2

print(list(map(sqr,num)))
print('-'*(50))

names = ['ashish','bob','chandan','don']
print(list(map(lambda x : len(x), names)))
