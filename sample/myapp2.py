name = "Ted"

for character in name:
    print(character)

coms = ["GOT", "Narcos", "Vice"]
for show in coms:
    print(show) 

for i, new in enumerate(coms):
    new = coms[i]
    new = new = new.upper()
    coms[i] = new

print(coms)

tv = ["GOT", "Narcos", "Vice"]
boms = ["Arrested Development", "friends", "Always Sunney"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

for show in boms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

for i in range(1,11):
    print(i)

qs = ["What is your name?","What is your fav. color?","What is your quest?"]
n = 0
# while True:
#     print("Type q to quit")
#     a = input(qs[n])
#     if a == "q":
#         break
#     n = (n + 1) % 3
#     print(n)

y = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]

for data in y:
    i = y.index(data)
    print(data + "は" + str(i) + "番目の要素です。")

x = 0
while x <= 50:
    if x >=25:
        print(x)
        x += 1
        continue
    x += 1

# while True:
#     a = input("アルファベットを入力してください。")
#     if a == "a" or a == a.upper():
#         print("correct!")
#         break
#     print("miss!")

def print_hello():
    print("hello!")

