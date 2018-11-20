# creating dict

cook_book = {}
with open('cookbook.txt', 'rt') as f:
    for line in f:
        dish = line.strip()
        dish_receipt = []
        ingridients_counter = int(f.readline().strip())
        for ingridient in range(1, ingridients_counter + 1):
            ingridient_dict = {}
            ingridient_name, quantity, measure = f.readline().strip().split(' | ')
            ingridient_dict['ingridient_name'] = ingridient_name
            ingridient_dict['quantity'] = int(quantity)
            ingridient_dict['measure'] = measure
            dish_receipt.append(ingridient_dict)
        cook_book[dish] = dish_receipt
        f.readline()   

# creating func
available_dishes = []
for key in cook_book.keys():
    available_dishes.append(key)
    
dishes = []
person_count = str()
dish = ''

while not dish == 'no':
    dish = input('Please choose dish (to refuse enter "no"): ')
    if dish.lower() == 'no':
        break
    elif dish.capitalize() in available_dishes:
        dishes.append(dish.capitalize())
    else:
        print("Unfortunately we don't know the receipt for this dish")

while not person_count.isdigit() == True:
    person_count = input('For how many people we will cook?')
    
def get_shop_list_by_dishes(dishes, person_count):
    shop_list_dict = {}
    measure_dict = {}
    already_used = []
    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingridient['ingridient_name'] in already_used:
                shop_list_dict[ingridient['ingridient_name']]['quantity'] += ingridient['quantity']
            else:
                measure_dict['quantity'] = ingridient['quantity'] * int(person_count)
                measure_dict['measure'] = ingridient['measure']
                shop_list_dict[ingridient['ingridient_name']] = measure_dict.copy()
                already_used.append(ingridient['ingridient_name'])

    print(shop_list_dict)

get_shop_list_by_dishes(dishes, person_count)










    
