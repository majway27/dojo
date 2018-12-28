# TODO enumerate(), len(),
# https://www.programiz.com/python-programming/examples/add-matrix
# https://www.programiz.com/python-programming/examples/transpose-matrix

"""
List Party

Sources:
- https://www.programiz.com/python-programming/list
"""

# Comprehension
a_list_of_numbers = [num for num in range(10)]
print(a_list_of_numbers)
a_special_list_of_numbers = [num for num in range(10) if num % 2 == 0]
print(a_special_list_of_numbers)
a_very_special_list_of_numbers = [2 ** num for num in range(10) if num % 2 == 0]
print(a_very_special_list_of_numbers)

# Regular
customers = ['widgetsforu', 'starkindustries', 'umbrellacorp']

# Nested
customer_cases = [
    ['[widgetsforu', 2, "happy"],
    ['starkindustries', 3, "meh"],
    ['umbrellacorp', 19, "mad"]
]
# Access elements
index = 0
print("first customer: " + str(customers[index]) + " Case: " + str(customer_cases[index]))

# "Searching"
print('Is starkindustries a customer? ' + str('starkindustries' in customers))  # returns True bool

# Slice

# Extend/Append/Insert
customers.append('initech')
customers.extend(['Wayne Enterprises', 'Acme'])

customer_cases = customer_cases + ([['umbrellacorp', 1, "mad"]] * 3)
customer_cases.insert(2, ['starkindustries', 1, "happy"])
print(customer_cases)

# Report time sort/reverse, Iteration/looping
customers.sort()
# Beware sort() not returning a value, it is an in-place sort
print('Customer report: ' + str(customers))
# Rpt time, case ct
total_cases = 0
for case in customer_cases:
    total_cases += case[1]
print("Case count report: " + str(total_cases))

# Delete/Remove
# I don't like del
# remove - by item
# pop - by index
# Customer quit
customer_cases[-4:] = []
customers.remove('umbrellacorp')
print(customer_cases)
print(customers)
# I quit
customers.clear()