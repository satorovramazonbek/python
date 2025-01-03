# # 1 instance method tasks
#
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def deposite(self, deposite):
#         self.balance = self.balance + deposite
#
#     def withdraw(self, money):
#         if money <= self.balance:
#             self.balance = self.balance - money
#         else:
#             print("No equal money")
#
#     def check(self):
#         print(self.balance)
#
#
# bank = BankAccount(5000)
# bank.deposite(3000)
# bank.withdraw(1000)
# bank.check()

# class Rectangular:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         print(self.width * self.length)
#
#     def perimetr(self):
#         print(2 * (self.width + self.length))
#
#     def is_square(self):
#         print(True if self.length == self.width else False)
#
#
# rect = Rectangular(10, 0)
# rect.is_square()


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.grade = [10, 60, 40]
#
#     def add_grade(self, amount):
#         self.grade.append(amount if amount >= 0 and amount <= 100 else print("please enter ball in this border"))
#
#     def calculate_average(self):
#         print(sum(self.grade) / len(self.grade) if len(self.grade) > 0 else print("you don't have balls"))
#
#     def print_summary(self):
#         print("Totals balls: \n", self.grade)
#
#
# ali = Student('ali', 18)
# ali.add_grade(100)
# ali.calculate_average()
# ali.print_summary()


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         print(3.14 * (self.radius) ** 2)
#
#     def circumference(self):
#         print(2 * 3.14 * self.radius)
#
#     def diametr(self):
#         print(self.radius * 2)
#
#
# oylana = Circle(2)
# oylana.area()
# oylana.circumference()
# oylana.diametr()

# class Book:
#     def __init__(self, title, author, current_page):
#         self.title = title
#         self.author = author
#         self.current_page = current_page
#
#     def open(self, page):
#         self.current_page = page
#
#     def turn_page(self):
#         self.current_page += 1
#
#     def restart(self):
#         self.current_page = 1
#


# Class Method Tasks:

# class Dogs:
#     order = 0
#
#     def __init__(self, name):
#         self.name = name
#         Dogs.order += 1
#
#     @classmethod
#     def get_order(cls):
#         return cls.order
#
#
# dog1 = Dogs("Buddy")
# dog2 = Dogs("Charlie")
# dog3 = Dogs("Max")
#
# print(Dogs.get_order())

#
# class Computer:  # comp count=?
#     def __init__(self, comp_name):
#         self.name = comp_name
#         self.comps = ['lg']
#     def add_comp(self,name):
#         self.comps.append(name)
#     def total_computer(self):
#         print(len(self.comps))
#
# asus=Computer('asus')
# asus.add_comp('asus')
# asus.total_computer()


# class Employee:  # emp count=?
#     def __init__(self, emp_name):
#         self.name = emp_name
#         self.emps = ['ali']
#     def total_computer(self,name):
#         self.emps.append(name)
#         print(len(self.emps))
#
# asus=Employee('asus')
# asus.total_computer('asus')
#
# class Television:
#     average_screen_size = 0
#     total_televisions = 0
#
#     def __init__(self, brand, screen_size):
#         self.brand = brand
#         self.screen_size = screen_size
#         Television.total_televisions += 1
#         Television.update_average_screen_size(screen_size)
#
#     @classmethod
#     def update_average_screen_size(cls, new_screen_size):
#         total_size = cls.average_screen_size * (cls.total_televisions - 1) + new_screen_size
#         cls.average_screen_size = total_size / cls.total_televisions
#
#     @classmethod
#     def get_average_screen_size(cls):
#         return cls.average_screen_size
#
# # Example Usage
# tv1 = Television("Samsung", 55)
# tv2 = Television("LG", 65)
# tv3 = Television("Sony", 50)
#
# print(Television.get_average_screen_size())

# class course:
#     total_courses = 0
#     courses_list = []
#
#     def __init__(self, name, instructor):
#         self.name = name
#         self.intructor = instructor
#         course.add(self)
#
#     @classmethod
#     def add(cls, name):
#         cls.courses_list.append(name)
#         cls.total_courses += 1
#
#     @classmethod
#     def get_count(cls):
#         print(cls.total_courses)
#         return (f"{course.name} by {course.instructor}" for course in cls.courses_list)
#
#
# course1 = course("Math 101", "Dr. Smith")
# course2 = course("History 201", "Prof. Johnson")
# course3 = course("Computer Science 301", "Dr. Lee")
#
# print(course.get_count())


# static metod
# class Math:
#     @staticmethod
#     def addnumber(a, b):
#         return a + b
#
# print(Math.addnumber(1,2))


# class Temperature:
#
#     @staticmethod
#     def cels_to_far(temp):
#         return temp-127
#
# print(Temperature.cels_to_far(273))
#

# class Distance:
#
#     @staticmethod
#     def mill_tokm(dist):
#         return dist/1000000
#
# print(Distance.mill_tokm(123456700000))


# class Utility:
#
#     @staticmethod
#     def is_even(numb):
#         return True if numb / 2 == 0 else False
#
# print(Utility.is_even(15))
#




class Time:

    @staticmethod
    def sec_to_min(time):
        return time/60

print(Time.sec_to_min(600))