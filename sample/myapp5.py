# pop = []   # 洋楽ポップソングを保存するリスト
# jpop = []  # 邦楽ソングを保存するリスト

# def collect_songs():
#     song = "曲名を入力してください。"
#     ask = "p か j のどちらかを入力してください。qで終わります:"

#     while True:
#         genre = input(ask)
#         if genre == "q":
#             break
        
#         if genre == "p":
#             p = input(song)
#             pop.append(p)

#         elif genre == "j":
#             j = input(song)
#             jpop.append(j)

#         else:
#             print("不正な値です。")
#         print("pop songs: ", pop)
#         print("jpop songs: ", jpop)

# collect_songs()

class Orange:
    def __init__(self, w, c):
        """weight(重さ)はグラム"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        """temp(温度)は摂氏"""
        self.mold = days * temp

# class Rectangle:
#     def __init__(self, w, l):
#         self.width = w
#         self.len = l

#     def area(self):
#         return self.width * self.len

#     def change_size(self, w, l):
#         self.width = w
#         self.len = l

# rectangle = Rectangle(10, 20)
# print(rectangle.area())

# rectangle.change_size(20, 40)
# print(rectangle.area())
# or1 = Orange(10, "dark orange")
# or1.weight = 100
# or1.color = "light orange"

# print(or1.weight)
# print(or1.color)

# or2 = Orange(8, "dark orange")
# or3 = Orange(14, "yellow")
orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)

class Apple:
    def __init__(self, s, w ,pl, pr):
        self.sweet = s
        self.weight = w
        self.place = pl
        self.price = pr
        print('Created!')

# アクセス制限

class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self.private = "unsafe"
    
    def public_method(self):
        # client が使ってもよい
        pass # pass文は、文が必須な構文で何もしない場合に使う

    def _unsafe_method(self):
        # client は使うべきじゃない
        pass # pass文は、文が必須な構文で何もしない場合に使う

print(type("Hello World"))

# ポリモーフィズムなしで様々な形状を描画する場合
# shapes = [tr1, sq1, cr1]
# for a_shape in shapes:
#     if isinstance(a_shape, Triangle):
#         a_shape.draw_triangle()
#     if isinstance(a_shape, Square):
#         a_shape.draw_square()
#     if isinstance(a_shape, Circle):
#         a_shape.draw_circle()

# #ポリモーフィズムを実装して描画する場合
# shapes = [tr1, sw1, cr1]
# for a_shape in shapes:
#     a_shape.draw()

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def print_size(self):
        print("{} by {}".format(self.width, self.len))

# my_shape = Shape(20, 25)
# my_shape.print_size()

class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))

a_square = Square(20, 20)
a_square.print_size()
    
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name) # [犬インスタンス].[owner][飼い主名]

# Shapeクラス
class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a Shape")

# Rectangleクラス
class Rectangle(Shape):
    def __init__(self, w, l):
        self.weight = w
        self.length = l
        self.calc = (w + l) * 2

    def calculate_perimeter(self):
        print("Rectangle = {}".format(self.calc))
    
    def what_am_i():
        pass

# Squareクラス
class Square(Shape):
    def __init__(self, w, l):
        self.weight = w
        self.length = l
        self.calc = w * l

    def calculate_perimeter(self):
        print("Square = {}".format(self.calc))

    def change_size(self, w, l):
        self.weight = w
        self.length = l
        self.calc = w * l

    # def what_am_i(self):
    #     pass

lect = Rectangle(20, 30)
squa = Square(20, 30)

lect.calculate_perimeter()
squa.calculate_perimeter()
squa.change_size(40, 50)
squa.calculate_perimeter()
squa.what_am_i()

class Horse:
    def __init__(self, hn, br, r):
        self.horseName = hn
        self.breed = br
        self.rider = r

class Rider:
    def __init__(self, n):
        self.name = n

name = Rider("Mickel")
horse = Horse("Max", "greatHorse", name)
print("騎手は{},彼は{}に乗っている".format(horse.rider.name, horse.horseName))

