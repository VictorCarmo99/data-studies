# Python Exercise 13: Create an algorithm that reads an employee's salary and shows the new salary with a 15% increase.

# Program introduction
print("\nThis program calculates a 15% salary increase."
      "\nThe user enters the current salary of an employee, and the system returns the updated salary after applying the increase."
      "\nIt's a simple and efficient tool for payroll calculations or HR system simulations.")

# The user enters the Original Salary
original_salary = float(input('\nEnter the employee\'s current salary: $'))

# The Algorithm calculates the new salary with 15% increase
increased_salary = original_salary * 1.15

#Returns the new salary for the user
print(f'\nThe new salary with an increase of 15% is: ${increased_salary:.2f}')
