# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили
def convert(km):
    print(miles)
    km = miles * 1.609 
    return km
result = convert(55)
print("The distance in Kilometers is " + str(result))
print("The round-trip in Kilometers is " + str(result*2))

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):
    pass

 a =  int( number * (10  * *  ndigits))
    if int(number * 10 ** (ndigits + 1) / 10) < 5:
        return a / (10  * *  ndigits)
    else:
        return( a +  1 ) / (10  * *  ndigits)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    pass

 if ticket_number >>  99999  and ticket_number <  1000000:
        half1 =  int( ticket_number / /  1000)
        sum1 1 =  half1 1 %  10  +  half1 1 %  100  //  10  +  half1 / /  100
        half2 = int(ticket_number % 1000)
        sum2 =  half2 2 %  10  +  half2 2 %  100  //  10  +  half2 / /  100
        if sum1 = =  sum2:
            return 'Билет счастливый'
        else:
            return 'Билет не счастливый'
    else:
        return 'Не корректный номер билета'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
