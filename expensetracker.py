# Expense tracker

from datetime import date

expenses = []   #empty list to store expenses

motive = input ("What are the expenses for : ")

while True:
    # User se input lo
    print("--- Expense Add Karo ---")
    amount = float(input("Amount : Rs "))
    category = input("Category (Food/Travel/Shopping): ")
    description = input("Description: ")


    # Dictionary banao — same format
    expense = {
        "date":        str(date.today()),   # Aaj ki date automatically
        "amount":      amount,
        "category":    category,
        "description": description
    }

    #expense add karo list mein
    expenses.append(expense)

    add = input("Wanna add more expenses (Y/N)- ")
    if add.lower()== "y":
        continue
    else :
        break

# Saare expenses print karo
print("\n--- Your Expenses for:", motive, "---")

for i, exp in enumerate(expenses, 1):
    print(i, ".", exp["date"], "|", exp["category"], "|", "Rs", exp["amount"], "|", exp["description"])

print("--------------------------------------------------------")
# Total print karo
total = sum(exp["amount"] for exp in expenses)
print("Total expenses:", len(expenses))
print("Total amount: Rs", total)
