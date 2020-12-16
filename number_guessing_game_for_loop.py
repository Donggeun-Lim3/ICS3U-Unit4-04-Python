#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This program uses a try statement

import random


def main():
    random_number = random.randint(0, 9)
    while True:
        integer_as_string = input("Enter your number : ")
        print("")

        try:
            integer_as_number = int(integer_as_string)

            if random_number == integer_as_number:
                print("You are right!")
                print("random number is {}".format(random_number))
                break
            else:
                print("you are wrong")

        except Exception:
            print("This was not an integer")


if __name__ == "__main__":
    main()
