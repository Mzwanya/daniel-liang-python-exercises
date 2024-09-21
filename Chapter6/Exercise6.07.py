def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    print("Years       Future years")
    for i in range(1, years + 1):
        futureValue = investmentAmount * ((1 + monthlyInterestRate) ** (12 * i))
        print(i, "\t\t\t", format(futureValue, ".2f"))


def main():
    investmentAmount = eval(input("The amount invested : "))
    interestRate = eval(input("Annual interest rate : "))
    futureInvestmentValue(investmentAmount, interestRate / 1200, 30)


main()
