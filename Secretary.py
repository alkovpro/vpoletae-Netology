import sys

# Initial data structures + variables
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

command_chosen = str()
doc_number = str()
doc_type = str()
owner_name = str()
shelf_number = str()
purpose_shelf = str()

message_1 = 'No such document. Please check and try again!'
message_2 = 'Shelf already exists'

# Define all functions

def show_instructions():
    print('''
Secretary Instruction

Please follow instrictions in order to process.
You'll be provided with applicable commands to use from.

'p' - ask for a doc №, get owner
'l' - show all docs
's' - ask for a doc №, get shelf
'a' - add new doc
'd' - delete chosen doc
'm' - ask for a doc №, purpose shelf and move the doc
'as' -ask for shelf №, add new shelf
'ss' - show current shelves
'bs' - show books on shelf

'e' - exit
''')

def ask_for_command():
    chose = ''
    appl_commands = ['p', 'l', 's', 'a', 'd', 'm', 'as', 'ss', 'bs', 'e',]
    while not chose in appl_commands:
        chose = input('\nPlease chose command listed above: ')
    return chose
    
def get_owner(doc_number):
    for doc in documents:
        if doc["number"] == doc_number:
            return doc["name"]
            break
        else:
            continue
    return message_1

def show_list():
    for doc in documents:
        print ('{0} {1} {2}'.format(doc["type"], doc["number"], doc["name"]))

def show_shelf(doc_number):
    for key, value in directories.items():
        if doc_number in str(value):
            return str(key)
        else:
            continue
    return message_1

def add_doc(doc_number, doc_type, owner_name, shelf_number):
    doc_record = dict()
    doc_record["number"] = doc_number
    doc_record["type"] = doc_type
    doc_record["name"] = owner_name
    documents.append(doc_record)
    if shelf_number not in list(directories.keys()):
        directories[shelf_number] = list()
        directories[shelf_number].append(doc_number)
    else:
        directories[shelf_number].append(doc_number)

def delete_doc(doc_number):
    for doc in documents:
        if doc["number"] == doc_number:
            documents.remove(doc)
            directories[show_shelf(doc_number)].remove(doc_number)
        else:
            pass

def move_doc(doc_number, purpose_shelf):
    # remove
    for i in list(directories.values()):
        if doc_number in i:
            i.remove(doc_number)
        else:
            continue
    # append
    if purpose_shelf not in list(directories.keys()):
        directories[purpose_shelf] = list()
        directories[purpose_shelf].append(doc_number)
    else:
        directories[purpose_shelf].append(doc_number)

def add_shelf(shelf_number):
    if shelf_number not in list(directories.keys()):
        directories[shelf_number] = list()
        print('New shelf was successfully added!')
    else:
        print(message_2)
        
def show_shelves():
    shelves = ''
    for shelf in list(directories.keys()):
        shelves += shelf + ', '
    print('Current shelves: {}'.format(shelves[:-2]))

def show_books_on_shelf(shelf_number):
    books = ''
    for doc in directories[shelf_number]:
        books += doc + ', '
    print('On the shelf {0} are the following docs: {1}'.format(shelf_number, books[:-2]))
    

# Key Loop
show_instructions()
while True:
    command_chosen = ask_for_command()
    
    if command_chosen.lower() == 'p':
        while not doc_number:
            doc_number = input('Please enter doc number: ')
        owner_name = get_owner(doc_number)
        doc_number = ''
        print (owner_name)
        
    elif command_chosen.lower() == 'l':
        show_list()
        
    elif command_chosen.lower() == 's':
        while not doc_number:
            doc_number = input('Please enter doc number: ')
        shelf_number = show_shelf(doc_number)
        print ('Shelf №: {}'.format(shelf_number))
        doc_number = ''
        shelf_number = ''
        
    elif command_chosen.lower() == 'a':
        while not doc_number:
            doc_number = input('Please enter doc number: ')
        while not doc_type:
            doc_type = input('Please enter doc type: ')
        while not owner_name:  
            owner_name = input('Please enter owner name: ')
        while not shelf_number:
            shelf_number = input('Please enter shelf_number: ')

        add_doc(doc_number, doc_type, owner_name, shelf_number)
        doc_number = ''
        doc_type = ''
        owner_name = ''
        shelf_number = ''
        print('Your doc was succesfully added!')

    elif command_chosen.lower() == 'd':
        while not doc_number:
            doc_number = input('Please enter doc number: ')
        delete_doc(doc_number)
        doc_number = ''
        print ('Document {} was successfully removed!'.format(doc_number))
        
    elif command_chosen.lower() == 'm':
        while not doc_number:
            doc_number = input('Please enter doc number: ')
        while not purpose_shelf:
            purpose_shelf  = input('Please enter purpose shelf : ')
        move_doc(doc_number, purpose_shelf)
        doc_number = ''
        purpose_shelf = ''
        print('Your doc was successfullly moved!')
        
    elif command_chosen.lower() == 'as':
        while not shelf_number:
            shelf_number = input('Please enter shelf_number: ')
        add_shelf(shelf_number)
        shelf_number = ''

    elif command_chosen.lower() == 'ss':
        show_shelves()

    elif command_chosen.lower() == 'bs':
        while not shelf_number:
            shelf_number = input('Please enter shelf_number: ')
        show_books_on_shelf(shelf_number)
        shelf_number = ''
        
    elif command_chosen.lower() == 'e':
        sys.exit()
    

