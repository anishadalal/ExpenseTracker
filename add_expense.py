import tkinter as tk
from tkinter import messagebox
from db import insert_expense
from datetime import date

def open_add_expense():
    def submit():
        d = entry_date.get()
        c = entry_category.get()
        desc = entry_description.get()
        a = entry_amount.get()

        if not d or not c or not a:
            messagebox.showwarning("Input error", "Date, Category and Amount are required")
            return
        try:
            insert_expense(d, c, desc, float(a))
            messagebox.showinfo("Success", "Expense Added")
            window.destroy()
        except:
            messagebox.showerror("Error", "Invalid data format")

    window = tk.Toplevel()
    window.title("Add Expense")

    tk.Label(window, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
    tk.Label(window, text="Category:").grid(row=1, column=0)
    tk.Label(window, text="Description:").grid(row=2, column=0)
    tk.Label(window, text="Amount:").grid(row=3, column=0)

    entry_date = tk.Entry(window)
    entry_date.insert(0, str(date.today()))
    entry_category = tk.Entry(window)
    entry_description = tk.Entry(window)
    entry_amount = tk.Entry(window)

    entry_date.grid(row=0, column=1)
    entry_category.grid(row=1, column=1)
    entry_description.grid(row=2, column=1)
    entry_amount.grid(row=3, column=1)

    tk.Button(window, text="Submit", command=submit).grid(row=4, column=0, columnspan=2, pady=10)
