# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

vyr = int (input ("Введите значение выручки, руб. "))
zat = int (input ("Введите значение издержек, руб. "))
pr = vyr-zat
if pr > 0:
    print ("Финансовый результат - прибыль")
    sotr = int (input ("Введите численность сотрудников "))
    ren = vyr/zat*100
    sotr_1=vyr/sotr
    print("Рентабельность", ren, "%" )
    print("Прибыль на одного сотрудника", sotr_1, "руб.");
elif pr < 0:
    print ("Финансовый результат - убыток");
else:
    #pr == 0
    print("Результат в 'ноль'")