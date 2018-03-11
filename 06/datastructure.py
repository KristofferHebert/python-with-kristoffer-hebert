def print_item(message, item):
    print message, item

def number_of_methods(obj, obj_name):
    methods = set(dir(obj))
    print obj_name, 'has', len(obj), 'methods: ' 

# List
# Has different methods than a tuple, 
# Takes up more resources
# Values can be changed
example_list = [1,2,3,4,5]
number_of_methods(example_list, 'Example List')

for example in example_list:
    print_item('Example list:', example)
else:
    print ''

# Tuples
# Like lists but more memory effiecient 
# Can't be changed after defined
example_tuples = (1,2,3,4,5)
# Also valid syntax example_tules = 1,2,3,4,5
number_of_methods(example_tuples, 'Example Tuples')

for example in example_tuples:
    print_item('Tuples set:', example)
else:
    print ''

# Dictionaries
# Notice how they print out of order
example_dictionary = {"example": 1, "example2": 2, "example3": 3}
number_of_methods(example_dictionary, 'Example Dictionary')

for example in example_dictionary:
    print_item('Dictionary:', example)
else:
    print ''

# Sets
# Sets work like lists but have no duplicate values
# Notice how Richard and Suzy are only printed once

example_set = set(['Bob','Suzy','Jill','Richard','Richard','Suzy','Fred','Richard'])
number_of_methods(example_dictionary, 'Example Set')

for example in example_set:
    print_item('Example set:', example)
else:
    print ''

## Run in the terminal with this command
## python datastructure.py