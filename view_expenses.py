import tkinter as tk
from db import fetch_expenses

def open_view_expenses():
    window = tk.Toplevel()
    window.title("View Expenses")

    expenses = fetch_expenses()

    tk.Label(window, text="Date", width=15).grid(row=0, column=0)
    tk.Label(window, text="Category", width=15).grid(row=0, column=1)
    tk.Label(window, text="Description", width=20).grid(row=0, column=2)
    tk.Label(window, text="Amount", width=10).grid(row=0, column=3)

    for i, expense in enumerate(expenses, start=1):
        tk.Label(window, text=expense[1], width=15).grid(row=i, column=0)
        tk.Label(window, text=expense[2], width=15).grid(row=i, column=1)
        tk.Label(window, text=expense[3], width=20).grid(row=i, column=2)
        tk.Label(window, text=expense[4], width=10).grid(row=i, column=3)
