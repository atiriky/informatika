import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    data = []
    with open(INPUT_FILENAME, 'r', encoding="utf-8") as file:  #Открываем CSV файл для чтения с кодировкой UTF-8
        reader = csv.DictReader(file, delimiter=",")#Создаём reader он превратит каждую строку в словарь, где ключами будут названия столбцов, а значениями соответствующие значения в этой строке
        for row in reader:#Проходим по всем строкам CSV и добавляем каждую в список data
            data.append(row)
    with open(OUTPUT_FILENAME, 'w', encoding="utf-8") as json_file:#Открываем JSON файл для записи
        json.dump(data, json_file, indent=4, ensure_ascii=False)
if __name__ == "__main__":
    task()
    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_file:#Открываем созданный который только что создали файл JSON и выводим его
        for line in output_file:
            print(line, end="")