def calculator(number_1, operator, number_2):
    if operator == '+':
        return number_1 + number_2
    elif operator == '-':
        return number_1 - number_2
    elif operator == '*':
        return number_1 * number_2
    elif operator == '/' and number_2 = 0:
        return 'на ноль делить нельзя'
    elif operator == '/':
        return number_1 / number_2
    elif operator == '//':
        return number_1 // number_2
    elif operator == '**':
        return number_1 ** number_2
    elif operator == '%':
        return number_1 % number_2
    else:
        return 'error'

def mirror(string:str, string2='hello'):
    if string = string[::-1]:
        return True
    else:
        return False

def multiplication_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result
