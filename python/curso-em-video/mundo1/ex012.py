# From now on, all of my exercises in this course will be written in english to make my portfolio more professional and better classified.

# Python Exercise 12: Create an algorithm that reads the price of a product and shows its new price with a 5% discount.

# Program introduction
print('\nHello! This algorithm automaticallu calculates a 5% discount on the price of a product'
      '\nThe user enters the original price, and the system returns the final price with the discount applied.'
      '\nSimple, fast, and efficient for use in sales systems or basic calculations.\n')

# The user enters the original product price
original_price = float(input('Enter the product price: $'))

# The algorithm calculates a 5% discount and subtracts it from the original price.
discounted_price = original_price - (original_price * 0.05)

# The final price with discount is displayed to the user
print('The price after a 5% discount is: ${:.2f}'.format(discounted_price))
