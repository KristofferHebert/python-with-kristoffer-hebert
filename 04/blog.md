# Extending Classes in Python
Learn about extending existing Classes, and importing classes from files this chapter.

## Overview
You can extend existing Python classes using the "class Classname(ParentClass):" syntax. By extending an existing class, you are able to reuse existing code. You can override class functions by using the same namespace for variables and class functions.

You can import existing classes from separate files using the “from folder_name.file_name import ClassName”. If the class file exists in a separate folder, create __init__.py file inside that folder. Inside that file add an array of files names a variable called __all__. Should look like __all__ = [“file, file2, file3”]

 
## Admin class Code
https://gist.github.com/KristofferHebert/227cf115c745b2cf8b8f418bbe926f42

## Summary
- Extending Class syntax is "class Classname(ParentClass):"
- import a class from file via "from folder_name.file_name import ClassName"

### Next Steps
Stay tuned for the next tutorial!

### Want to start from the beginning?
https://medium.com/@khbrt/python-with-kristoffer-hebert-5cce2fa4e6ab

### Have suggestions? Make a pull request!
https://github.com/KristofferHebert/python-with-kristoffer-hebert