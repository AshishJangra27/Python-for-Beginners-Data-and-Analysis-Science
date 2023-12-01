# Exception Handling

try:
    x = 10
    print(1)
    print(x/0)
    print(2)
except:
    print('Error Occured!')
print('-'*30)

# Exception with Specific Errors
try:
    num = 0
    print(int('e23'))
except ZeroDivisionError:
    print('Zero is in the divisor')
except:
    print('Unknown Error')
print('-'*30)

# Final Exception with Specific Errors

try:
    num1 , num2 = 10,0
    print(int('3.14'))

except ZeroDivisionError as zde:
    print(zde)

except Exception as e:
    print(e)

else:
    print('Everything is fine!')

finally:
    print('Program End!')
