# 1 .Syntax Errors
print("Hello, World!')

# 2. Runtime Erros | ZeroDivisionError
num1, num2 = 10, 0
result = num1 / num2  # This will raise a ZeroDivisionError

# 3. Logical Errors
def add_numbers(num1, num2):
    return num1 - num2

# 4. NameError
print(variable_number_1, function_for_sum())

# 5. TypeError
print("2" + 2)

# 6. IndexError
my_list = [1, 2, 3]
print(my_list[5])

# 7. KeyError
my_dict = {'name': 'John', 'age': 25}
print(my_dict['gender'])

# 8. AttributeError
x = 10
print(x.upper())

# 9. IndentationError
if True:
print("Indented incorrectly")

# 10. ImportError
import non_existent_module

# 11. ValueError
int('abc')
