# Lambda функции задание 1
# hello = lambda X: X * X - 10
# print(hello(24))
# ##############################
# print((lambda X: X * X - 10)(24))

# Задание 2
# from functools import reduce
# if __name__ == '__main__':
#     name =["Kuma", "Nurtilek", "Zina", "Edzen", "Kuma", "Aitenur", "Zina"]
#     name[:] = reduce(lambda m, x: m if x in m else m + [x], name,[])
#     print(name)

# Задание 3
# numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = list(filter(lambda num: num % 2 == 0, numbers))
# print(even)
#######################################################
# numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda num: num % 2 == 0, numbers)))
#######################################################
# print(list(filter(lambda num: num % 2 == 0,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

# Задание 4
# from operator import eq
# s = input("Введите любое слово: ")
# res = all(map(lambda x: eq(*x), zip(s, reversed(s))))
# print(res)

 #Модули задание 5
# sideA = int(input("Длина: "))
# sideB = int(input("Ширина: "))
# area = sideA * sideB
# print("Площадь прямоугольника: ", area)
# sideR = int(input("Длина: "))
# sideL = int(input("Ширина: "))
# perimeter = (sideR + sideL) * 2 
# print("Периметр прямоугольника: ", perimeter)

# Задание 6
# lst =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst.reverse() 
# print(lst)

# Задание 7
a = int(input('Введите секунды :' ))
h = str(a//3600)
m = (a//60)%60
s = a%60
if m<10:
    m='0'+str(m)
else:
    m=str(m)
if s<10:
    s='0'+str(s)
else:
    s=str(s)
print(h+':'+m+':'+s)

# # Задание 8
# def ms():
#      while True:
#           qr = input("Введи что хочешь: ")
#           if qr.find("?")>=0:
#                print("Конечно")
#           elif qr.find("!")>=0:
#                print("Успокойся")
#           elif qr == "":
#                print("“Как классно, когда ты молчишь. Продолжай в том же духе")
#           else:
#                print("Ну и что")
# ms()               

# Задание 9
# def rima(sam):
#      kammy = sam.title().split()
#      for a in range(len(kammy)):
#           print(kammy[a][0], end='')
# rima('Ruby on Rails')

# Задание 10
# menu ={'beefstrogonoff': 350, 'burger': 200, 'meatloaf': 500, 'chicken pot pie': 400, 'beefshteks': 650}
# new_menu = {k:v+50 for (k,v) in menu.items()}
# print(new_menu)


