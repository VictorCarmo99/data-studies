# Python Exercise 15: Write a program that asks for the number of kilometers driven by a rented car and the number of days it was rented. Calculate the total price to pay, knowing that the car costs R$60 per day and R$0.15 per kilometer driven.

# Program introduction
print('\nWelcome! This program calculates the total rental cost of a car.'
      '\nYou just need to enter the number of days the car was rented and the kilometers driven.'
      '\nThe system will then calculate the final price based on a daily rate of R$60.00 and R$0.15 per kilometer')

# The user enters the number of days rented and the kilometers driven
days_rented = int(input('\nEnter the number of days the car was rented (numbers only): '))
km_driven = float(input('Enter the kilometers driven during that time: '))

# Calculate the total amount
cost = (days_rented * 60) + (km_driven * 0.15)

# Return the total amount to the user
print(f'The total amount to pay is: R${cost:.2f}')
