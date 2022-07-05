import re
pattern="^4[0-9]{12}(?:[0-9]{3})?$"
check_valid=lambda card_number: re.match(pattern,card_number)
valid=check_valid(input("Enter a visa credit card number"))
if valid:
    print("Valid")
else:
    print("Invalid")