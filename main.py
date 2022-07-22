from random import randrange
import sys

def rand_num():
    dice_num = randrange(1, 7)
    return dice_num


def option():
    inp = str(input("Do you want to contuine (y or n): "))
    yes = 'y' or 'Y'
    no = 'n' or 'N'
    if inp == yes:
        print(rand_num())
    else:
        sys.exit()


def main():
    print("getting your dice number:")
    print("it is ", rand_num())
    while True:
        option()

__main__ = __name__

if __name__ == __main__:
    main()
