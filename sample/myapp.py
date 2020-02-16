# モジュール

import calendar

# import mypackage.user as mymodule
lists =[]

rap = ["蟹江・ウェスト","ジェイ・ｚ","エミネム","ナズ"]
rock = ["ボブ・ディラン","ザ・ビートルズ","レッド・ツェッペリン"]
djs = ["ぜっず・ですと", "ティエスト"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

#print(lists)

rap = lists[0]
#print(rap)

rap.append("県土リックサマー")
# print(rap)
# print(lists)

locations = []

la = (34.0522, 188.2437)
chicago = (41.8781,87.6298)

locations.append(la)
locations.append(chicago)

# print(locations)

""" line one
    line two
    line three
"""

print(calendar.prcal(2019))

str = "we hold these truths..."
print(str.upper())

str2 = "SO IT GOES"
print(str2.lower())
print(str2.capitalize())

# what = input("何が：")
# when = input("いつ：")
# where = input("どこで：")
# do = input("どうした：")

r = "{}は{}に{}で{}。"
# print(r.format(what, when, where, do))

str3 = "水たまりを飛び越えたんだ。3メートルもあったんだぜ!"
print(str3.split("。"))


first_three = "abc"
result = "+" .join(first_three)
print(result)

words = ["The", "fox", "jumped", "over", "the", "fense", "."]
one = " ".join(words)
print(one)

s = one.strip()
print(s)

equ = "All animals are equal."
equ = equ.replace("a", "@")
print(equ)

i = "animals".index("m")
print(i)

bl = "Cat" in "Cat in the seat"
print(bl)

print("line1\nline2\nline3")

ivan = "死の代わりに一つの光があった"
print(ivan[0:16])
print(ivan[6:16])

kamu = "カミュ"
print("{},{},{}".format(kamu[0],kamu[1],kamu[2]))

# input1 = input("入力１：")
# input2 = input("入力２：")

# str4 = "私は昨日{}を書いて、{}に送った！"
# print(str4.format(input1, input2))

str5 = "aldous Huxley was born in 1894"
print(str5.capitalize())

words[5] = words[5] + words[6]
two = " ".join(words)
print(two)

str6 = "A screaming comes across the sky."
three = str6.replace("s", "$")
print(three)

str7 = "hemingway"
print(str7.index("m"))

str8 = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
i1 = str8.index("、")
str9 = str8[:i1]
print(str9)

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]

i = 0
nl = []
for l1 in list1:
    bi = l1 * list2[i]
    nl.append(bi)
    i += 1
print(nl)