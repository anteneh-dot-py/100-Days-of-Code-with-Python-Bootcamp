import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# password_length=nr_letters+nr_numbers +nr_symbols
pass_letter=[]
pass_symbol=[]
pass_number=[]
for i in range(nr_letters):
    pass_letter+=letters[i]
for i in range(nr_symbols):
    pass_symbol+=symbols[i]
for i in range(nr_numbers):
    pass_number+=numbers[i]
easy_password=pass_letter + pass_symbol+pass_number
password_choice=input("Easy or Hard Password:E or H").upper()
if password_choice=="E":
    print("Easy Password")
    for easy_pass in easy_password:
        print(easy_pass,end="")
    print("\n")
else:
    hard_password=""
    pass_length=len(easy_password)
    for char in easy_password:
        index=random.randint(0,pass_length-1)
        easy_password.index(easy_password[index])
        hard_password+=easy_password[index]
        
    print("Hard Password")
    for hard_letter in hard_password:
        print(hard_letter,end="")
    print("\n")


