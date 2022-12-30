#Множества set, frozenset
# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 2}
# print(numbers)
# print(numbers[0]) # Нельзя set выводить по индексу
# print(numbers[::-1]) #Set не поддерживает срезы

# names = {"Askhat", "Kurmanbek", "Daniel", "Asylbek"}
# print(names)
# names.add("Nursultan")#добавляем Nursultan в set  множество
# print(names)
# names.remove("Askhat")# Удаляем Askhat из множества
# print(names)
# names.pop()#рандомно удаляет в set
# print(names)
# names.update("Kurmanbek")# Добавляет Kurmanbek и делит по буквам
# print(names)
# names.clear()# Очищает set
# print(names)

# lst =[]
# print(type(lst))
# hello =""
# print(type(hello))
# st = {}
# print(st)

# lst = [10, 4.0, False, "Geek", [1, 2, 3], {1, 2, 3, 3}]
# print(lst)
# st = {1, 1.1, False, "1"}
# numbers = {10, 4, 9, 55, 11}
# print(st)
# print(sorted(st))
# print(sorted(numbers))
# frzn = frozenset([1, 2, 3, 4, 5, 6])
# print(frzn)
# frzn.add(10)
# print(frzn)
# frzn.remove(2)
# print(frzn)

#Tuple- кортеж
# numbers = (1, 10, 11, 2, 3, 4, 4, 5)
# print(numbers)
# tup = (1, 1.0, True, "Hello",  [2, 5, 6], {5, 6, 9}, (10, 20))
# print(tup)
# tup.append()
# print(tup.count("Hello"))
# print(tup.index(1))
# print(tup[2])
# print(tup[0:3])


# cars = ("BMW", "Mersedes", "Ferrari")
# print(cars)
# lst_cars = list(cars) #Добавление List
# print(lst_cars)
# lst_cars.append("Tesla")
# print(lst_cars)
# cars = tuple(lst_cars)
# print(cars)

# tup = (10, )
# print(type(tup))

#Dictionary-словари
student = {"student" : "Askhat", "age" : 18} #Создаем словарь Student
print(student)
print(len(student)) #Выводит длину словаря student
print(student['age'])#по ключу age выводим значение с словаря student
student.setdefault('language', 'Python') #Добавляем в словарь новый ключ и значение
print(student)
student.pop('age')#Удаляем по ключ age и его значение
print(student)
student['language'] = 'JavaScript' #Обновляем по ключу значение 
print(student)
student['place_study'] = 'GeekTech'#Если нужного  ключа нету то он добавит его
print(student)
print(student.keys()) #Выводит все ключи 
print(student.values()) #Получаем все значения словаря

# contact = ["Askhat"]
# while True:
#     command = input("1-посмотреть контакт, 2-добавить в контакты, 3-удалить контакты, 4-обновить контакт")
#     if command == "1":
#         print(contact)
#     elif command == "2":
#         app_contact = input("Введите имя: ")
#         contact.append(app_contact)
#         print("Удачно добавлен")
#     elif command == "3":
#         pop_contact = input("Введите имя человека которого хотите удалить: ").title()
#         if pop_contact in contact:
#             contact.remove(pop_contact)
#             print("контакт удален")
#         else:
#             print("контакт не найден")
#     elif command == "4":
#         star_name = input("Введите старое имя: ")
#         new_name = input("Введите новые имя: ")
#         try:
#             contact[contact.index(star_name)] = new_name
#             print("контакт обновлен")
#         except ValueError:
#             contact.append(new_name)
#             print("был создан новый контак")
#     else:
#         print("err")
#         break

    
