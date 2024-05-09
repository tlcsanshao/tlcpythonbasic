#! /usr/bin/python3
import sys

authorname = 'sanshao'


def sayHello(name):
    print('sayHello to ' + name)


def getInputName(name):
    return 'input name is ' + name


class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def describeMe(self):
        return "my name is " + self.name + ",my age is " + str(self.age) + ",my sex is " + self.sex


if __name__ == '__main__':
    name = 'sanshao'
    length = len(sys.argv)
    if length > 1:
        name = sys.argv[1]
    sayHello(name)
    value = getInputName(name)
    print(value)

    person = Person(name, 18, 'male')
    print(person.describeMe())

