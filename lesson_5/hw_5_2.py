#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
# строк, количества слов в каждой строке.

my_file= open ('file_2.txt', 'r')
content = my_file.read()
print (f'Текст \n {content}')
my_file= open ('file_2.txt', 'r')
content = my_file.readlines()
print (f'Количество строк - {len(content)}')
my_file= open ('file_2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print (f'Количество символов {i+1} строки {len (content[i])}')
my_file = open ('file_2.txt', 'r')
content = my_file.read()
content = content.split ()
print (f'Общее количество слов - {len (content)}')
my_file.close ()