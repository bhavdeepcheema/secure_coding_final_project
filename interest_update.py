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

# Iterate through the dictionary of bank records to calculate and update the balances with interest/charges
        
for account_number, balance in account_balances.items():
    if balance > 0:
        if balance < 1000:
            interest_rate = 0.01
        elif balance < 6000:
            interest_rate = 0.025
        else:
            interest_rate = 0.05
    else:
        interest_rate = 0.1

    # Applying mothly interest or charge
    interest = (balance * interest_rate) / 12
    balance += interest

    # Updating the balance in the Dictionary
    account_balances[account_number] = balance

# Displaying the contents of the Dictionary after applying interest
print("\nBalances After Applying Interest/Charges:") 
pprint.pprint(account_balances)

