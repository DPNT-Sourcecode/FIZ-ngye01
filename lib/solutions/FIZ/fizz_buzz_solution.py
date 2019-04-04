# noinspection PyUnusedLocal
def fizz_buzz(number):
    qualifiers = []
    if is_fizz(number):
        qualifiers.append('fizz')
    if is_buzz(number):
        qualifiers.append('buzz')
    if is_deluxe(number):
        qualifiers.append('deluxe')    
    if len(qualifiers) > 0:
        return " ".join(qualifiers)
    return str(number)
    
def is_fizz(number):
    return '3' in str(number) or number % 3 == 0

def is_buzz(number):
    return '5' in str(number) or number % 5 == 0

def is_deluxe(number):
    repr = str(number)
    all_same_digits = all([digit == repr[0] for digit in repr])
    return number > 10 and all_same_digits