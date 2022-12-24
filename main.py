import random
import string
from tkinter import *

root = Tk()

entryScale = Scale(root, from_=8, to=30, length=300, orient=HORIZONTAL)
entryScale.grid(row=2, column=0)

password_field = Text(root, width=35, height=1)
password_field.grid(row=3, column=0)


def display_password():
    n = entryScale.get()
    password = password_construction(n)
    password_field = Text(root, width=35, height=1)  # there is a problem here, keeps creating new text field over the old one
    password_field.grid(row=3, column=0)
    password_field.insert(END, chars=password)


def password_construction(n):
    list_of_lists = [] # we will create each list and append it to list_of_lists

    # list of numbers 0-9
    list_numbers = [x for x in range(10)]
    str1 = " ".join(str(e) for e in list_numbers)
    list_numbers = str1.split()
    list_of_lists.append(list_numbers)

    # list of letters
    string_small_letters = "abcdefghijklmnopqrstuvwxyz"
    string_small_letters = " ".join(string_small_letters)
    list_small_letters = string_small_letters.split()
    list_of_lists.append(list_small_letters)

    # list of capital letters
    string_capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string_capital_letters = " ".join(string_capital_letters)
    list_capital_letters = string_capital_letters.split()
    list_of_lists.append(list_capital_letters)

    # list of symbols
    symbols_string = "!#$%&()*+,-./:;<=>?@[\]^_{|}~"
    symbols_string = " ".join(symbols_string)
    list_symbols = symbols_string.split()
    list_of_lists.append(list_symbols)

    result = []
    for i in range(n):
        result.append("-1")
    for i in range(n):
        if result[i] == "-1":
            random_list = list_of_lists[i % 4]
            result[i] = random_list[random.randint(0, len(random_list)-1)]  # pick an element in a list randomly, O(n)

    random.shuffle(result)  # shuffle because the for loop creates a pattern, O(n)
    password_value_return = ''.join(result)
    password_value_return = password_value_return.strip(" ")  # remove unwanted spaces
    return password_value_return


titleOfProgram = Label(root, text="Password Generator")
titleOfProgram.grid(row=0, column=0)  # a title in the window, label

promptUser = Label(root, text="use the scale to select password length!")
promptUser.grid(row=1, column=0)  # a prompt (label) for user to enter the length of the password


generateButton = Button(root, text="Generate Password", pady=10, command=display_password)
generateButton.grid(row=4, column=0)  # a button to generate the password


root.mainloop()
