# Reading files in Python

## Overview
You can read files with the “open(file_name)”. It would be wise to wrap the statement in a try catch. This way your program can continue if an error occurs.

You can read from CSV files using the CSV library. “csv.DictReader” allows you to transform the cvs data into a collection of key value pairs.

You can pass arguments to a Python file via sys library. The first argument is the name of the Python file. The zero index of “python file_reader.py demographic.py” would return “file_reader.py”

In Python, a try catch statement is used for error handling. It is similar to other C based languages. This allows a program to continue after an error has occurred.

## Loop Code
https://gist.github.com/KristofferHebert/bde066bf76efb2b88e9f172540accf30

## Summary
- "Open("file_name")" is the syntax for reading files in Python.
- A "try catch" statement allows a program to continue after an error occurs.
- "Sys.argv" contains every argument passed the python file. The first index is the name of the python file.

### Next Steps
Stay tuned for the next tutorial!

### Want to start from the beginning?
https://medium.com/@khbrt/python-with-kristoffer-hebert-5cce2fa4e6ab

### Have suggestions? Make a pull request!
https://github.com/KristofferHebert/python-with-kristoffer-hebert