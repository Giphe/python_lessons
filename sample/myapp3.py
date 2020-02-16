import math
import random
import statistics
import keyword
import myapp2
import os
import csv

print(math.pow(2,3))
print(random.randint(0,100))

#mean
nums = [1, 5, 33, 12, 46, 33, 2]
print(statistics.mean(nums))

#median
print(statistics.median(nums))

#mode
print(statistics.mode(nums))

#keyword
print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))

myapp2.print_hello()

aA = os.path.join("Users", "kou", "MyCentOS", "python_lessons", "sample", "st.txt")

print(aA)

st = open("st.txt", "w", encoding="utf-8")
st.write("Pythonからこんにちは！")
st.close()

with open("self_taught.csv", "w", encoding="utf-8") as f:
    f.write("one,two,three\nfour,five,six")

#前の節で作成したファイルを読み込みます
with open("st.txt", "r", encoding="utf-8") as f:
    print(f.read())

my_list = []

with open("st.txt", "r", encoding="utf-8") as f:
    my_list.append(f.read())

print(my_list)

with open("st.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

#ここで開くファイルは
#前のコード例を実行して
#作られる、

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

a2 = input("ファイルに出力します：")

with open("st.txt", "w", encoding="utf-8") as f:
    f.write(a2)

with open("st2.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["Top Gun", "Risky Business", "Minority Report"])
    w.writerow(["Titanic", "The Revenant", "Inception"])
    w.writerow(["Traning Day", "Man on Fire", "Flight"])

with open("st2.csv", "w", newline='', encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["タカシ", "メグ", "ウトシ"])
    w.writerow(["ヴィシャス", "カンポ", "ペガサス"])
