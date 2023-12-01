
class person:
    name = 'Ashish'
    age  = 25

p1 = person()
print(p1.name)
print(p1.age)

print('-'*30)

p1.name = 'Ankur'
p1.age  = 26
print(p1.name)
print(p1.age)

print('-'*30)

p2 = person()
print(p2.name)
print(p2.age)

print('*' * 30)

class mathematics:

    def greet(self):
        print('Hello')
        return 'Hi'

    def factorial(self,n):
        s = 1
        for i in range(1,n+1):
            s*=i
        return s

    def lst_mul(self,lst):
        s = 1
        for i in lst:
            s *= i
        return s

    def lst_dot(self,lst_1, lst_2):
        return [lst_1[i]*lst_2[i] for i in range(len(lst_1))]

math = mathematics()
print(math.greet())
print('-'*30)
print(math.factorial(5))
print('-'*30)
print(math.lst_mul([3,4,5]))
print('-'*30)
print(math.lst_dot(lst_1 = [1,2,3,4],lst_2 = [2,3,4,5]))
print('-'*30)
