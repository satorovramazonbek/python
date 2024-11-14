# def str_counter(strs):
#     diction = {}
#     for i in strs:
#         diction[len(i)] = i
#     return diction
#
# print(str_counter(["shaftoli", 'olma', 'nok','Ganiyev']))

# def merge_list(list1, list2):
#     diction = {}
#     for i in range(len(list1)):
#         diction[list1[i]] = list2[i]
#     return diction
#
# list_1 = ["a", "b", "c"]
# list_2 = [1, 2, 3]
# print(merge_list(list_1, list_2))


# contacts = {"Nodir":"+998918602711", "Laziz":"+998908002534"}
#
#
# def add_person():
#     person = input("Kontakt nomini kiriting: ")
#     number = input("Raqamni kiriting : ")
#     contacts[person] = number
#
#
# def remove_person(person):
#     person = input("Kontakt nomini kiriting: ")
#     del contacts[person]
#
#
# def update_person():
#     person = input("Kontakt nomini kiriting: ")
#     number = input("Raqamni kiriting : ")
#     contacts[person] = number
#
#
# while True:
#     command = input("""Amalni kiriting :
#         1: kontak qo'shish
#         2: kontakt nomerini yangilash
#         3: kontaktni o'chirish
#     """)
#     if command == 'exit':
#         print(contacts)
#         break
#     elif command == "1":
#         add_person()
#     elif command == "2":
#         update_person()
#     elif command == "3":
#         remove_person()
#     else:
#         print("Bunday komanda yo'q")

g