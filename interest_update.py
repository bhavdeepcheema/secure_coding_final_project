"""
Description: Module 3 Assignment 03
Author: Bhavdeep
Date: 02/20/2024
"""

import csv
import pprint

# Defining an empty dictionary to store the contents of the input file
account_balances = {}

# Open the input file named account_balances.txt in read mode using a context manager (with clause)
with open('account_balances.txt', 'r') as file:
    # Create a CSV reader object with pipe delimiter
    reader = csv.reader(file, delimiter='|')

    # Processing the data in the file
    for row in reader:
        account_number, balance_str = row
        # Converting balance to float
        balance = float(balance_str)
        # Adding teh contents of the input file to the dictionary
        account_balances[account_number] = balance

# Displaying the contents of the Dictionarybefore applying interest
        print("Curent Balance (Before Interest):")
        pprint.pprint(account_balances)
        