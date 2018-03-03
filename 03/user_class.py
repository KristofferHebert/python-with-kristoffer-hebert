# include python library for encrypting values 
import hashlib
# include library for time
import time

class User:
    # creates unique id based on epoch time
    id = int(round(time.time() * 1000))
    # Adding '__' to a variable obscures the variable
    __admin = False
    email = ''
    passwordHash = ''
    # __init__ is called each time a new User is created
    def __init__(self, email, password):
        # self refers to variables within a class
        # self is usually the first argument of a function within a class
        self.email = email
        # self also refers to functions within a class
        self.passwordHash = self.hash_password(password)
    def hash_password(self, password):
        # function is used to create a password hash via sha256
        hash = hashlib.sha256(password)
        return hash.hexdigest()
    def verify_password(self, password):
        # hash password
        # returns True or False
        return self.passwordHash == self.hash_password(password)
    def details(self):
        # print details of user
        print "email: " + self.email
        print "password hash: " + self.passwordHash
        print "id: " + str(self.id)
    def is_admin(self):
        # Get value of __admin
        return self.__admin

# Create new user based on User class
user = User('test@test.com', 'examplepassword')

# Print user details like email, password, id
user.details()

# Should return AttributeError: User instance has no attribute '__admin'
# print user.__admin

print ""

# Validate Password
print "Your password is 'examplepassword': " + str(user.verify_password('examplepassword'))

# Check if user is an admin
print "User is an Admin? " + str(user.is_admin())

## Run in the terminal with this command
## python user_class.py