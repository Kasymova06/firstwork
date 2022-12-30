# Задание 1
# def zahro(zahro1):
#      zahro2 = zahro1.title().split()
#      for i in range(len(zahro2)):
#           print(zahro2[i][0], end='')
# zahro('Лос Анджелес')
# Задание 2
# zahro = {}
# def zahro1(zahro2):
#      zahro3 = zahro2.lower().split(" ")
#      for i in zahro3:
#           zahro[i] = zahro3.count(i)
# zahro1("Money, money, money, it’s always sunny, in the richmen’s world")
# print(zahro)
# Задание 3
def nyc(exchange):
     zahro1 = list(exchange)
     zahro2 = set(exchange)
     if len(zahro1) == len(zahro2):
          return True
     return False
print(nyc("zahro"))
# Задание 4
# def zahro(word):
#      return int(str(word)[::-1])
# print(zahro(123))
# Доп задание 5
# def lena():
#      while True:
#           qr = input("Введите  что нибудь: ")
#           if qr.find("?")>=0:
#                print("конечно")
#           elif qr.find("!")>=0:
#                print("успокойся")
#           elif qr == "":
#                print("“Как классно, когда ты молчишь. Продолжай в том же духе")
#           else:
#                print("ну и что")
# lena()               