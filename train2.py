def basic_op(operator, value1, value2):
    if '+' == operator:
        return value1 + value2
    elif '-' == operator:
        return value1 - value2
    elif '*' == operator:
        return value1 * value2
    elif '/' == operator:
        return value1 / value2
    
result = basic_op('/', 5, 7)
print(result)