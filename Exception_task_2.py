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
    operator, num_1, num_2 = expression.split(' ')
    assert int(num_1) > 0 and int(num_2) > 0, print('Please enter positive numbers!')
    if operator not in operators:
        print('Please enter correct operator!')
    else:
        return operator, int(num_1), int(num_2)

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
        print("You'have enetered the wrong symbols!")


