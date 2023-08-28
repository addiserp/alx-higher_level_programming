#!/usr/bin/python3
# a function that prints x elements of a list.
def safe_print_list(my_list=[], x=0):
    result = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            result += 1
        except:
            break
    print()
    return(result)
