#!/usr/bin/python3
# a function that
def list_division(my_list_1, my_list_2, list_length):
    divs = []
    for index in range(list_length):
        val = 0
        try:
            val = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
        except IndexError:
            print('out of range')
        finally:
            divs.append(val)

    return divs
