from classes.user import User

# The syntax for extending an existing class is Child(Parent):
class Admin(User):
   __admin = True
   # Overide existing method of details
   # Adds role to Print output
   def details(self):
        # print details of user
        print "role: Admin"
        print "email: " + self.email
        print "password hash: " + self.passwordHash
        print "id: " + str(self.id)
   # Overide existing method of is_admin
   def is_admin(self):
       return self.__admin

# Create new user based on User class
user = User('test@test.com', 'examplepassword')
# Create new user based on Admin class
admin = Admin('admin@admin.com', 'examplepassword2')

# Print user details like email, password, id
print "Is admin?: " + str(user.is_admin())
print "User Details:"
user.details()

# Print admin details like role, email, password, id
print "\nAdmin Details:"
admin.details()

print "Is admin?: " + str(admin.is_admin())

## Run in the terminal with this command
## python admin_class.py