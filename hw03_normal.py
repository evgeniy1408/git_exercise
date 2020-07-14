# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

print("Задача-1:")
 NumList1 = [1, 2, 3, 4, 5, -10, 25]
 NumList2 = []
 import math
 for Num in NumList1:
     if Num >= 0:
         Res = math.sqrt(Num)
         if (float(Res) % 1) == 0:
             NumList2.append(int(Res))
# print(NumList2)
# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print("Задача-2:")
date = "26.11.2013"
days = ["первое",
        "второе",
        "третье",
        "четвертое",
        "пятое",
        "шестое",
        "седьмое",
        "восьмое",
        "девятое",
        "десятое",
        "одиннадцатое",
        "двенадцатое",
        "тринадцатое",
        "четырнадцатое",
        "пятнадцатое",
        "шестнадцатое",
        "семьнадцатое",
        "восемнадцатое",
        "девятнадцатое",
        "двадцатое",
        "двадцать первое",
        "двадцать второе",
        "двадцать третье",
        "двадцать четвертое",
        "двадцать пятое",
        "двадцать шестое",
        "двадцать седьмое",
        "двадцать восьмое",
        "двадцать девятое",
        "тридцатое",
        "тридцать первое"]
month = ["января",
         "февраля",
         "марта",
         "апреля",
         "мая",
         "июня",
         "июля",
         "августа",
         "сентября",
         "октября",
         "ноября",
         "декабря"]
date = "26.02.1975"
D = int((date.split("."))[0])
M = int((date.split("."))[1])
Y = (date.split("."))[2]
print(date)
print("Дата: {0} {1} {2} года".format(days[D-1],month[M-1],Y))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
 print("Задача-3")
 import random
 NumList = []
 n = int(input("Введите количество элементов списка случайных значений"))
 for item in range(n):
     NumList.append(random.randint(-100, 100))
 print(NumList)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
print("Задача-4")
NumList1 = [1, 2, 4, 5, 6, 2, 5, 2]
NumList_a = []
NumList_b = []
NumList_temp = NumList1.copy()
while NumList_temp:
    Num = NumList_temp[0]
    NumList_temp.remove(Num)
    if Num in NumList_temp:
        NumList_a.append(Num)
        while Num in NumList_temp:
            NumList_temp.remove(Num)
    else:
        NumList_a.append(Num)
        NumList_b.append(Num)

print("Исходный список:")
print(NumList1)
print("Список с уникальными элементами:")
print(NumList_a)
print("Список без повторяющихся элементов:")
print(NumList_b)