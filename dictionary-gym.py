# TODO

"""
Dictionary Party

Sources:
- https://www.programiz.com/python-programming/dictionary
"""

# Comprehension


# Regular
customers = {'C1': 'widgetsforu', 'C2': 'starkindustries', 'C3': 'umbrellacorp'}

# Nested
customer_cases = {
    'C1': {'CA100': 'blahblahcase', 'CA101': 'blahblahcase'},
    'C2': {
        'CA103': 'blahblahcase',
        'CA104': 'blahblahcase',
        'CA105': 'blahblahcase',
        'CA106': 'blahblahcase'
    },
    'C3': {'CA107': 'blahblahcase'}
}

# Access elements
cust_id = 'C2'
print("Customer: " + str(customers[cust_id]) + " Cases: " + str(customer_cases[cust_id]))

# Add/Edit
customers['C4'] = 'initech'

# Report time
# 1) Provision customers
# 2) Report on cases


def _get_next_cust_id():
    """
    Returns next customer id
    :return: string
    """
    # print('Customer roster: ' + str(customers))
    key_list = []
    for customer_key in customers:
        stripped_prefix = customer_key[1:]
        # print('Adding key: ' + str(stripped_prefix))
        key_list.append(stripped_prefix)
    key_list.sort()
    last_id = int(key_list[-1])
    return 'C' + str(last_id + 1)


def add_customers(current_customers, new_customer_list):
    """
    Add customer and init case mgmt
    :param current_customers: list of strings, current customers appended to
    :param new_customer_list: list of strings, new customers
    :return: N/A
    """
    for new in new_customer_list:
        new_id = _get_next_cust_id()
        current_customers[new_id] = new
        customer_cases[new_id] = {}


add_customers(customers, ['wayne enterprises', 'acme'])
print('Customer Add Operation Complete.  New roster: ' + str(customers))


def case_report_report(customer_master, cases):
    """
    Report on all cases in system
    :param customer_master: Current customers
    :param cases: Each customer's cases
    :return: N/A
    """
    output = ['Reporter, CaseID, Description \n', ("-" * 10)]
    for reporter_id, reporter_cases in cases.items():
        for case_id, case_desc in reporter_cases.items():
            output.append(customer_master[reporter_id] + ' ' + case_id + ' ' + case_desc)

    print("\n".join(output))


case_report_report(customers, customer_cases)

'''
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
'''
