def is_vormir_safe(thresh_temp, day_1_temp, day_2_temp, day_3_temp):
    measured_temp = [day_1_temp, day_2_temp, day_3_temp]
    higher = []
    for i in measured_temp:
        if i > thresh_temp:
            higher.append(i)
    if len(higher) >= 2:
        return True
    else:
        return False


if __name__ == '__main__':
    is_vormir_safe()
