def read_file(filename):
  try:
    file = open(filename, 'r')
    print 'Reading contents of', filename
    return file.read()
  except IOError as error:
    print '[IOERROR]', error
  except TypeError as error:
    print '[TYPE ERROR]', error
  except:
    print 'Something went wrong with', filename

def is_string(input):
    try:
      #isinstance checks type of object
      if(isinstance(input, str)):
        return input + ' is a string.'
      else:
        raise TypeError('\n[TYPE ERROR] Value is not string.')
    except TypeError as error:
      print error
      return ''

# Should return  true
print is_string('taco')

# Should return error
print is_string(['taco'])

# Should print text
print read_file('helloworld.txt')

# Should throw value error
print read_file('helloworld')

# Should throw IO error
print read_file(['helloworld'])


## Run in the terminal with this command
## python tryexcept.py7