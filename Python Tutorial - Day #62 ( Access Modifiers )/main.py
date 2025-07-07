class Employee:
    def __init__(self):
        self.name = "Will"  # Public


class Employee2:
    def __init__(self):
        self._name = "John"  # Protected (shouldn't be used outside subclasses)

    def intro(self):
        print(f"My name is {self._name}")


class Employee3:
    def __init__(self):
        self.__name = "Jack"  # Private (Shouldn't be used outside the class)

    def get_name(self):
        return self.__name  # Provide a public method to access private variable


class Son(Employee2):
    def __init__(self):
        super().__init__()  # Call parent constructor to initialize _name
        print(self._name)   # Accessing protected attribute from parent


a = Employee()
print(a.name)  # Will

b = Employee2()
b.intro()  # No error, calls the method properly

d = Son()
print(d._name)  # Accessing protected attribute from child instance (not recommended but works)

# c = Employee3()
# print(c.__name)  # This will raise an AttributeError because __name is private

c = Employee3()
print(c.get_name())  # Correct way to access private variable via public method
