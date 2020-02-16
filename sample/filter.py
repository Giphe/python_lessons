# filter(関数, イテレータ)

def is_even(n):
    return n % 2 == 0

# print(list(filter(is_even, range(10))))

print(list(filter(lambda n: n % 2 == 0, range(10))))

# 内包表記

# 0 - 9
# print([i for i in range(10)])
# print([i * 3 for i in range(10)])
# print([i * 3 for i in range(10) if i % 2 == 0])
# print((i * 3 for i in range(10) if i % 2 == 0))
print(i * 3 for i in range(10) if i % 2 == 0) # ジェネレータ
print({i * 3 for i in range(10) if i % 2 == 0}) # 集合型

def f(x):
    return x * 2

result = f(2)
print(result)

# age = input("Enter your age:")
# int_age = int(age)
# if int_age < 21:
#     print("You are young!")
# else:
#     print("Wow, you are old!")

# n = input("type a number:")
# n = int(n)
# if n % 2 == 0:
#     print("n is even.")
# else:
#     print("n is odd.")

# n = input("type a number:")
# n = int(n)
# if n % 2 == 0:
#     print("n is even.")
# else:
#     print("n is odd.")

# n = input("type a number:")
# n = int(n)
# if n % 2 == 0:
#     print("n is even.")
# else:
#     print("n is odd.")

def even_odd():
    n = input("type a number:")
    n = int(n)
    if n % 2 == 0:
        print("n is even.")
    else:
        print("n is odd.")

# even_odd()
# even_odd()
# even_odd()

# def f1(x=2):
#     return x ** x

# print(f1())
# print(f1(4))

# def add_id(x,y = 10):
#     return x + y
# result = add_id(2)
# print(result)

# x = 1
# y = 2
# z = 3

# def f2():
#     print(x)
#     print(y)
#     print(z)

# f2()

x = 100

def f3():
    global x
    x += 1
    print(x)

f3()
print(x)

a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
# print(a / b)

try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero.")