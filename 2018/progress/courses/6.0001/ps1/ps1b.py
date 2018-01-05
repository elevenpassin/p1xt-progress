"""
Problem Set 1B

Calculate the number of months it will take to save up for the down payment
on your dream home. Account for a semi-annual raise.
"""


ANNUAL_SALARY = float(input("Enter your annual salary: "))
PORTION_SAVED = float(
    input("Enter the percent of your salary to save, as a decimal: "))
TOTAL_COST = float(input("Enter the cost of your dream home: "))
SEMI_ANNUAL_RAISE = float(input("Enter the semi-annual raise, as a decimal: "))
PORTION_DOWN_PAYMENT = 0.25
CURRENT_SAVINGS = 0
R = 0.04
MONTHLY_SALARY = ANNUAL_SALARY / 12
TOTAL_DOWN_PAYMENT = TOTAL_COST * PORTION_DOWN_PAYMENT
MONTHS = 0

while CURRENT_SAVINGS < TOTAL_DOWN_PAYMENT:
    MONTHS = MONTHS + 1
    CURRENT_SAVINGS = CURRENT_SAVINGS + \
        (CURRENT_SAVINGS * R / 12) + (MONTHLY_SALARY * PORTION_SAVED)
    if MONTHS % 6 == 0:
        MONTHLY_SALARY = MONTHLY_SALARY + (MONTHLY_SALARY * SEMI_ANNUAL_RAISE)

print("Number of months: " + str(MONTHS))
