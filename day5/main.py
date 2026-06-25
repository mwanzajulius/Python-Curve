#Python loops= for loop and also range function
#use Ctrl + Alt + L to cleans up spacing and fixes indentation errors
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my Password Generator!")
number_of_letters = int(input("Enter the number of letters: "))
number_of_symbols = int(input("Enter the number of symbols: "))
number_of_numbers = int(input("Enter the number of numbers: "))
password = []
for char in range(number_of_letters):
    password.append(random.choice(letters))

for char in range(number_of_symbols):
    password.append(random.choice(symbols))

for char in range(number_of_numbers):
    password.append(random.choice(numbers))

print(password)  # This is to print the password before shuffling
random.shuffle(password)
print(password)  # Password after shuffling

passwordNew = " "
for char in password:
    passwordNew += char

print(f"The password is {passwordNew}")
