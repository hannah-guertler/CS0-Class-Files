def recurExp(number, exp):
    
    if exp == 1:
        return number
    else:
        return number * recurExp(number, exp - 1)