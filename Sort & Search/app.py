# array to hold a list of employees
employees = ['oscar', 'jim', 'dwight', 'phyllis', 'angela', 'andy', 'kevin', 'erin', 'toby', 'stanley', 'creed']
target = 'kevin'

# a function to perform linear search
def linear_search(list=[], tar=str):
    for i in range(len(list)):
        if list[i] == target:
            print(tar + ' found')
            return True
        else:
            i = i + 1
    print(tar + ' not found')
    return False

linear_search(employees, target)