def quadratic_equation(num1, num2, num3):
    """

    :param num1:
    :param num2:
    :param num3:
    :return:
    """
    sol1, sol2 = None, None
    if (num2 ** 2 - 4 * num1 * num3) < 0:
        return sol1, sol2
    elif (num2 ** 2 - 4 * num1 * num3) == 0:
        sol1 = (-num2) / (2 * num1)
    else:
        sol1, sol2 = (-num2 + (num2 ** 2 - 4 * num1 * num3) ** 0.5) / (2 * num1), (
                -num2 - (num2 ** 2 - 4 * num1 * num3) ** 0.5) / (2 * num1)
    return sol1, sol2


def quadratic_equation_user_input():
    exp = input('Insert coefficients a, b, and c: ').split()
    if exp[0] == '0':
        print('The parameter \'a\' may not equal 0')
        return
    else:
        sol = quadratic_equation(float(exp[0]), float(exp[1]), float(exp[2]))
        if sol[0] is not None and sol[1] is not None:
            print('The equation has 2 solutions:', sol[0], 'and', sol[1])
        elif sol[0] is not None and sol[1] is None:
            print('The equation has 1 solution:', sol[0])
        elif sol[0] is None and sol[1] is None:
            print('The equation has no solutions')
        return


if __name__ == '__main__':
    quadratic_equation_user_input()
