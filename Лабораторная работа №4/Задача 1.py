# TODO решите задачу
import json

def task() -> float:
    filename = "input.json" #Задаём имя файла из которого будем читать данные
    with open(filename) as file:
        json_data = json.load(file)#Загружаем содержимое файла в переменную json_data
    sum_values = sum([item["score"] * item["weight"] for item in json_data]) # Считаем сумму произведений score * weight для каждого элемента списка
    return round(sum_values, 3) #Округляем итоговую сумму до трёх знаков после запятой и возвращаем результат
print(task())
