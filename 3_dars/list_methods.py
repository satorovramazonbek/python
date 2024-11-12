# mevalar = ['olma', 'shaftoli', 'nok']
# mevalar.insert(0,'uzum')
# print(mevalar)            # fruitsda nolinchi indexda uzumni qo'shadi

# fruits = ['olma', 'o\'rik', 'shaftoli']
# fruits.append('mango')
# print(fruits)     #fruitsni oxirida mangoni qo'shadi


# fruits = ['olma', 'o\'rik', 'shaftoli']
# fruits.clear()
# print(fruits)       #fruitsni tozalaydi


# fruits = ['olma', 'o\'rik', 'shaftoli']
# x = fruits.copy()
# x.append('uzum')
# print(x)      # fruitsni x ga copy qilib olib unga uzumni qushadi


# fruits = ['olma', 'o\'rik', 'shaftoli']
# p = fruits.count('olma1')
# if p ==0:
#     print('yo')
# else:
#     print(p)   #count olma1 degan obyektni qidiradi

#
# fruits = ['olma', 'o\'rik', 'shaftoli']
# fruits.extend(('uzum', 'gilos','gul'))
# print(fruits)       #fruitsga tupleni elementlarini qo'shadi


# fruits = ['olma', 'o\'rik', 'shaftoli']
# x = fruits.index('shaftoli')
# print(x)      #fruitsdan shaftolini indexisini topadi



# fruits = ['olma', 'o\'rik', 'shaftoli']
# x = fruits.pop(1)
# print(x)
# print(fruits)           # pop fruitsdan 1 indexdagi elementni uchirib tashaydi


# fruits = ['olma', 'o\'rik', 'shaftoli']
# fruits.remove('olma')
# print(fruits)       #fruitsdan olma elementini topib uchiradi birinchi turganini

#
# fruits = ['olma', 'o\'rik', 'shaftoli']
# fruits.sort()
# print(fruits)   # fruits elementlarini alifbo tartibida tartiblaydi


fruits = ['olma', 'o\'rik', 'shaftoli']
fruits.sort(reverse=True)
print(fruits)   # fruits elementlarini alifbo tartibiga teskari tartiblaydi