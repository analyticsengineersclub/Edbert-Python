# calc.py

import argparse

# Import package to handle decimal precision of division subcommand set precision to 4 decimal places
from decimal import *

getcontext().prec = 4

parser = argparse.ArgumentParser(description="CLI Calculator")

subparsers = parser.add_subparsers(help="sub-command help", dest="command")

# Exercse 1: Add any number of args to add command
# Docs https://docs.python.org/3/library/argparse.html#nargs
add = subparsers.add_parser("add", help="add integers")
add.add_argument("ints_to_sum", nargs="*", type=int)

sub = subparsers.add_parser("sub", help="subtract integers")
sub.add_argument("ints_to_sub", nargs="*", type=int)

# Testing in Python lecture
def aec_subtract(ints_to_sub):
    our_sub = ints_to_sub[0] - ints_to_sub[1]
    # Test Exercise 2
    if len(ints_to_sub) > 2:
        raise Exception("Too many arguments")
        # the print statement does not work - Python extension indicates not reachable
        print("Exception: You inputted too many arguments")
    elif our_sub < 0:
        our_sub = 0
    print(f"The subtracted result of values is: {our_sub}")
    return our_sub


# Exercise 2A: Add subcommand for multiplication
multiply = subparsers.add_parser("multiply", help="multiply two integers")
multiply.add_argument("ints_to_multiply", nargs=2, type=int)

# Exercise 2B: Add subcommand for division
divide = subparsers.add_parser("divide", help="divide two integers")
divide.add_argument("ints_to_divide", nargs="*", type=int)

# Testing in Python lecture - Exercise 1
def aec_divide(ints_to_divide):
    # Testing in Python - Exercise 3 too many arg
    # Testing in Python - Exercise 2 TDD
    if len(ints_to_divide) > 2:
        raise Exception("Too many arguments")
    elif len(ints_to_divide) == 2:
        try:
            our_divide = ints_to_divide[0] / ints_to_divide[1]
            print(f"The division result of values is: {our_divide}")
            return our_divide
        except ZeroDivisionError:
            print("Division by Zero - retry with different arguments")
            return 0


if __name__ == "__main__":
    args = parser.parse_args()

    if args.command == "add":
        our_sum = sum(args.ints_to_sum)

    if args.command == "sub":
        aec_subtract(args.ints_to_sub)

    if args.command == "multiply":
        our_multiply = args.ints_to_multiply[0] * args.ints_to_multiply[1]
        print(f"The product of values is: {our_multiply}")

    if args.command == "divide":
        aec_divide(args.ints_to_divide)


# parser.add_argument("ints_to_sum", nargs=2, type=int)
