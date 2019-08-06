
print('this is nester')


def print_lol(li, level = 0):
    for l in li:
        if isinstance(l, list):
            print_lol(l, level)
        else:
            print(l)
    
# function is not correct, just for fun
