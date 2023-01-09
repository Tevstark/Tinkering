# Key in prices for
# Add prices in list of prices
# Prices separated by whitespace 
"""ADVANCED"""
# Instead of error in Wrong Query, cue try again.
# Start and exit like an application 
# Option to try again 
# Help menu on Navigation
"""Additional functionality ideas"""

import sys

print("\nPRICE CALCULATOR\n\n")

while True:


    prompt = input("\n\nFor instructions type in help. \n >>> ").lower()

    if prompt == "Start".lower():
        try:
            prices = input("\n\nKey in prices(Use comma between prices): ")
            input_list = prices.split(",")

            input_list = list(map(int, input_list))

        except ValueError:
            input("\nUse comma between prices\n\n")
            sys.exit(1)

        total = 0

        for price in input_list:
            total += price
        
        print(total)

    elif prompt == "Help".lower():
        print("""
            Start - Begin Application
            Help - Show Instructions
            Quit - Exit the application 
        """)
    elif prompt == "Quit".lower():
        break
    
else:
    sys.exit(1)