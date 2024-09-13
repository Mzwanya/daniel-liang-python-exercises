# Financials: currency exchange rate between U.S. dollars and Chinese Renminbi (RMB)

exchange_rate = eval(input("Enter the exchange rate from dollars to RMB: "))
conversion = int(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))

if conversion == 0:
    dollar_amount = eval(input("Enter the dollar amount: "))
    RMB = dollar_amount * exchange_rate
    print('$' + str(dollar_amount) + ' is ' + str(format(RMB, ".2f")) + ' yuan')
elif conversion == 1:
    RMB_amount = eval(input("Enter the RMB amount: "))
    dollars = RMB_amount / exchange_rate
    print(str(RMB_amount) + ' yuan is ' + '$' + str(format(dollars, ".2f")))
else:
    print("Incorrect input")
