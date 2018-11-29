# defining functions
def create_cook_dict(file):
    '''creating dict'''
    with open(file, 'rt') as f:
        cook_book = {}
        for line in f:
            dish = line.strip()
            dish_receipt = []
            ingridients_counter = int(f.readline().strip())
            for ingridient in range(ingridients_counter):
                ingridient_dict = {}
                ingridient_name, quantity, measure = f.readline().strip().split(' | ')
                ingridient_dict['ingridient_name'] = ingridient_name
                ingridient_dict['quantity'] = int(quantity)
                ingridient_dict['measure'] = measure
                dish_receipt.append(ingridient_dict)
            cook_book[dish] = dish_receipt
            f.readline()
    return cook_book

def invite_to_choose(cook_book):
    '''invite user to choose'''
    dishes = []
    person_count = str()
    dish = ''

    while not dish == 'no':
        dish = input('Please choose dish (to refuse enter "no"): ')
        if dish.lower() == 'no':
            break
        elif dish.capitalize() in cook_book:
            dishes.append(dish.capitalize())
        else:
            print("Unfortunately we don't know the receipt for this dish")

    while not person_count.isdigit() == True:
        person_count = input('For how many people we will cook?')

    return dishes, person_count
    
def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list_dict = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingridient['ingridient_name'] in shop_list_dict :
                shop_list_dict[ingridient['ingridient_name']]['quantity'] += ingridient['quantity']
            else:
                measure_dict = {}
                measure_dict['quantity'] = ingridient['quantity'] * int(person_count)
                measure_dict['measure'] = ingridient['measure']
                shop_list_dict[ingridient['ingridient_name']] = measure_dict
    print(shop_list_dict)

#key loop
file = 'cookbook.txt'

cook_book = create_cook_dict(file)
dishes, person_count = invite_to_choose(cook_book)
get_shop_list_by_dishes(dishes, person_count, cook_book)










    
