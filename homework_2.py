 # Задача 1
name = input("Введите имя: ")
password = input("Введиите пароль: ")
if  name == "Zahro" and password == "404070":
    print("Password is correct.You are welcome") 
elif name != "Zahro":
    print("Password is incorrect.Please try again")
elif password != "404070":
    print("Password is incorrect.Please try again")
else:
    print("err")
# Задача 2
num = int(input("Сколько градусов на улице: "))
if -30 > num:
    print("Там так холодно,лучше дома сиди!")
elif -30 <= num <= 0:
    print("Холодновато.Оденься потеплее!")
elif 0 <= num <= 15:
    print("Прохладно.Куртку накинь!")
elif 15 <= num <= 30:
    print("Тепло.Иди погуляй в парке!")
elif 30 <= num <= 50:
    print("Ого как жарко!")
elif 50 < num:
    print("Там такая жара,лучше сиди дома!")
else:
    print("Ошибка")
# Задача 3
a =("Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colourful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colourless. But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, con  sumers say, if there is advertising there must be rules. Somadverts advertise unhealthy things like cigarettes and make people waste their money.")
print("Бекв<<S>>:",a.count("s"))
print("Бекв<<T>>:",a.count("t"))
# Задача 4
str1 = 'Aidana'

str2 = 'Adilet'

new_str = ''

for i in range(6):

   new_str += str1[i] + str2[i]

print(new_str)