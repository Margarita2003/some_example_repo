#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func (a,b,c):
    return sum([a,b,c]) - min(a,b,c)

print (my_func(1,2,3))
print (my_func(1,20,30))
print (my_func(1,1,1))