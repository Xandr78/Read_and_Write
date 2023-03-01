# Задача №1 Получить словарь
from pprint import pprint
with open('recipes.txt', 'r', encoding='utf-8') as f:
    cook_book = {}
    cook_book_list = []
    for line in f:
        cook_book_list.append(line.strip())
        dish_name = line.strip()
        ingredients_count = int(f.readline())
        ingredients = []
        for i in range(ingredients_count):
            ingred = f.readline().strip()
            name, quantity, parameter = ingred.split('|')
            ingredients.append({'name':name, 'quantity': quantity, 'parameter': parameter})
        cook_book[dish_name] = ingredients
        f.readline()
pprint(cook_book, sort_dicts = False)

# Заказ
print(f'\nВАШ ЗАКАЗ: \n')
print(f'Перечень возможных блюд: {cook_book_list} \n')
dishes_list = []
d1 = ''
flag = False
counter_dish = 0
while cook_book != '':
    counter_dish = 0
    counter_dish2 = 0
    d1 = input('введите свой заказ из перечня блюд через ПРОБЕЛ (нажмите Enter, если больше заказывать не надо)):').split()
    if len(d1) == 0:
        print('Вы ничего не заказали!')
        continue    
    for i in d1:
        counter_dish2 += 1
        if i not in cook_book and d1 != '':
            print(f'\nБлюда №{counter_dish2} - нет в меню! Вы можете добавить любое блюдо из нашего меню!')
            print(f'Сейчас ВАШ ЗАКАЗ состоит из: {dishes_list}')
            print(f'Перечень блюд из нашего МЕНЮ: {cook_book_list} \n')
            break
        elif i in cook_book:
            counter_dish += 1
            dishes_list.append(i)         
            if counter_dish == len(d1):                
                flag = True                
                break
    if flag == True:
        break    
                       
p_c1 = int(input('введите количество персон:', ))
print(f'\nСейчас ВАШ ЗАКАЗ состоит из: {dishes_list} на {p_c1} персоны\n')
    
# Задача №2 Функция для получения словаря с названием ингредиентов и его количества для блюда
def get_shop_list_by_dishes(dishes, person_count):
    order_ingredients = {}
    for dish_some in dishes:        
        for ing in cook_book[dish_some]:
            ing_dict = {}
            if ing['name'] not in order_ingredients:
                ing_dict['parameter'] = ing['parameter']
                ing_dict['quantity'] = int(ing['quantity']) * person_count
                order_ingredients[ing['name']] = ing_dict
            else:
                order_ingredients[ing['name']]['quantity'] = order_ingredients[ing['name']]['quantity'] + int(ing['quantity']) * person_count
    return order_ingredients
                
print(get_shop_list_by_dishes(dishes_list, p_c1))