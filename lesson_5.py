#Циклы for,while
# for i in range(2, 1001, 2):
#     print(i)

# names =["Kurmanbek", "Daniel", "Askhat", "Nursultan"]
# for ny in  names:
#     # print(ny)
#     if ny == "Askhat":
#         print("Askhat есть")

# numbers = [1, 10, 100, 12, 50, 333, 407]   
# for num in numbers:
#     if num % 2 == 0:
#         print(num, "четный")
#     else:
#         print(num, "нечетный")

# name = "Kurmanbek"
# for n in name:
#     if n == "a":
#      print("Буква есть в имени")
    # print(n)

# number = "100" # не итеруется типы данных
# for num in number:
#     print(num)

# cities_tup = ("Osh", "Bishkek", "Talas", "Tokmok" ) # Тuple здесь выводит
# for city in cities_tup:
#     print(city)

# cars = {"BMW", "MERSEDES", "TESLA", "HONDA"} # set здесь работает
# for i in cars:
#     print(i)

# student = {"name": "Daniel", "age": "18", "language" : "Python"}
# for key, value in student.items(): # Items возврвщает ключи значения
#     # print(key, value)
#     if key == "language" and value == "Python":
#         print("Питонист найден")

# numbers =[]
# for n in range(1, 1001):
#     numbers.append(n)
#     print(numbers)

# for i in range(1, 11):
#     print(i)
#     if i == 6:
#         print("STOP")
#         continue

# numbers = [10, 20, 30, 40, 50]
# for i, n in enumerate(numbers): #выводит индекс
#     print(i, n)

# num1 = 10
# num2 = 20
# while num1 < num2:
#     print(num1)
#     # num1 = num1 + 1 
#     num1 += 1 #в кратце выше показанного 
 

# import random 

# n = 0 
# random_number = random.randint(1, 100)
# print(random_number)
# while True:
#     n += 1
#     if n == random_number:
#       print("Ненайден") #не запусти этого
#     break
# import time

# process = 0
# while True:
#     print(str(process) + "% HACK")
#     process += 10
#     time.sleep(1)
#     if process == 100:
#         print("HACKEND")
#         break