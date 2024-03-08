import operator


def calculate(msg):
    try:
        a, oper, b = msg.replace(',', '.').split(' ')
    except:
        return 'Нет такой команды'

    a = float(a) if '.' in a else int(a)
    b = float(b) if '.' in b else int(b)

    ops = {
        '+': operator.add,
        '-': operator.sub,
        'х': operator.mul,
        '/': operator.truediv
    }

    result = ops[oper](a, b)
    if type(result) is float:
        result = round(float(result), 2)

    return str(result)
