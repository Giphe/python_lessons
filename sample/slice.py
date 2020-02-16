#スライス

# scores = [40, 50, 70, 90, 60]
# print(scores[1:4]) #50 70 90
# print(scores[:2]) #40 50 
# print(scores[3:]) #90 60 
# print(scores[-3:]) #70 90 60 

s = "hello"
print(s[1:4])

#セット

# # a = set([5, 4, 8, 5])
# a = {5, 3, 8, 5}
# print(a)
# print(5 in a) # true
# a.add(2)
# a.remove(3)
# print(a)
# print(len(a))


a = {1, 3, 5, 8}
b = {3, 5, 8, 9}
print(a | b)
print(a & b)
print(a - b)

sales = {"taguchi":200, "fkoji":400}
# print(sales["taguchi"])
# sales["taguchi"] = 300
# sales["dotinstall"] = 500
# del(sales["fkoji"])
# print(sales)

# for key, value in sales.items():
#     print("{0}:{1}".format(key,value))

# イテレータ

# scores = [40, 50, 70, 90, 60]
# it = iter(scores)
# print(next(it))
# print(next(it))
# print("hello")
# print(next(it))

# for score in scores
# print(score)

def get_infinite(): # ジェネレータ
    i = 0
    while True:
        yield i * 2
        i += 1

g = get_infinite()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#docstring(ドキュメンテーション文字列)
def add(x, y):
    """
    Returns x + y.
    :param x: int.
    :param y: int.
    :return: int sum of x and y.
    """
    return x + y

print(add(5, 4))

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")

print(random)
print(random[0])
print(random[1])

item = random.pop()
print(item)

print(random)
print(random)
print(len(random))

random.append("C")

guess = input("何でしょう？入力してください：")

if guess in random:
    print("あたり")
else:
    print("はずれ")




