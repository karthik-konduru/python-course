import random
characters ="abcdefghijklmnopqrstuvwxyz"
characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters += "12345678890"
characters += "!@#$%&*₹"
password = ""
length = int(input())
for i in range(length):
    ch =random.choice(characters)
    password += ch
print(password)