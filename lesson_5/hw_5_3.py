#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open ('file_3.txt', encoding='utf-8') as my_file:
    list_1 = my_file.readlines()
    name = []
    oklad = []
    for i in list_1:
        i=i.split()
        if int (i[1]) < 20000:
            name.append (i[0])
        oklad.append (i[1])
print (f'Оклад меньше 20000 {name}, средний оклад {sum (map(int, oklad))/len (oklad)}')