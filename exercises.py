'''
Question 7. Miles-Per-Gallon
Input(s): 
- miles_driven, float, from the user 
- gallons_used, float, from the user
Process(es): 
- miles_per_gallon, float, miles_driven / gallons_used
Output(s): 
- miles_per_gallon
'''
# Type your code here

# Inputs
miles_driven = float(input('How many miles did you drive?'))
gallons_used = float(input('How many gallons of gas did you use?'))

# Process
miles_per_gallon = float(miles_driven / gallons_used)

# Output
print('You used ' + format(miles_per_gallon, '.2f') + ' miles per gallon.')
'''
Question 9. Celsius to Fahrenheit Temperature Converter
Input(s): 
- celsius, float, from the user
Process(es): 
- fahrenheit, float, ((celsius * 9/5) + 32)
Output(s): 
- fahrenheit, 
'''
# Type your code here

# Input
celsius = float(input('Input Celsius Temperature.\n'))

# Process
fahrenheit = float(((celsius/5)*9)+32)

# Output
print('Fahrenheit is ' + format(fahrenheit, '.1f') + ' degrees.')
'''
Question 11. Male and Female Percentages
Input(s):
- males, float, from the user
- females, float, from the user
Process(es): 
- total, float, males + females
- male_percent, float, males / total
- female_percent, float, females / total
Output(s): 
- male_percent
- female_percent
'''
# Type your code here

# Inputs
males = float(input('How many males do you have in the class?'))
females = float(input('How many females do you have in the class?'))

# Process
total = float(males + females)
male_percent = float((males / total) * 100)
female_percent = float((females / total) * 100)

#Outputs
print('The total percent of males is ' + format(male_percent, '.2f') + '%')
print('The total percent of females is ' + format(female_percent, '.2f') + '%')

'''
Question 12. Stock Transaction Program
Input(s): 
  - shares_purchased, int, from the user, 2000
  - purchase_price, float, from the user, 40.00
  - COMMISSION_RATE, float, constant, 0.03
  - shares_sold, int, from the user, 2000
  - sale_price, float, from the user, 42.75
Process(es): 
  - amount_paid, float, shares_purchased * purchase_price, 80000.00
  - commission_1, float, amount_paid * commission_rate, 2400.00
  - amount_sold, float, shares_sold * sale_price, 85500.00
  - commission_2, float, amount_sold * commission_rate, 2565.00
  - earnings, float, amount_sold - amount_paid - commission_1 - commission_2, 535.00
Output(s):
  - amount_paid
  - commission_1
  - amount_sold
  - commission_2
  - earnings
'''
# Type your code here
COMMISSION_RATE = float(0.03)

# Inputs
shares_purchased = int(input("How many shares have you purchased?"))
purchase_price = float(input("How much did you buy each share for?"))
shares_sold = int(input("How many shares have you sold?"))
sale_price  = float(input("How much did you sell each share for?"))

# Processes
amount_paid = float(shares_purchased * purchase_price)
commision_1 = float(amount_paid * COMMISSION_RATE)
amount_sold = float(shares_sold * sale_price)
commision_2 = float(amount_sold * COMMISSION_RATE)
earnings = float(amount_sold - amount_paid - commision_1 - commision_2)


# Outputs
print("You paid $" + format(amount_paid, ".2f") + " for " + str(shares_purchased) + " stocks!")
print("You had to pay your broker $" + (format(commision_1, ".2f")) + ".")
print("You sold all of your shares for $" + (format(amount_sold, ".2f")) + "!")
print("You had to pay your broker again for $" + (format(commision_2, ".2f")) + "!")
print("You made $"  + (format(earnings, ".2f")) + " overall!")