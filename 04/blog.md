# Extending Classes in Python
Learn about extending existing Classes, and importing classes from files this chapter.

## Overview
Classes in Python allow you to group related variables and function inside reusable code. The syntax for classes is "class Classname:" Each class should have a __init__ function that is fired every time a class is instantiated. You instantiate a class with class = Classname(argument1, argument2).  

Within Classes you don't want every variable to be accessible. For example, you wouldn't want a class of User to be able to change it's self to have the permissions of an Admin. People could use this to maliciously harm your website. Private variables have the syntax of "__variable" and are usually grouped with the variables above "__init__".

Hashlib is a hashing library within Python. It can be used encrypt sensitive data like passwords. You should never store passwords in the database as plain text. Use "import hashlib" to import the library.

Time is a Python library used for time related functions. Use "import time" to import the library. 
 
## Admin class Code
https://gist.github.com/KristofferHebert/227cf115c745b2cf8b8f418bbe926f42

## Summary
- Extending Class syntax is "class Classname(ParentClass):"
- import a class from file via "from folder_name.file_name "
- Use a getter function to access these private __variables
- Instantiate a class with class = Classname(argument1, argument2)

### Next Steps
Stay tuned for the next tutorial!

### Want to start from the beginning?
https://medium.com/@khbrt/python-with-kristoffer-hebert-5cce2fa4e6ab

### Have suggestions? Make a pull request!
https://github.com/KristofferHebert/python-with-kristoffer-hebert