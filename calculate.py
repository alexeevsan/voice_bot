import operator


def calculate(msg):
    try:
        a, oper, b = msg.replace(',', '.').split(' ')
    except:
        return msg

    a = float(a) if '.' in a else int(a)
    b = float(b) if '.' in b else int(b)

    ops = {
        '+': operator.add,
        '-': operator.sub,
        'х': operator.mul,
        '/': operator.truediv
    }

    return str(ops[oper](a, b))