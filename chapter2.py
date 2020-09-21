#transactionsThisMonth is assigned an int
transactionsThisMonth = 1

#accountBalance is assigned a float
accountBalance = 555.55

#firstname, lastname, accountNUmber, and pin are assigned strings
firstName = "Marc"
lastName = "Hauschildt"
accountNumber = "k0519415"
pin = "1234"

#active is assigned a boolean
active = True

# Add these lines after the "active = True" statement
PROCESSING_FEE = 2.00
INTEREST_RATE = 0.019

pinInput = str(input("What is your PIN? ")) # Add this line after the "INTEREST_RATE = 0.019" statement

# add the remaining lines after the "Your account balance is..." statement
withdrawInput = float(input("\nHow much would you like to withdraw? "))

# Place this code above the "Rate your experience" input
print("This transaction includes a $" + format(PROCESSING_FEE, ".2f"), "processing fee.")
accountBalance = accountBalance - withdrawInput - PROCESSING_FEE
interestEarned = accountBalance * (INTEREST_RATE / 12)
print("Congratulations, your account earned $" + format(interestEarned, ".2f"), "in interest this month.")
accountBalance = accountBalance + interestEarned
print("\nYour updated account balance is $" + format(accountBalance, "5.2f"))
transactionsThisMonth += 1
print("You have made", str(transactionsThisMonth), "transactions this month.")

ratingInput = int(input("\nRate your experience today (1-Bad, 5-Great): "))
print(type(pinInput), type(withdrawInput), type(ratingInput))

# Don't do this when you want to add two numbers. The + sign means concatenate when dealing with strings
num1 = input("Enter a number: ")
print(num1)
num2 = input("Enter another number: ")
print(num1 + num2)

# Do this instead
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(num1 + num2)

a = 5
b = 2
c = 3
smallest = min(a,b,c)  # smallest is assigned 2
largest = max(a,b,c)  # largest is assigned 5
print("Smallest:\t" + str(smallest))
print("Largest:\t" + str(largest))