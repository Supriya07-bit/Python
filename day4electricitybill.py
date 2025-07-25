units = int(input("Enter units used:"))
bill = 0

if units <= 100:
    bill = units * 1.5

elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2.5

else:
    bill = 100 * 1.5 + 100 * 2.5 + (units - 100) * 3.5

print(f"Your Electricity Bill Is: rs{bill:.2f}")