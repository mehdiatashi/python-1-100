# name = len(input("What is your name?"))
# new_name = str (name)
# print( "Your name has " + new_name + " characters." ) 
# 3 + 5
# 7 - 3
# 3 * 2
# 6 / 2
# 2 ** 3
# 2 ^ 3
# print(3 *(( 3 + 3) / 3) - 3)
# name =  "Your BMI"
# print(name)
# height = input("Enter your height in m :")
# weight = input("Enter your weight in kg :")
# bmi = int(weight) / float(height) **2
# print(round(bmi , 1))
# age = input("What is your current age? ")
# age_as_int = int(age)
# years_remaining = 60 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# month_remaining = years_remaining * 12
# final =(f"You have {years_remaining}years ,{days_remaining}days , {weeks_remaining}weeks, and {month_remaining}months left.")
# print(final)
hi = "Welcome to the tip calculato!"
print(hi)
money = float(input("What was the total bill? " ))
tip = int(input("What percentage tip would you like to give? 3, 10, or 15? "))
people = int(input("How many people to split the bill? "))
total = tip / 100 * money + money
print (total)
totall = total / people
print(totall)
