# import random as random
#
# a = random.randint(1, 101)
# count = True
# while count:
#     b = int(input("1dan 100 gacha sonni taxmin qiling"))
#     if a == b:
#         print("Barakalla siz uylangan sonni topdingiz")
#         break
#     elif a < b:
#         print("O'ylagan soningiz katta")
#     elif a>b:
#         print("O'ylagan soningiz kichik")
# a = 1
# while a < 6:
#     s = ""
#     for i in range(a):
#         s += str(a)
#     print(s)
#     s=""
#     a = a + 1
#
# b=0
# a= input()
# c=0
# while c<len(a):
#     b+=int(a[c])
#     c+=1
# print(b)

# lst = [123, 125, 152, 22, 556, 535, 960, 11, 111, 1522]
# lst.remove(max(lst))
# print(max(lst))
#
# ranglar =['qizil', 'sariq', 'yashil']
# while True:
#     rang = input("Svetofor rangini kiriting: ")
#     if rang in ranglar:
#         print("Rahmat, to'g'ri keladi")
#         break
#     else:
#         print("Xato rang!")


# import random
# r =random.randint(1,11)
# while True:
#     numb = int(input("Tasodifiy sonni kiriting: "))
#     if numb == r:
#         print("Siz sonni topdiz")
#         break
#     else:
#         print("Noto'g'ri qayta urinib ko'ring")
#

# friends =[]
# while True:
#     name = input("Do'stingiz ismini kiriting")
#
#     if name.lower() == 'stop':
#         print(friends)
#         break
#     friends.append(name.capitalize())

usd=12600
while True:
    sum=(input("pulni so'mdagi qiymatini kiriting: "))
    if sum=='exit':
        print("Dastur yopildi")
        break
    print(int(sum)/usd, "USD")









