# TODO Напишите функцию find_common_participants
def find_common_participants(famili1, famili2, razdel=","):
    #Используем метод split, чтобы исбавить от разделителя
    newfamili1 = famili1.split(razdel)
    newfamili2 = famili2.split(razdel)
    obshie = list(set(newfamili1).intersection(newfamili2))#Используем метод intersection, чтобы найти пересечения между множествами, по такому же принципу как в последней практической задаче с покупками
    sortobshie = sorted(obshie)
    return sortobshie




participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, "|"))
# TODO Провеьте работу функции с разделителем отличным от запятой
