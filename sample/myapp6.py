
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def print_size(self):
        print("{} by {} ".format(self.width, self.len))

my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()

class AlwaysPositive:
    def __init__(self, number):
        self.n = number
    
    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)

class Lion:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion) # クラス変数？

class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

x = 10
if x is None:
    print("x はNone :( ")
else:
    print("x はNoneじゃない")

x = None
if x is None:
    print("x はNone")
else:
    print("x はNoneじゃない：（")

class Square:
    def __init__(self, n):
        sqare_lis