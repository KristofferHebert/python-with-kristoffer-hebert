def print_number(prefix, number):
    print prefix + str(number) + '\n'
    return 

# Create a list of numbers between 1 and 5
numbers  = [1,2,3,4,5]

# Loop over every number in numbers
# first variable is the namespace of numbers[index]
for number in numbers:
    print_number('Numbers: ', number)
    if(number == 5):
        print 'Numbers : COMPLETE \n'

# Range creates a list of numbers between 0 and 25
for number in range(25):
    print_number('Range: ', number)
    if(number == 25):
        print 'Range : COMPLETE \n'

# "Break" will break loops
count = 0
while True:
    count += 1
    print_number('Count: ', count)
    if(count > 10):
        print 'Count: COMPLETE \n'
        break

# You can treat while like an "if" statement
count = 0
while(count < 5):
    count += 1
    print_number('Count 2: ', count)
else:
    print 'Count 2: COMPLETE \n'

## Run in the terminal with this command
## python loop.py