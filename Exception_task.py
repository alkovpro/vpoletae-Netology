# Pollish notation
# with no assert but x2 try/except :)

def enter():
    answer = input("Please enter math expression in format '+ a b': ")
    return answer

def check_input(expression):
    operator = ''
    operators = ['+', '-', '*', '/']
    num_1 = int()
    num_2 = int()
    try:
        operator, num_1, num_2 = expression.split(' ')
        if operator not in operators or (int(num_1) or int(num_2)) <= 0:
            enter()
        else:
            return operator, int(num_1), int(num_2)
    except:
        enter()

def calculate(operator, num_1, num_2):
    result = int()
    if operator == '+':
        result = num_1 + num_2
    elif operator == '-':
        result = num_1 - num_2
    elif operator == '*':
        result = num_1 * num_2
    elif operator == '/':
        result = num_1 / num_2
    print('Total result: {}'.format(result))
    
# key loop
while True:
    expression = enter()
    try:
        operator, num_1, num_2 = check_input(expression)
        calculate(operator, num_1, num_2)
    except:
        check_input(expression)


