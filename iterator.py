# def towarfanoi(n, from_rod, to_rod, aux_road):
#     if n == 1:
#         print("Move disk 1 from rod ", from_rod, "to rod", to_rod)
#         return
#     towarfanoi(n - 1, from_rod, aux_road, to_rod)
#     print(f"Move disk {n} from rod {from_rod} ro rod {to_rod}")
#     towarfanoi(n - 1, aux_road, to_rod, from_rod)
#
#
# n = int(input("enter number of disks: "))
# towarfanoi(n, 'a', 'c', 'b')


# l = [1, 2, 4, 5, 6, 6]
# l_iter=iter(l)
# print(next(l_iter))

# n1
# def tub_son():
#     n = 2
#     while True:
#         if all(n % i != 0 for i in range(2, int(n**0.5)+1)):
#             yield n
#         n += 1
#
# result = tub_son()
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

# from itertools import combinations
# n = input("belgini kiriting: ")
#
#
# # abc    abc acb cab cba bac bca n*(n-1)

# n2
# from itertools import *
#
# n = input("Enter a string: ")
# result = permutations(n, len(n))
#
# # Kombinatsiyalarni chop qilish
# for comb in result:
#     print(''.join(comb))
#


# n4
# from itertools import *
#
# my_list = []
#
# while True:
#     n = input("list emlementlarini kiriting : ")
#     if n == 'exit':
#         break
#     my_list.append(int(n))
#
# number = int(input("nechtadan guruhlash kerak : "))
# result = combinations(my_list, number)
#
# # Kombinatsiyalarni chop qilish
# for comb in result:
#     print(comb)

n = 2


def fibonachi():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


resul = fibonachi()
for i in range(50):
    print(next(resul))







