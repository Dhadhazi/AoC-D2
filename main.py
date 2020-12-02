import re

with open("input.txt") as file:
    input_lines = file.read().splitlines()


# PART ONE
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

print(f"There are total of {valid_passwords} Part One valid passwords")


# PART TWO
def check_password_position(password_line):
    password_list = re.split('[- :]', password_line)
    position1 = int(password_list[0])-1
    position2 = int(password_list[1])-1
    char = password_list[2][0]
    word = password_list[4]
    return (word[position1] == char or word[position2] == char) and word[position1] != word[position2]


valid_passwords = 0

for line in input_lines:
    if check_password_position(line):
        valid_passwords += 1

print(f"There are total of {valid_passwords} Part Two valid passwords")