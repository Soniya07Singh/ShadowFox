# CALCULATING EXPENSES 
my_expenses = {
    "Hotel": 1500,
    "Food": 1200,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 600
}

friend_expenses = {
    "Hotel": 1400,
    "Food": 400,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 450
}

# Calculate total expenses
my_total = sum(my_expenses.values()) #value is used to get values of the dictionary. sum is used to get the total sum of the value.
friend_total = sum(friend_expenses.values())

print(f"My total expenses: ₹{my_total}")
print(f"Friend's total expenses: ₹{friend_total}")

# Determine who spent more
if my_total > friend_total:
    print("You spent more overall.")
elif friend_total > my_total:
    print("Your partner spent more overall.")
else:
    print("Both spent the same amount.")

max_diff = 0
category_with_max_diff = ""    

for category in my_expenses:
    diff = abs(my_expenses[category] - friend_expenses[category])     #abs is used to get the absolute value of the difference.
    if diff > max_diff:
        max_diff = diff
        category_with_max_diff = category

print(f"The biggest difference in spending was in '{category_with_max_diff}' with a difference of ₹{max_diff}")

#-----------------------OUTPUT-----------------------
#My total expenses: ₹4100
#Friend's total expenses: ₹3250
#You spent more overall.
#The biggest difference in spending was in 'Food' with a difference of ₹800