import tkinter as tk
from add_expense import open_add_expense
from view_expenses import open_view_expenses
from stats import show_stats
from db import init_db

init_db()

root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("300x200")

tk.Label(root, text="Welcome to Expense Tracker", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Add Expense", command=open_add_expense, width=25).pack(pady=5)
tk.Button(root, text="View Expenses", command=open_view_expenses, width=25).pack(pady=5)
tk.Button(root, text="View Statistics", command=show_stats, width=25).pack(pady=5)

root.mainloop()
