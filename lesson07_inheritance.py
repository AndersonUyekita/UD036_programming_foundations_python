
# Creating a new Class to show an example of Class child
class Parent(): # My new Class
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")  # Just to keep tracking
        self.last_name = last_name  # Defining the Instance Variables
        self.eye_color = eye_color  #

    def show_info(self): # Creating a method
        print("Last Name: "+self.last_name) # This method return this infos last_name and eye_color.
        print("Eye Color: "+self.eye_color) #

class Child(Parent): # My Class child!!! <=======
    def __init__(self,last_name,eye_color,number_of_toys): # Atention to the new variable
        print("Child Constructor Called")   # Just to keep tracking
        Parent.__init__(self, last_name, eye_color) # Using the same values from the Parent
        self.number_of_toys = number_of_toys # NEW INSTANCE VARIABLE

    def show_info(self):                    # This method will overwrite the method from
        print("Last Name: "+self.last_name) # the Parents!!!
        print("Eye Color: "+self.eye_color) #
        print("Number of toys: "+self.number_of_toys)

# Creating a Parent object
ah_uyekita = Parent("uyekita","brown")
print(ah_uyekita.last_name) # Testing if works

# Creating a Child object
hitoshi_uyekita = Child("uyekita","dark_brown","iPad")

print(hitoshi_uyekita.last_name)       # Note that the two flags to keep track were printed.
print(hitoshi_uyekita.number_of_toys)  #

# Let's test the method show_info in Parent Class
ah_uyekita.show_info() # Must print those two info.

# Let's test the method show_info in Child Class
hitoshi_uyekita.show_info() # It's WORKS also!! =)
