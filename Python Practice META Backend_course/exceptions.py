class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

p = Person("John", 30)
print(p)  # Output: John, 30 years old
# age = int(input("Enter your age: "))
# if age < 0:
#     raise ValueError("Age cannot be negative!")
# else:
#     print("Your age is:", age)

# # try:
# #     print(10)
# # except ZeroDivisionError:
# #     print('cannot divide  by zero')
# # else:
# #     print('divison was succesfull')

