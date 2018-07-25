# class MyClass:
#     """ A simple example class """
#     i = 12345
#
#     def f(self):
#         print('hello world')
#         return 'Hello!'
#
# print(MyClass.i)
# print(MyClass.f('self'))


# class Test:
#     """Test class"""
#
#     def __init__(self, temp1, temp2):
#         self.x = temp1
#         self.y = temp2
#
# m = Test(2,4)
# print(m.x, m.y)


# class Test1:
#     """Test class"""
#
#     def __init__(self, temp1, temp2):
#         self.x = temp1
#         self.y = temp2
#
# m = Test(5,6)
# print(m.x, m.y)

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def addTricks(self, trick):
        self.tricks.append(trick)

d  = Dog('Fibo')
e  = Dog('Buddy')

d.addTricks('Rollover')
d.addTricks('PlayDead')
e.addTricks('turnAround')

print(d.tricks)
print(e.tricks)
