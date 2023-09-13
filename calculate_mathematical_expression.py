def calculate_mathematical_expression(num1, num2, op):
    """

    :param num1:
    :param num2:
    :param op:
    :return:
    """
    if num2 == 0:
        return None
    elif op == '*':
        return num1 * num2
    elif op == ':':
        return num1 / num2
    elif op == '-':
        return num1 - num2
    elif op == '+':
        return num1 + num2
    else:
        return None


def calculate_from_string(exp):
    sep = exp.split()
    cal = calculate_mathematical_expression(float(sep[0]), float(sep[2]), sep[1])
    return cal
