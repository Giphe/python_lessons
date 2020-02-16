text = '隴西《ろうさい》の李徴《りちょう》は博学｜才穎《さいえい》、天宝の末年、若くして名を虎榜《こぼう》に連ね、ついで江南尉《こうなんい》に補せられたが、性、狷介《けんかい》、自《みずか》ら恃《たの》むところ頗《すこぶ》る厚く、賤吏《せんり》に甘んずるを潔《いさぎよ》しとしなかった。'

# in_bracket = False
# for s in list(text):
#     if in_bracket:
#         if s == '》':
#             in_bracket = False
#         continue
#     if s == '《':
#         in_bracket = True
#         continue
#     print(s, end="")
# print()

# 正規表現
import re
# print(re.sub(r'《.*?》', '', text))

text = 'hanamogera'
m = re.search(r'moge', text)
# print(m)
m.span() #=> (4, 8)マッチした場所をタプルとして返す
s, e = m.span()
print(text[s:e]) #=> 'moge'