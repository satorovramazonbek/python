# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
# Doe = Person(name="Doe", age=18, gender="female")
# print(Doe.age,Doe.gender)

# class Oson_1:
#     a=5
#     def print_a(cls):
#         print(cls.a)
#
# Oson_1.print_a(Oson_1)

# class Oson_2:
#     a = 2
#     b = 3
#
#     def summa(cls):
#         print(cls.a + cls.b)

# class Oson_3:
#     a=4
#     def number(cls):
#         if cls.a>0:
#             print("musbat")
#         elif cls.a<0:
#             print("Manfiy")
#         else:
#             print("SOn nolga teng!!!")
#
# Oson_3.number(Oson_3)

# class Oson_4:
#     a=4
#     def number(cls):
#         if cls.a%2==0:
#             print("juft")
#         else:
#             print("Toq")
#
# Oson_4.number(Oson_4)


# class Oson_5:
#     a=4
#     b=3
#     def number(cls):
#         print(cls.a**cls.b)
#
# Oson_5.number(Oson_5)

#
# class My_class__6:
#     words = []
#     @classmethod
#     def add_word(cls, word):
#         cls.words.append(word)
# word = input("So'zni kiriting: ")
# My_class__6.add_word(word)
# print("So'zlar ro'yxati:", My_class__6.words)

# class My_class__7:
#     mydict = {}
#
#     @classmethod
#     def add_element(cls, key, val):
#         cls.mydict[key] = val
#
#     @classmethod
#     def update_element(cls, key, val):
#         cls.mydict[key] = val
# while True:
#
#     key = input("So'zni kiriting: ")
#     val = input("So'zni kiriting: ")
#     if key in My_class__7.mydict.keys():
#         My_class__7.update_element(key, val)
#
#     else:
#         My_class__7.add_element(key, val)
#     print("So'zlar ro'yxati:", My_class__7.mydict)

# class my_class_8:
#     numbers=[]
#     def compare_list(self,new_list):
class MyClass9:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def list1_max(self):
        return max(self.list1)

    def list2_max(self):
        return max(self.list2)

    def sum_of_two_max(self):
        max1 = self.list1_max()
        max2 = self.list2_max()
        print(f"Sum of maximums: {max1 + max2}")

my_instance = MyClass9([1, 5, 3], [7, 2, 9])
my_instance.sum_of_two_max()

