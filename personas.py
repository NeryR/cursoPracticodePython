
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('Hello motherfukcer, my name is {} and i have {} years old'.format(self.name, self.age))

if __name__ == '__main__':
    person = Person('Nery', 24)

    print('Age: {}'.format(person.age))
    person.say_hello()