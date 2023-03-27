'''
Docstring - Multiline comment

Data types in python:
'''
'''
1. Integer - მთელი რიცხვები Z, int - in python (-INF, +INF). example:
'''
age = 22
print(type(
    age
))

# ოპერაციები Integer-ებზე
print(age + 2)
print(age - 2)
print(age / 2)
print(age * 2)
# გაყოფა და დამრგვალება
print(age // 2)
# ახარისხება
print(age ** 2)
# Modulus - ნაშთის ოპერატორი
print(age % 2)

'''
2. String - ტექსტი, str - in python
'''
name = 'John'
name2 = "Jane"
name3 = """Jake"""
name4 = '''Mary'''

print(type(name))

# ოპერაციები სტრინგებზე
# concatenation (Slow Operation!)
print(name + ' ' + name2)
# format string - fstrings
print(f'{name} and {name2}')
print(name2.lower())
print(f'Old: {name2}; in lower case {name2.lower()}')
print(name2)

'''
Variable naming
-------------------
Allowed:
name1,
full_name,
first_name,
username,
home_address,

Reccomendation:
use meaningful long names (don't use single characters, a, b, n),
not reccomended to use numbers in variable naming,

Restricted:
1231231 <-> Error,
1name <-> Error,
%$@sfwe/ <-> Error,

Reserved
int <-> Error,
str <-> Error,
print <-> Error,
'''

'''
Constatns
SCREAMING_SNAKE_CASE
'''
FIRST_NAME = 'Jane'

'''
Fractions, float in python - წილადი რიცხვები Q, (-INF, -1, -0.9, -0.98, 0, 0.6, 0.9, 1, +INF)
'''
pi = 3.14