#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы
#сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

def my_func (time,stavka,bonus):
    return time * stavka + bonus
file_path,time, stavka, bonus = argv
print (argv)
print(my_func(int(time), int (stavka), int (bonus))