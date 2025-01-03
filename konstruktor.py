# class texnika:
#     def __init__(self, brand, model, type):
#         self.brand = brand
#         self.model = model
#         self.type = type
#
#     def info(self):
#         print(f"{self.brand} ostidagi {self.model} turi: {self.type}")
#
#
# class notebookchild(texnika):
#     def __init__(self, brand, model, type, video_card, rasm, display):
#         super().__init__(brand, model, type)  # Ota klassning __init__ metodini chaqiramiz
#         self.video_card = video_card
#         self.rasm = rasm
#         self.display = display
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, "
#               f"Video Card: {self.video_card}, Rasm: {self.rasm}, Display: {self.display}")
#
#
# class televison(texnika):
#     def __init__(self, brand, model, type, size, display):
#         super().__init__(brand, model, type)  # Ota klassning __init__ metodini chaqiramiz
#         self.size = size
#         self.display = display
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, "
#               f"size: {self.size},  Display: {self.display}")
#
#
# class Smartphones(texnika):
#     def __init__(self, brand, model, size, sim_count):
#         super().__init__(brand, model, type)
#         self.size = size
#         self.sim_coun = sim_count
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model},  "
#               f"size: {self.size},  Display: {self.sim_coun}")
#
#
# # notebook = televison('Dell', 'XPS 13', 'Notebook', '165', '1920x1080')
# # notebook.more_info()
#
# # phone = texnika('samsung', 'j3', 'b/u')
# # phone.info()
#
# smartphoone = Smartphones('Dell', 'XPS 13', 'Notebook', '165')
# smartphoone.more_info()

#
# # 2
# class transport():
#     def __init__(self, brand, model, tip):
#         self.brand = brand
#         self.model = model
#         self.tip = tip
#
#     def info(self):
#         print(f"Brand {self.brand}, Model: {self.model}, Turi {self.tip}")
#
#
# class Electrcars(transport):
#     def __init__(self, battery_life, chargin_time, brand, model, tip):
#         super().__init__(brand, model, tip)
#         self.battery_life = battery_life
#         self.chargin_time = chargin_time
#
#     def more_info(self):
#         print(
#             f"Model {self.model}, Brand: {self.brand}, Turi: {self.tip}, Batareta Hayoti: {self.battery_life}, Quvvat vaqti: {self.chargin_time}")
#
#
# class Sport_cars(transport):
#     def __init__(self, motor, color, brand, model, tip):
#         super().__init__(brand, model, tip)
#         self.motor = motor
#         self.color = color
#
#     def more_info(self):
#         print(
#             f"Model {self.model}, Brand: {self.brand}, Turi: {self.tip}, Motor: {self.motor}, rangi: {self.color}")
#
#
# class Truck(transport):
#     def __init__(self, brand, model, tip, motor, height, long, weight):
#         super().__init__(brand, model, tip)
#         self.motor = motor
#         self.height = height
#         self.long = long
#         self.weight = weight
#
#     def more_info(self):
#         print(
#             f"Model {self.model}, Brand: {self.brand}, Turi: {self.tip}, Motor: {self.motor}, balandligi {self.height}, uzuznligi: {self.long}, kengligi: {self.weight}")
#


# 3
class University():
    def __init__(self, universitet):
        self.universitet = universitet

    def info(self):
        print(f"Bu {self.universitet} oliy talim muassasasi")


class staff(University):
    def __init__(self, universitet, first_name, last_name, age):
        super().__init__(universitet)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def staff_info(self):
        print(f"UNiversitet: {self.universitet}, Familiya: {self.first_name}, Ism: {self.last_name}, yosh: {self.age}")


class Student(University, staff):
    def __init__(self, universitet, first_name, last_name, age, group):
        super().__init__(universitet, first_name, last_name, age)
        self.group = group

    def more_info(self):
        print(
            f"UNiversitet {self.universitet}, familiya: {self.first_name}, ism: {self.last_name}, yosh: {self.age}, guruh: {self.group}")


class Teacher(University, staff):
    def __init__(self, universitet, first_name, last_name, age, postition, subject):
        super().__init__(universitet, first_name, last_name, age)
        self.position = postition
        self.subject = subject

    def more_info(self):
        print(
            f"UNiversitet {self.universitet}, familiya: {self.first_name}, ism: {self.last_name}, yosh: {self.age}, Unvoni: {self.position}, Fani {self.subject}")


class Other_staff(University, staff):
    def __init__(self, universitet, first_name, last_name, age, position):
        super().__init__(universitet, first_name, last_name, age)
        self.position = position

    def more_info(self):
        print(
            f"UNiversitet {self.universitet}, familiya: {self.first_name}, ism: {self.last_name}, yosh: {self.age}, guruh: {self.position}")


class Object(University):
    def __init__(self, universitet, name):
        super().__init__(universitet)
        self.name = name

    def object_info(self):
        print(f"Universitet: {self.universitet}, nomi: {self.name}")


class Computer(Object):
    def __init__(self, universitet, name, soni, tizimi, holati):
        super().__init__(universitet, name)
        self.soni = soni
        self.tizimi = tizimi
        self.holati = holati

    def object_more_info(self):
        print(
            f"Universitet: {self.universitet}, Nomi: {self.name}, Soni: {self.soni}, Tizim: {self.tizimi}, Holati: {self.holati}")


class Mebel(Object):
    def __init__(self, universitet, name, soni, turi, holati):
        super().__init__(universitet, name)
        self.soni = soni,
        self.turi = turi
        self.holati = holati
    def object_more_info(self):
        print(f"Universitet: {self.universitet}, Nomi: {self.name}, Soni: {self.soni}, TUri: {self.turi}, Holati: {self.holati}")

