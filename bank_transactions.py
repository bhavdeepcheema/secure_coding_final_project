"""
Description: Module 3 Assignment 03
Author: Bhavdeep
Date: 02/20/2024
"""

import os
from time import sleep
import random
import locale

# Setting the locale for currency formatting
locale .setlocale(locale.LC_ALL, '')

# Defining transaction options
transactions_options = {"D", "W", "Q"}

# Generating random balance
random_balance = float(random.randint(-1000, 10000))
bank_balance = float(random_balance)

# Function to display the interface
def display_interface(balance):
    print("*" * 40)
print("{:^40}".format("PIXELL RIVER FINANCIAL"))
print("{:^40}".format("ATM Simulator"))
print("{:^40}".format(f"Your current balance is: {locale.currency(random_balance,grouping=True)}"))
print()
print("{:^40}".format("Desposit:D"))
print("{:^40}".format("Withdraw:W"))
print("{:^40}".format("Quit:Q"))
print("*" *40)

