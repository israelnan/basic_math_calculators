# I have chosen to check with all equal numbers because I think this is the bast way to check weather my function
# is going over all arguments, and with negative number to see if it writen so it can understands the meaning of
# # negative.
def largest_and_smallest(num1, num2, num3):
    """

    :param num1:
    :param num2:
    :param num3:
    :return:
    """
    x = (num1, num2, num3)
    largest = x[0]
    for i in range(3):
        if x[i] > largest:
            largest = x[i]
    smallest = x[0]
    for i in range(3):
        if x[i] < smallest:
            smallest = x[i]
    print(largest, smallest)
    return largest, smallest


def check_largest_and_smallest():
    x_check = [largest_and_smallest(17, 1, 6), largest_and_smallest(1, 17, 6), largest_and_smallest(1, 1, 2), largest_and_smallest(1, 1, 1), largest_and_smallest(1, -17, 6)]
    if x_check == [(17, 1), (17, 1), (2, 1), (1, 1), (6, -17)]:
        return True
    else:
        return False


if __name__ == '__main__':
    check_largest_and_smallest()
