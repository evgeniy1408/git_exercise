Гурин Евгений 6 лекция
# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5


a = float(input("a = "))
b = float(input("b = "))
c = avg(a, b)
print("Среднее геометрическое = {:.2f}".format(c))

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys
import shutil

dir_name = [('dir_' + str(i + 1)) for i in range(9)]

def make_dir(path):
    dir_loc = os.path.join(os.getcwd(), path)
    try:
        os.mkdir(dir_loc)
        print(' -- папка успешно создана')
    except:
        print(dir_loc + ' -- папка уже существует')


for i in dir_name:
    make_dir(i)

def remove_dir(path):
    dir_loc = os.path.join(os.getcwd(), path)
    try:
        os.rmdir(dir_loc)
        print(' -- папка успешно удалена')
    except:
        print(dir_loc + ' -- такой папки не существует')
    pass

for i in dir_name:
    remove_dir(i)
# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.
print("Задача 2. Отобразить папки текущей директории.\n", ' - '  *  46, sep= ")
def show_dir():
    '''
 show_dir: функция вывода папок в текущей директории
    '''
    currentPath = os.getcwd()
    for i in os.listdir(currentPath): 
        dir_path = os.path.join(currentPath, i)
        if os.path.isdir(dir_path):
            print(i)
            

    print("\nВторой вариант (одной строкой):")
    print([i for i in os.listdir(currentPath) if os.path.isdir(os.path.join(currentPath, i))]) 

    print("\nТретий вариант (os.walk):")
    for dirs in os.walk(currentPath): 
        print(dirs[1])
        break

    print("\nЧетвертый вариант (os.walk, но одной строкой):")
    
    print(next(os.walk(currentPath))[1])

show_dir()
print()


# Задача-4:# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file():
    file_name = os.path.realpath(__file__)
    new_file = file_name + ".copy"

    if os.path.isfile(new_file) != True:
        shutil.copy(file_name, new_file)
        print(f"{new_file} создан")
    else:
        print("Файл уже скопирован")



