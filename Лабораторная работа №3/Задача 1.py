# TODO Напишите функцию для поиска индекса товара
def search_fruict(nabor, namefruict):
    for nomer, nujnifruict in enumerate(nabor):# Используем функцию enumirate, чтобы задать номера предметов и сами значения
        if nujnifruict == namefruict: #Если тот фрукт, что мы ищем равен фрукту в списке, то выдает номер этого фрукта
            return nomer



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_fruict(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
