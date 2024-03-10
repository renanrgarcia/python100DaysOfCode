# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# letters_chosen = []
# for n in range(nr_letters):
#     picked_letter = letters[random.randint(0, len(letters) - 1)]
#     while picked_letter in letters_chosen:
#         picked_letter = letters[random.randint(0, len(letters) - 1)]
#     letters_chosen.append(letters[random.randint(0, len(letters) - 1)])


# symbols_chosen = []
# for n in range(nr_symbols):
#     picked_symbol = symbols[random.randint(0, len(symbols) - 1)]
#     while picked_symbol in symbols_chosen:
#         picked_symbol = symbols[random.randint(0, len(symbols) - 1)]
#     symbols_chosen.append(symbols[random.randint(0, len(symbols) - 1)])


# numbers_chosen = []
# for n in range(nr_numbers):
#     picked_number = numbers[random.randint(0, len(numbers) - 1)]
#     while picked_number in numbers_chosen:
#         picked_number = numbers[random.randint(0, len(numbers) - 1)]
#     numbers_chosen.append(picked_number)

# password_list = letters_chosen + symbols_chosen + numbers_chosen
# password = ''
# for char in password_list:
#     password += char
# print(f'Here is your password: {password}')

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
letters_chosen = []
for n in range(nr_letters):
    picked_letter = letters[random.randint(0, len(letters) - 1)]
    while picked_letter in letters_chosen:
        picked_letter = letters[random.randint(0, len(letters) - 1)]
    letters_chosen.append(picked_letter)


symbols_chosen = []
for n in range(nr_symbols):
    picked_symbol = symbols[random.randint(0, len(symbols) - 1)]
    while picked_symbol in symbols_chosen:
        picked_symbol = symbols[random.randint(0, len(symbols) - 1)]
    symbols_chosen.append(picked_symbol)


numbers_chosen = []
for n in range(nr_numbers):
    picked_number = numbers[random.randint(0, len(numbers) - 1)]
    while picked_number in numbers_chosen:
        picked_number = numbers[random.randint(0, len(numbers) - 1)]
    numbers_chosen.append(picked_number)

password_list = letters_chosen + symbols_chosen + numbers_chosen
random.shuffle(password_list)

password = ''
for char in password_list:
    password += char
print(f'Here is your password: {password}')
