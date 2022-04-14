import random
import array
import argparse

formatter = lambda prog: argparse.HelpFormatter(prog,max_help_position=52)
parser = argparse.ArgumentParser(formatter_class=formatter)
m = 'N'
parser = argparse.ArgumentParser(description='Simple password generator in Python')
parser.add_argument("-s", "--symbol", help="Include Symbols. (e.g. @#$%%)", action="store_true")
parser.add_argument("-i", "--include", help="Include Similar Characters (e.g. i, l, 1, L, o, 0, O)", action="store_true")
parser.add_argument("-l", "--length", help="Set password length", type=int, metavar=m)

if len(sys.argv)==1:
    parser.print_help()

args = parser.parse_args()


DEFAULT_LEN = 14
DIGITS = ['2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'j', 'k', 'm', 'n', 'p', 'q', 'r', 's',
                     't', 'u', 'v', 'w', 'x', 'y', 'z']
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'P', 'Q', 'R',
                     'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['']


def create_pwd():
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    for x in range(DEFAULT_LEN - 3):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
    password = ""
    for x in temp_pass_list:
        password = password + x
    print(f"\nNew password is: {password}\n")

if args.length:
    DEFAULT_LEN = args.length

if args.symbol:
    DEFAULT_LEN -= 1
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

if args.include:
    DIGITS += ["0", "1"]
    LOCASE_CHARACTERS += ["i", "l", "o"]
    UPCASE_CHARACTERS += ["L", "O"]

create_pwd()
