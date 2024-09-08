# Taking user inputs
employee_name = input("Enter employee's name: ")
number_of_hours_worked_per_week = eval(input("Enter the number of hours worked in a week: "))
hourly_pay_rate = eval(input("Enter the hourly pay rate: "))
federal_tax_withholding_rate = eval(input("Enter the federal pay rate: "))
state_tax_withholding_rate = eval(input("Enter the state tax withhholding rate: "))

# Calculations
gross_pay = hourly_pay_rate * number_of_hours_worked_per_week
federal_withholding = federal_tax_withholding_rate * gross_pay
state_withholding = state_tax_withholding_rate * gross_pay
total_deductions = federal_withholding + state_withholding
net_pay = gross_pay - total_deductions

# Display the results
print("\n")
print("Employee Name:", employee_name,"\n" \
      "Hours Worked: ", number_of_hours_worked_per_week, "\n" \
      "Pay Rate: ", "$" + str(hourly_pay_rate), "\n" \
      "Gross Pay: ", "$" + str(gross_pay), "\n" \
      "Deductions: ", "\n"\
      f"\t Federal Withdrawing ({str(federal_tax_withholding_rate * 100) + "%"}):", "$" + str(federal_withholding), "\n" \
      f"\t State Withholding ({str(state_tax_withholding_rate * 100) + "%"}):", "$" + str(state_withholding), "\n" \
      f"\t Total Deductions:", "$" + str(total_deductions), "\n" \
      "Net Pay:", "$" + str(net_pay))
