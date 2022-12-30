# 1
# it_company =("Google", "Amazon", "Microsoft")
# print(it_company)
# lst_it_company = list(it_company)
# print(lst_it_company)
# lst_it_company.append("Tesla")
# print(lst_it_company)
# it_company = tuple(lst_it_company)
# print(it_company)
# 2
# it_company =("Google", "Amazon", "Microsoft")
# print(it_company)
# lst_it_company = list(it_company)
# print(lst_it_company)
# print(lst_it_company[1])

# # 3
# it_company =("Google", "Amazon", "Microsoft")
# print(it_company)
# lst_it_company = list(it_company)
# print(lst_it_company)
# lst_it_company [0] = "Apple"
# print(lst_it_company)
# it_company = tuple(lst_it_company)
# print(it_company)

# # 4
# it_company =("Google", "Amazon", "Microsoft")
# print(it_company)
# lst_it_company = list(it_company)
# print(lst_it_company)
# lst_it_company [0] = "Apple"
# print(lst_it_company)
# print(lst_it_company[0:2:1])

# # 5
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean',
# 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite',
# 'with', 'our', 'python', '3', 'overview')
# print(text_tuple)
# lst_text_tuple = list(text_tuple)
# print(lst_text_tuple)
# print(lst_text_tuple.count("Python"))
# print(lst_text_tuple.count("Python"))

# # 6
# dictionary_1 = {'a': 300, 'b': 400} 
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_2.update(dictionary_1)
# print(dictionary_2)

# 7
# numbers = {"num_1" : 1, "num_2" : 2,"num_3": 3, "num_100" : 100}
# numbers["num_1"] = 1 * 5
# numbers["num_2"] = 2 * 5
# numbers["num_3"] = 3 * 5
# numbers["num_100"] = 100 * 5
# print(numbers)

# 8
# student = {'name' : 'Askhat', 'age' : 17}
# student['age'] = 17 * 2





# 9
# student = {"name" : "Askhat", "age" : 17, "color" : "White"}
# student['age'] = '16'
# print(student)

# 10
# student = {"name" : "Askhat", "age" : 17}
# student.pop('age')
# print(student)
 
# 11
# student = {"name" : "Askhat"}
# student.setdefault('address', 'Западный Анар')
# print(student)

# 12
parol = {}
while True:
    zahro = input("введите пароль: ")
    posledov_1 = zahro.find("123")
    if len(zahro) > 7:
        if posledov_1 < 0:
            parol.setdefault('first_p', zahro)
            proverka_paroly = input("введите повторный пароль: ")
            if parol['first_p'] == proverka_paroly:
                print("ok")
            else:
                print("различаються")
        else:
            print("простой пароль")
    else:
        print("короткий пароль")
    print(parol)
