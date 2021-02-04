# Creating a class named MyClass using camel stlye
class MyClass:
    
    # defining a method 
    # Methods allow objects to perform actions.
    def first_method(self):
        return "This is the first method"
    
    # Method that returns a given list 
    def return_list(self, input_list):
        return input_list

# Creating an instance of  MyClass
# assigning it to the variable my_instance
my_instance = MyClass()

# apply the first method to my_instance
result_1 = my_instance.first_method()

# apply the return_list method to my_instance
result_2 = my_instance.return_list([1,2,3,4])

print()
print(result_1)
print()
print(result_2)
print()
print(type(my_instance))

class MyList:

    # defining a the init constructor to store attributes 
    def __init__(self, initial_data):

        # Creating attribute to store data
        self.data = initial_data
        
# inatiating MyList and storing the list into the attribute data 
# inside our object
my_list = MyList([1,2,3,4,5])

# usinging dot notation to access attribute 
print(my_list.data)


class MyList:
    
    def __init__(self, initial_data):
        
        self.data = initial_data
        
        self.length = 0
        for item in self.data:
            self.length += 1
    
    def appendd(self, new_item):
        self.data = self.data + [new_item]
        self.length += 1
        
        
my_list = MyList([1,2,3,4,5])   

print(my_list.data)

my_list.appendd(6)

print(my_list.data)
print(my_list.length)

''' 
We've created a MyList class which stores a list at the point of instantiation using the init constructor.
We stored that list inside an attribute of MyList called data.
We've created a method — MyList.appendd() — which mimics the behavior of list.append().
'''