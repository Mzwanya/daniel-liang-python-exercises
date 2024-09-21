from CH06Module import MyFunctions

print("Celsius\t\tFahrenheit  |  Fahrenheit\t\tCelsius")
celsuis = 40
fahr = 120
for i in range(1, 11):
    print(format(celsuis, ".2f"), format(" ", "8s"), format(MyFunctions.celsiusToFahrenheit(celsuis), ".2f"), end="\t|")
    print(format(" ", "3s"), format(fahr, ".2f"), format(" ", "8s"),
          format(MyFunctions.fahrenheitToCelsius(fahr), "-.2f"))
    celsuis -= 1
    fahr -= 10
