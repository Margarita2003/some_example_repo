# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции

number = int (input ("Введите целое положительное число: "))
number_max = 0
while number > 0:
    a = number % 10
    number = number // 10
    if a > number_max:
        number_max = a
print(number_max)