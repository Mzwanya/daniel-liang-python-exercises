from Chapter6.CH06Module import my_functions

print("Celsius\t\tFahrenheit  |  Fahrenheit\t\tCelsius")
celsuis = 40
fahr = 120
for i in range(1, 11):
    print(format(celsuis, ".2f"), format(" ", "8s"), format(my_functions.celsiusToFahrenheit(celsuis), ".2f"), end="\t|")
    print(format(" ", "3s"), format(fahr, ".2f"), format(" ", "8s"),
          format(my_functions.fahrenheitToCelsius(fahr), "-.2f"))
    celsuis -= 1
    fahr -= 10
