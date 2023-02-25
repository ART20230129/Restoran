import os
from pprint import pprint

with open('recipes.txt', encoding ='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for number in range(ingredients_count):
            ingr = file.readline().strip()
            ingredient_name, quantity, measure = ingr.split(' | ')
            ingredients.append(
                {'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
                }
            )
        cook_book[dish] = ingredients
        file.readline()


pprint('cook_book =', cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ingridients_list = {}
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingr in cook_book[dish_name]:
                person_list = {}
                if ingr['ingredient_name'] not in ingridients_list:
                    person_list['measure'] = ingr['measure']
                    person_list['quantity'] = int(ingr['quantity']) * person_count
                    ingridients_list[ingr['ingredient_name']] = person_list
                else:
                    ingridients_list[ingr['ingredient_name']]['quantity'] = ingridients_list[ingr['ingredient_name']]['quantity'] + int(ingr['quantity']) * person_count

        else:
            print('Нет такого блюда!')
    print(f"Для приготовления блюд на {person_count} человек необходимо приобрести:")

    return print(ingridients_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)





