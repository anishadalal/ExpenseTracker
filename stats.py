import matplotlib.pyplot as plt
from db import fetch_expenses
from collections import defaultdict

def show_stats():
    expenses = fetch_expenses()
    totals = defaultdict(float)
    for exp in expenses:
        totals[exp[2]] += exp[4]

    if not totals:
        print("No data to show.")
        return

    labels = list(totals.keys())
    values = list(totals.values())

    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Expenses by Category")
    plt.axis("equal")
    plt.show()
