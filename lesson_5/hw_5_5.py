#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
        with open ('file_5.txt', 'w+') as file_obj:
            line = input ('Введите цифры через пробел \n')
            file_obj.writelines (line)
            my_numb = line.split()
            summa = (sum(map(int, my_numb)))
            print (f'Сумма = {summa}')
            file_obj.writelines (f' Summa = {summa}')
summary()