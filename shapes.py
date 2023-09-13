def shape_area():
    """

    :return:
    """
    import math
    shape = input('Choose shape (1=circle, 2=rectangle, 3=triangle): ')
    if shape == '1':
        r = float(input())
        return math.pi*(r**2)
    elif shape == '2':
        side_1 = float(input())
        side_2 = float(input())
        return side_1*side_2
    elif shape == '3':
        side = float(input())
        return 0.25*(3**0.5)*(side**2)
    else:
        return None


if __name__ == '__main__':
    shape_area()
