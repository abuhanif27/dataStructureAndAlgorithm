num1 = 10
num2 = num1
print(f'number_one:  {num1}, and number_two: {num2}')
print(f'number_one id is: {id(num1)}, and number_two id is: {id(num2)} \
,, are they locate in the same address: {'yes' if id(num1) == id(num2) else 'no'}')

num1 = 11
print('\nAfter Update\n')
print(f'number_one:  {num1}, and number_two: {num2}')
print(
    f'number_one id is: {id(num1)}, and number_two id is: {id(num2)} \
     ,, are they locate in the same address: {'yes' if id(num1) == id(num2) else 'no'}')

dict1 = {
    'value': 11
}
dict2 = dict1

print('\n\n Dictionary\n')
print(f'number_one:  {dict1['value']}, and number_two: {dict2['value']}')
print(f'number_one id is: {id(dict1)}, and number_two id is: {id(dict2)} \
,, are they locate in the same address: {'yes' if id(dict1) == id(dict2) else 'no'}')

print("\nAfter Update\n")

dict2['value'] = 22
print(f'number_one:  {dict1['value']}, and number_two: {dict2['value']}')
print(f'number_one id is: {id(dict1)}, and number_two id is: {id(dict2)} \
,, are they locate in the same address: {'yes' if id(dict1) == id(dict2) else 'no'}')
