
import json
import os
from datetime import datetime

FILE_NAME = "transactions.json"


# Load transactions from JSON
def load_transactions():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


# Save transactions to JSON
def save_transactions(transactions):
    with open(FILE_NAME, "w") as file:
        json.dump(transactions, file, indent=4)


# Generate unique transaction ID
def generate_transaction_id(transactions):
    if not transactions:
        return 1

    return max(t["id"] for t in transactions) + 1


# Get valid amount from user
def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero!")
                continue

            return round(amount, 2)

        except ValueError:
            print("Please enter a valid numeric amount.")


# Add income or expense
def add_transaction(transactions, transaction_type):
    print(f"\n========== ADD {transaction_type.upper()} ==========")

    amount = get_amount()

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty!")
        return

    description = input("Enter description: ").strip()

    if not description:
        description = "No description"

    transaction = {
        "id": generate_transaction_id(transactions),
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    transactions.append(transaction)
    save_transactions(transactions)

    print("\nTransaction added successfully!")


# View all transactions
def view_transactions(transactions):
    if not transactions:
        print("\nNo transactions found.")
        return

    print("\n========== TRANSACTION HISTORY ==========")

    for transaction in transactions:
        print(f"\nID: {transaction['id']}")
        print(f"Type: {transaction['type']}")
        print(f"Amount: {transaction['amount']:.2f}")
        print(f"Category: {transaction['category']}")
        print(f"Description: {transaction['description']}")
        print(f"Date: {transaction['date']}")

    print("\n=========================================")


# Calculate total income
def calculate_income(transactions):
    return sum(
        t["amount"]
        for t in transactions
        if t["type"] == "income"
    )


# Calculate total expenses
def calculate_expenses(transactions):
    return sum(
        t["amount"]
        for t in transactions
        if t["type"] == "expense"
    )


# Display total income
def view_total_income(transactions):
    total = calculate_income(transactions)

    print(f"\nTotal Income: {total:.2f}")


# Display total expenses
def view_total_expenses(transactions):
    total = calculate_expenses(transactions)

    print(f"\nTotal Expenses: {total:.2f}")


# Display current balance
def view_balance(transactions):
    income = calculate_income(transactions)
    expenses = calculate_expenses(transactions)

    balance = income - expenses

    print("\n========== ACCOUNT BALANCE ==========")
    print(f"Total Income:   {income:.2f}")
    print(f"Total Expenses: {expenses:.2f}")
    print("-------------------------------------")
    print(f"Current Balance: {balance:.2f}")
    print("=====================================")


# Filter transactions by category
def filter_by_category(transactions):
    if not transactions:
        print("\nNo transactions available.")
        return

    category = input("\nEnter category to search: ").strip().lower()

    filtered = [
        t for t in transactions
        if t["category"].lower() == category
    ]

    if not filtered:
        print("No transactions found in this category.")
        return

    print(f"\n========== {category.upper()} TRANSACTIONS ==========")

    for transaction in filtered:
        print(
            f"ID: {transaction['id']} | "
            f"{transaction['type'].title()} | "
            f"Amount: {transaction['amount']:.2f} | "
            f"Date: {transaction['date']}"
        )


# Generate monthly summary
def monthly_summary(transactions):
    if not transactions:
        print("\nNo transactions available.")
        return

    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid format! Use YYYY-MM (e.g. 2026-11).")
        return

    monthly_transactions = [
        t for t in transactions
        if t["date"].startswith(month)
    ]

    if not monthly_transactions:
        print("\nNo transactions found for this month.")
        return

    income = calculate_income(monthly_transactions)
    expenses = calculate_expenses(monthly_transactions)

    print(f"\n========== SUMMARY: {month} ==========")
    print(f"Transactions: {len(monthly_transactions)}")
    print(f"Total Income: {income:.2f}")
    print(f"Total Expenses: {expenses:.2f}")
    print("-------------------------------------")
    print(f"Monthly Balance: {income - expenses:.2f}")
    print("=====================================")


# Delete transaction
def delete_transaction(transactions):
    if not transactions:
        print("\nNo transactions available.")
        return

    view_transactions(transactions)

    try:
        transaction_id = int(input("\nEnter transaction ID to delete: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    for transaction in transactions:
        if transaction["id"] == transaction_id:
            transactions.remove(transaction)
            save_transactions(transactions)

            print("\nTransaction deleted successfully!")
            return

    print("\nTransaction not found!")


# Display main menu
def display_menu():
    print("\n====================================")
    print("       PERSONAL EXPENSE TRACKER")
    print("====================================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Total Income")
    print("5. View Total Expenses")
    print("6. View Current Balance")
    print("7. Filter by Category")
    print("8. Monthly Summary")
    print("9. Delete Transaction")
    print("10. Exit")
    print("====================================")


# Main application
def main():
    transactions = load_transactions()

    while True:
        display_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_transaction(transactions, "income")

        elif choice == "2":
            add_transaction(transactions, "expense")

        elif choice == "3":
            view_transactions(transactions)

        elif choice == "4":
            view_total_income(transactions)

        elif choice == "5":
            view_total_expenses(transactions)

        elif choice == "6":
            view_balance(transactions)

        elif choice == "7":
            filter_by_category(transactions)

        elif choice == "8":
            monthly_summary(transactions)

        elif choice == "9":
            delete_transaction(transactions)

        elif choice == "10":
            print("\nThank you for using Personal Expense Tracker!")
            break

        else:
            print("\nInvalid option! Please select 1-10.")


if __name__ == "__main__":
    main()