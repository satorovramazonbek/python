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


# from collections import Counter
# counter_list = [2, 1, 1, 1]
# def counter():
#     count = Counter(counter_list)
#     print(count)
# counter()


students = {"Akmal": 94, "Tohir": 55, "Nodir": 76, "Zafar": 80}  # -> {"Zafar":80, "Nodir":76}
max_ball_students_dict = {}

def max_persons(max_score):
    for key, value in students.items():
        if max_score == value:
            max_ball_students_dict[key] = value
            return key


def max_ball_students():
    for i in range(2):
        max_score = max(students.values())
        print(max_score)
        key = max_persons(max_score)
        del students[key]

    print(max_ball_students_dict)

max_ball_students()
