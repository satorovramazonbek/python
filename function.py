# funksiyaning asosiy vazifasi kodlarni  kodlarni to'g'ri guruhlash va abstraksiya yani kodni kerakli paytda chaqirib ishlatish
# def sanoq():
#     for i in range(6, 40, 6):
#         if i % 2 == 0 and i % 3 == 0:
#             print(i)
#
#
# sanoq()

# 1. "user_data" funksiyasini elon qilasizlar.
# Funksiyani 3 ta parametri bor (first_name, last_name, age).
# Input orqalik ism, familiya va yoshni kiritamiz.
# va bu bu qiymatlarni "user_data" funksiyasini chaqirib argumentlariga beramiz.
# "user_data" funksiyasi bu (first_name, last_name, age) o'zgaruvchilarni qiymatini
#
#   Ism: Alisher
#   Familiya: Olimov
#   Yosh: 27
#
# ko'rinishiga print qilib bersin.


# def user_data(first_name, last_name, age):
#     return f"""
#       Ism: {first_name}
#       Familiya: {last_name}
#       Yosh: {age}
#     """
#
# print(user_data('Alisher',"Soliyev", 29))


# 2. "find_max" funksiyasini elon qilasizlar.
# Funksiyani 3 ta parametri bor (a, b, c).
# Input orqalik 3 ta son kiritamiz.
# va bu sonlarni "find_max" funksiyasi chaqirib argumentlariga beramiz.
# "find_max" funksiyasini bu (a, b, c) o'zgaruvchilardan eng kattasini
# topib print qiladi.

#   Eng katta son - A = 10
#   yoki
#   Eng katta son - A va B = 10
#   yoki
#   Eng katta son - A va B va C = 10
# def find_max(a, b, c):
#     max = a
#     if max < b and b > c:
#         max = b
#         return f"Eng katta son - B = {b}"
#     elif max < c and c > b:
#         max = c
#         return f"Eng katta son - C = {c}"
#     else:
#         return f"Eng katta son - A = {a}"
#
# print(find_max(12, 15, 1))


# 3. "find_letter_count" funksiyasini elon qilasizlar.
# Funksiyani 2 ta parametri bor (word, letter).
# Input orqalik so'z kiritamiz, keyin esa shu so'zda qidirmoqchi bolgan so'zimizni kiritamiz.
# va bu qiymatlarni "find_letter_count" funksiyasini chaqirib argumentlariga beramiz.
# "find_letter_count" funksiyasi bu (word, letter) o'garuvchilardan foydalanib
# "word" da "letter" nechi martda qatnashganini print qilsin.
#
#   "Programing" so'zida "r" dan 2 ta.

# def find_letter_count(word, letter):
#     return word.count(letter)
#
# word=input()
# letter=input()
# print(find_letter_count(word,letter))


# 4. "list_sum" funksiyasi elon qilasizlar.
# Funksiyani 1 ta pametrni bor (myList).
# "myList" funksiyasini chaqirib unda argumentini berasizlar.
# uni ichida esa myList elementlarini yig'indisini print qilasizlar.
#   Listning elementlar yig'indisi = 32

# def list_sum(mylist):
#     sum = 0
#     for i in mylist:
#         sum+=i
#     print(sum)
#
# mylist=[123,124,235,11,11]
# list_sum(mylist)

# 5. daraja(a, b) - bu funksiya a ni b darajasini print qilsin.

# def daraja(a,b):
#     print(a**b)
# daraja(2,6)

# 6. daraja4(a, b, c, d) - bu funksiya a ni b, c va d chi darajasini print qilsin.
# def daraja4(a, b, c, d):
#     print(a ** b, ' ', c ** d)
# daraja4(2,4,5,6)

# 7. digit_count_and_sum(word) - bu funksiya "word" ni ichidagi raqamni aniqlab ularni yig'indisini va nechtaligini print qilsin.

# def digit_count_and_sum(word):
#     sum = 0
#     count = 0
#     for i in word:
#         if i.isdigit():
#             sum += i
#             count += 1
#     print(f"Yig'indisi {sum} soni {count}")
# digit_count_and_sum("idsjfiesfjeifj12i3uj12iubj124iubj5ijubijdsf")
# 8. add_right(a, b) - bu funksiya a sonini o'ng tomoniga b sonini birlashtirib qoysin va print qilsin.

# def add_right(a,b):
#     return str(a)+str(b)
# print(add_right(12,22))

# 9. add_left(a, b) - bu funksiya a sonini chap tomoniga b sonini birlashtirib qoysin va print qilsin.
# def add_left(a,b):
#     return str(b)+str(a)
# print(add_left(123,543))

# 10. work_with_list(a) - bu funksiya a listdan eng kichik sonni topib list elementlariga ko'paytirib qiymatini o'zgartiradi va listni print qilsin.

# def work_with_list(a):
#     return min(a)
#
#
# a = [123, 433, 455, -111, -4, 0]
# print(work_with_list(a))

# 11. big_sales(sales) funksiyasini yarating.
# sales bu dictionary:
# {
#   "yanvar": 12000,
#   "mart": 6000,
#   "aprel": 15000,
#   "sentabr": 9000,
#   "dekabr": 10000,
# }
# qaysi oyda eng ko'p sotuv bolgan bo'lganini return qilsin.

# def big_sales(sales):
#     return max(sales.keys())
#
#
# sale = {
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }
# print(big_sales(sale))

# 12. min_max(numbers, max_num, min_num) max_num numbers ichigagi eng katta sonmi yoki yoqmi shuni aniqlang,
# min_num numbers ichigagi eng kichik sonmi yoki yoqmi shuni aniqlang
# def min_max(numbers, max_num, min_num):
#     if max_num not in numbers:
#         print(f"{max_num} bundan son mavjud emas")
#         if min_num not in numbers:
#             print(f"{min_num} bundan son mavjud emas")
#     else:
#         if max_num == max(numbers):
#             print(f"{max_num} {numbers} list ichidagi eng katta son")
#         else:
#             print(f"{max_num} {numbers} list ichidagi eng katta son emas")
#         if min_num == min(numbers):
#             print(f"{min_num} {numbers} list ichidagi eng kichik son")
#         else:
#             print(f"{min_num} {numbers} list ichidagi eng kichik son emas")
#
# number = [12, 124, 15, 255, 4, 2, 4, 4, 55]
# min_max(number, 255, 2)


# 13. expensiveProduct(products) - funksiyadagi products - list.
# Unga products sifatida [
#   {
#     "name": "Iphone X",
#     "price": 600
#   },
#   {
#     "name": "Iphone 12",
#     "price": 1500
#   },
#   {
#     "name": "Samsung Note 9",
#     "price": 800
#   },
#   {
#     "name": "Samsung S10",
#     "price": 1100
#   },
# ] shunaqa qiymat beriladi.
# Eng qimmat telefon nomini print qilib bersin bu funksiya.

def expensiveProduct(products):
    maxproduct = products[0]["price"]
    productname=products[0]["name"]
    # print(maxproduct)
    for i in products:
        if maxproduct < i["price"]:
            maxproduct = i["price"]
            productname = i["name"]
    print(productname)


product = [
    {
        "name": "Iphone X",
        "price": 600
    },
    {
        "name": "Iphone 12",
        "price": 1500
    },
    {
        "name": "Samsung Note 9",
        "price": 800
    },
    {
        "name": "Samsung S10",
        "price": 1100
    },
]

expensiveProduct(product)