class Person:
    def __init__(self, name, age):
        self.name = name  # 'self.name' refers to the attribute 'name' of the instance
        self.age = age    # 'self.age' is the attribute 'age' of the instance

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
person1 = Person("Alice", 30)
print(person1.greet())  # Outputs: Hello, my name is Alice and I am 30 years old.
