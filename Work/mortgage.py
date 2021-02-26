# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_months = 0
extra_payment_start_month = input("What month will you start paying extra?")
extra_payment_end_month = input("What month will you stop paying extra?")
extra_payment = input("How much extra will you be paying?")

while principal > 0:
    
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    total_months += 1

    if ((total_months >= int(extra_payment_start_month)) and
    (total_months <= int(extra_payment_end_month))):
        principal -= int(extra_payment)
        total_paid += int(extra_payment)
    
    if principal < 0:
        total_paid += principal
        principal = 0

    print(total_months, round(total_paid, 2), round(principal, 2))

print(f"Total paid = {round(total_paid, 2)} over {total_months} months.")