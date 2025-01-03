startproject = """
Mehmonxonaga xush kelibsiz!
  Buyruqni tanlang:
  1 - mehmon qo'shish
  2 - mehmonni ro'yxatdan chiqarish
  3 - mehmonlar ro'yxati
  
  0 - dasturdan chiqish
"""
turiuchun = """
Xona turini quyidagi belgilar orqali tanlang: 
  e - ekanom
  s - standart
  l - lyuks
"""
print(startproject)

diction_people = {"John": [12, "standart"],
                  "Doe": [15, "standart"]
                  }
while True:
    n = int(input(f"{startproject}\n Komandani kiriting: "))
    if n == 1:
        ism = input("Ism: ")
        while True:
            xona = int(input("Xona raqamini kiriting: "))

            # Xona bandligini tekshirish
            xona_band = any(xona == value[0] for value in diction_people.values())

            if xona_band:
                print("Bu xona band, boshqa xona tanlang.")
            else:
                turi = input(turiuchun)
                turga = 'ekanom' if turi == 'e' else 'standart' if turi == 's' else 'lyuks' if turi == 'l' else 'notanish'

                diction_people[ism] = [xona, turga]
                print(f"{ism} mehmon ro'yxatga qo'shildi.")
                break

    elif n == 2:
        ism = input("Mehmon nomini kiriting uni ro'yxatdan o'chirish uchun: ")
        if ism in diction_people.keys():
            del diction_people[ism]
        else:
            print("Bunday foydalanuvchi mavjud emas!!!")

    elif n == 3:
        if diction_people:
            print("Ismi \t\tXonasi\t\tXona turi\n")
            for key, value in diction_people.items():
                print(f"{key}: \t\t {value[0]}, \t\t{value[1]}")
        else:
            print("ro'yxat mavjud emas!!!")

    elif n == 0:
        exit()
