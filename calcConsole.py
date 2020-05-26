start = input()


def sign(acts, list):
    for act in acts:
        if act in list:
            res = act
            return (res)


while start != 'exit':
    actions = ['+', "-", "/", "*"]
    result = 0
    c = 0
    start = list(start)
    c = sign(actions, start)
    strStart = ''.join(start)
    strStart = strStart.split(c)
    n1 = float(strStart[0])
    n2 = float(strStart[1])
    if c == '+':
        result = n1 + n2
    elif c == '-':
        result = n1 - n2
    elif c == '*':
        result = n1 * n2
    elif c == '/':
        if n2 == 0:
            print('Ошибка! Деление на ноль!')
            start = input()
            continue
        else:
            result = n1 / n2
    print("{:.2f}".format(result))
    start = input()
    continue
