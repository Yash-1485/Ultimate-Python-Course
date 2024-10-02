#  Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
class Animals:
    def __init__(self):
        print('Class Animals')
class Pets(Animals):
    def __init__(self):
        super().__init__()
        print('Class Pets')
class Dog(Pets):
    def __init__(self):
        super().__init__()
        print('Class Dog')
    @staticmethod
    def bark():
        print('Dog is barking...')
dog=Dog()
dog.bark()