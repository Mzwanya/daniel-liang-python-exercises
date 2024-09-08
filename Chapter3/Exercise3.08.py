amount = int(input("Enter an amount, for example, 1156: "))
number_of_one_dollars = amount // 100
amount = amount % 100
number_of_quarters = amount // 25
amount = amount % 25
number_of_one_dimes = amount // 10
amount = amount % 10
number_of_one_nickels = amount // 5
amount = amount % 5
number_of_one_pennies = amount

print("Your amount", amount, "consists of\n",\
      "\t", number_of_one_dollars, "dollars\n", \
      "\t", number_of_quarters, "quarters\n", \
      "\t", number_of_one_dimes, "dimes\n", \
      "\t", number_of_one_nickels, "nickels\n", \
      "\t", number_of_one_pennies, "pennies")
