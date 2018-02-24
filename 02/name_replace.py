## Import is used to import libraries within python
import random

## "def" represents a function in python.
def name_replace(message, name):
    ## Use .replace to replace specific text in string.
    return message.replace("[name]", name)

## Scrambles texts using random character in a string.
def message_mangle(message):
    ## store length of string using len
    message_length = len(message)
    ## used to cache message output
    output = ""
    ## will fire until message_length is 0
    while(message_length):
        message_length -= 1
        random_number = random.randint(0, message_length) 
        ## Append random character from message to output
        output += message[random_number]
    return output 

## Call a function using it's name
## Pass arguments to () brackets
message = name_replace("My name is [name].","Jeff")

## Print outputs contents of variables to the terminal
print(message)

## Mangle message
message = message_mangle(message)

## Output results of mangle
print(message)

## Run in the terminal with this command
## python name_replace.py 

