import re

with open("input.txt") as file:
    input_lines = file.read().splitlines()


def check_password(password_line):
    password_list = re.split('[- :]', password_line)
    min_number = int(password_list[0])
    max_number = int(password_list[1])
    char = password_list[2][0]
    word = password_list[4]
    return min_number <= word.count(char) <= max_number


valid_passwords = 0


for line in input_lines:
    if check_password(line):
        valid_passwords += 1

print(f"There are total of {valid_passwords} valid passwords")




