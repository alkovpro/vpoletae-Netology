# searching for .sql files
import os

while True:
    search_string = input('Please enter a string: ')
    search_list = []

    for file in os.listdir('C:\\'):
        if file.endswith('.sql'):
            file_path = os.path.join('C:\\', file)
            with open(file_path, 'r') as f:
                f.read()
                if search_string in f:
                    search_list.append(file)
                else:
                    continue
        else:
            continue

    for file in search_list:
        print(file)

    print('Total: {}'.format(len(search_list))
            
                       

        
    
