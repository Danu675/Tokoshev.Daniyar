# print("Hello World")
# name = input("your name : ")
# surname = "Dodk"
# age = int(input("age :"))
# height = 1.80
# current_year = 2023
# born = current_year - age
# print(f"{name} {surname},born : {born}")
# sum_ages = 17 + 16 + 18 + 22 + 20 +32 + 19 + 16 + 19 + 23
# students_count = 10
# # average_age = int(sum_ages / students_count)
# average_age = round(21.788745,1)
# print(average_age)
# print(20.8 // 2)

# print(name.title(),surname.upper())
# print(name + surname)
# print("{} {}".format(name,surname))
# print(f"{name} {surname}")
# first_number =  30
# second_number = 10
# print(first_number + second_number)
# print(first_number - second_number)
# print(first_number * second_number)
# print(first_number / second_number)
# print(first_number // second_number)
# print(first_number ** second_number)
# print(first_number % second_number)




# right
# var=5
# var_1 = 5
# Var = 5
# var_one_1 = 5
# VarIne = 1



# wrong!
# 1bad = 0
# &b&ad*>- = 0

# Логический тип данных , условные конструкции
# time = input("enter your time please =  ")
# if time == "morning" or time == "утро":
#     print("good morning")
# elif time == "day" or time == "день":
#     print("good afternoon")
# elif time == "evening" or time == "вечер":
#     print("good evening")
# else:
#     print("good night")
# "Операторы Сравнения"
# print(5 > 6)
# print(8 > 5)
# print(7 == 9)
# print(2 != 9)
# print(5 <= 5 )
# print(5 < 5 or 5 == 5)
# print(2 > 0.5 and 2 < 3)
# print(0.5 < 2 < 3)
# maximum = 10000
# minimum = 100
# sum_expenses = 1560.85
# average_expense = round(sum_expenses,1)
# if average_expense > maximum :
#     print("too much !")
# elif average_expense < minimum :
#     print("мало ")
# else :
#     print("average")
# """Операторы Назначения"""
# print(bool(0))
# print(bool(0.1))
# print(bool(" "))
# num = 6
# num += 4
# print(num)
# print(not True)
# name = "jack"
# age = 21
# weight = 67.3
# married = True
# print(type(married))
# [start:stop:step]
# word = "123456789"
# # part = word[::-1]
# # print(part)
# word ="*" * len(word[:7]) + word[-2:]
# print(word)
# count = len(word)
# print(count)
# print(word[-1])
# print(word.isdigit())
# print(word.startswith("4"))
# print(word.isalpha())
# print(word.isalnum())
# temperature = int(input("Введите температуру - "))
# if temperature <= 10 and temperature >= - 40:
#     print("На улице холодно")
# elif temperature >= 11 and temperature <= 14:
#     print("На улице прохладно")
# elif temperature >= 15 and temperature <= 21:
#     print("На улице нормально")
# elif temperature >= 22 and temperature <= 45:
#     print("На улице жарко")
# else:
#     print("Такой погоды не бывает")
# "Доп задание написать логику проверки пароля"
# "условия на свои усмотрение"
# elif (date>=23 and date<=31 and month== 12)or(month == 1 and date<=20 and date>=1):



# "Циклы WHILE FOR"
# day_sum = 0
# for day in range(1,7+1):
#     expens=int(input(f"Expense for day = {day}:"))
#     day_sum += expens
# print(day_sum)
# print(day_sum/7)
# rus="йцукенгшщзхъфывапролджэячсмитьбю."
# eng = qwertyuiop[]asdfghjkl;'zxcvbnm,./'
# print(type(object))
# списки - list , кортежи - tuple
# object = 312,996.0,"Geeks",True,[1,4,2]
# object = list(object)
# object= tuple(object)
# one =(56, )
# print(one)




#int()
#float()
#str()
#bool()
#list()
# new = list('python')
# new = list(range (1,6))
# print(new)
# object = [312,996,"python","geeks",5,5,6,3,True,False]
# object = [
#     'sam',
#     'tima',
#     'syka',
#     'patasha',
#     'ольга',
#     'моя жопа'
# ]
# name = 'rustam'
# name2 = 'igor'
# print(id(name))
# print(id(name2))
# new = object
# print((id(new), id(object))#проверяет их айди
# print(new == object)
# print(new is object)
'''add'''
# deleted_list=[]
# deleted_list.append(object.pop(1))
# deleted_list.append(object.pop(object.index("patasha")))
# print(object)
# print(deleted_list)
# object.extend(new)#расширить список!
# object += new
# # object.append('31-3')
# # object.insert(3,70)
# print(object)
'''edit'''
# object=object[::-1]
# print(object)
# object[2:4] = 500,700
# object.sort()
# object[1],object[4]=object[4]object,object[1]
# object[4]=100
# object.reverse()#перевернуть список
# print(object)
'''delite'''
# deleted = object.pop(1)#Удаляет хз как
# object = [i.upper() for i in object if i =="ольга"]
# del object[:5]#Универсально удаляет
# object.pop(1)#По индексу удаляет
# object.remove('sam')#по имени удаляет
# print(deleted,object)
# print((object[1:4]))
# print(type(object))
#Словари ,множества.
#1)ключи должны быть из неизменяимых данных все кроме списка
#2)ключи должны быть
#3)значением может быть любой тип данных
# object={1,2,3,2,4,3,5}
# object2=[1,2,3,2,4,4,5]
# object.add(7)
# print(object)
# print(object2)
# lagman = {"noodles","meat","pepper"}
# shorpo = {"meat","potato","carrot"}
# print(lagman.difference(shorpo))#Различие
# print(lagman.intersection(shorpo))#Общее
# print(lagman & shorpo)
#
# print(lagman.union(shorpo))#Смешивание всего
# print(lagman )
#
# print(lagman.difference(shorpo))#смешивание всего  кроме различий
# print(lagman-shorpo)
#
# print(lagman.symmetric_difference(shorpo))
# print(lagman )
# print(type(student))

# menu = {
#     "lagman": {'noodles','meat','pepper'},
#     'shorpo': {'meat','potato','carrot'},
#     'plov':{'rice','carrot','meat'},
#     'okroshka':{'sousage','milk','celery'}
# }
# while True :
#     button = input("1) search by name:\n"
#                    "2) search by ingrs:\n"
#                    "0) exit\n")
#     if button == "0":
#         print("goodbye !")
#         break
#     if button == "1":
#     name = input("enter food name: ")
#     if name in menu.keys():
#         print(menu[name])
#     else:
#         print("андай жок!\n"
#               f"варик: {tuple(menu.keys())}")
#
#     ingridient = input("ingridient: ")
#     for name,ingridients in menu.items():
#         elif ingridient in ingridients:
#             print(name)
#{key: value}
# print(student["name"])
# print(student['age'])
# print(dict[["one",1],["two",2]])
# print(dict(enumerate("python",start=1)))
# new = dict(name="Nurlan",age=79,country="KG")
# print(new)

# res={i:int(input(f'enter day{i} :'))for i in range (1,8)}
# print(sum(res.values()),sum(res.values())/len(res.values()))#-Это первая домашка в двух строчках

# student = {
#     "name":'Karina',
#     'age': 22,
#     "height":1.75,
#     "married":False,
#     "hobby":["piano","violin","voleyball"]
#     # "Languages":("uyg","kgz","rus","eng")
# }
'''add'''
# student["surname"] = "tokoshev"
# student["hobby"].append("chess")
# student.update(new)
# student["languages"]=list(student["languages"])
# student["languages"].append("ger")
# student["languages"]=tuple(student["languages"])
# student["hobby"]+=("esp",)
'''edit'''
# student["married"]=True
# student["hobby"][-1]="football"
# student["age"]+=1
# print(student.keys())
# print(student.values())
# print(student.items())
# for key , value in student.items():
#     print(f'{key} => {value}')
# for i in student:
#     print(i,"-",student[i])
'''delite'''
# del student["hobby"]
# student.pop("hobby")
# deleted = student.pop("hobby")
# print(student.get("name","жок андай!"))#проверка есть ли такой ключ
'''Функии Аргуменьты *args,*kwargs '''
'''def - define - определить!!'''
# Определние наименования (параметры):
#     Тело
#     Возврат результат
#
# вызов функции
# наименования(аргументы)
# def get_square(width, length):
#     return width * length
# square_2 = get_square(4,6)
# square_hall=get_square(width=8,length=16)
# print(square_2,square_hall,sep="\n")
# def menu(**kwargs):
#     return kwargs
# monday = menu(drink="tea",eat="pizza")
# tuesday = menu(drink="cola",eat="burger",dessert="cake")
# print(monday)
# print(tuesday)
# def func(a,b=0,*c,**d):
#     return [a,b,c,d]
# print(func(2,3,4,5,6,p=7,l=8))
# def plus(*args):
#     return sum(args)
# print(plus(2,4,6,10,96059))

# witdh = 4
# length = 6
# square_2 = witdh * length
# print(square_2)
# width = 8
# length = 16
# square_hall = width * length
# print(square_hall)
# def greet(name,surname=None):
#     print(f'name: {name} surname:{surname}') #нэйм - обязательный позиционный параметр!!!!!!!
#
# greet("Пошла нахуй","сука")# обязательный позиционный аргумент!!!!
# greet(surname="bruce",name="lee")#Keywords arguments!!!!!!!!!!!
# greet("jonny")
# def len1(sequence):
#     counter = 0
#     for _ in sequence:
#         counter +=1
#     return counter
#
# print(len("12345")+5)
# print(len1("12345")+5)
# def min1(sequence):
#     min_value =sequence[0]
#     for i in sequence:
#         if i < min_value:
#             min_value = i
#         return min_value
# print(min([2,3,4,5]))
# def min1(sequence):
#     return sorted(sequence)[-0]
# print(min1([23,25,11,97,1233]))
'''8 урок '''
#Работа с файлами
#w - write
#a - add - Добавиьб
#r - read - читать
#x - unique filename

# file = open('new.txt','w',encoding='UTF-8')
# file.write('Бишкек,Кыргызстан!')
# file.close()#всегда закрывать
# with open('new.txt','a')as file:
#     file.write('\n222')
'''Расскажи мне структуру словаря'''
'''{Кюч:Значение}
#1)ключи должны быть из неизменяимых данных все кроме списка
#2)ключи должны быть
#3)значением может быть любой тип данных'''
a = "fa"