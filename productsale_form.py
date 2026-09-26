import tkinter as tk
from tkinter import messagebox
from productsale import ProductSale


def productsale_form():

    obj = ProductSale()

    window = tk.Toplevel()
    window.title("Product Sale Management")
    window.geometry("500x700")

    tk.Label(
        window,
        text="Product Sale Management",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # Bill ID
    tk.Label(window, text="Bill ID").pack()
    bill_entry = tk.Entry(window, width=35)
    bill_entry.pack(pady=2)

    # Product ID
    tk.Label(window, text="Product ID").pack()
    product_entry = tk.Entry(window, width=35)
    product_entry.pack(pady=2)

    # Quantity
    tk.Label(window, text="Quantity").pack()
    quantity_entry = tk.Entry(window, width=35)
    quantity_entry.pack(pady=2)

    # Rate
    tk.Label(window, text="Rate").pack()
    rate_entry = tk.Entry(window, width=35)
    rate_entry.pack(pady=2)

    # Amount
    tk.Label(window, text="Amount").pack()
    amount_entry = tk.Entry(window, width=35)
    amount_entry.pack(pady=2)

    # Product Sale ID
    tk.Label(window, text="Product Sale ID (For Update/Delete)").pack()
    id_entry = tk.Entry(window, width=35)
    id_entry.pack(pady=2)

    # ---------------- Clear ---------------- #

    def clear_fields():
        id_entry.delete(0, tk.END)
        bill_entry.delete(0, tk.END)
        product_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        rate_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

    # ---------------- Insert ---------------- #

    def insert():

        if (
            bill_entry.get() == "" or
            product_entry.get() == "" or
            quantity_entry.get() == "" or
            rate_entry.get() == "" or
            amount_entry.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required")
            return

        obj.insert_productsale(
            bill_entry.get(),
            product_entry.get(),
            quantity_entry.get(),
            rate_entry.get(),
            amount_entry.get()
        )

        messagebox.showinfo("Success", "Product Sale Inserted Successfully")
        clear_fields()

    # ---------------- View ---------------- #

    def view():

        rows = obj.view_productsale()

        output.delete("1.0", tk.END)

        if len(rows) == 0:
            output.insert(tk.END, "No Product Sale Found")
            return

        for row in rows:

            output.insert(
                tk.END,
                f"Product Sale ID : {row.ProductSaleID}\n"
                f"Bill ID : {row.BillID}\n"
                f"Product ID : {row.ProductID}\n"
                f"Quantity : {row.Quantity}\n"
                f"Rate : {row.Rate}\n"
                f"Amount : {row.Amount}\n"
                "----------------------------------------\n"
            )

    # ---------------- Update ---------------- #

    def update():

        if id_entry.get() == "":
            messagebox.showerror("Error", "Enter Product Sale ID")
            return

        obj.update_productsale(
            id_entry.get(),
            bill_entry.get(),
            product_entry.get(),
            quantity_entry.get(),
            rate_entry.get(),
            amount_entry.get()
        )

        messagebox.showinfo("Success", "Product Sale Updated Successfully")
        clear_fields()

    # ---------------- Delete ---------------- #

    def delete():

        if id_entry.get() == "":
            messagebox.showerror("Error", "Enter Product Sale ID")
            return

        obj.delete_productsale(id_entry.get())

        messagebox.showinfo("Success", "Product Sale Deleted Successfully")
        clear_fields()

    # ---------------- Buttons ---------------- #

    tk.Button(
        window,
        text="Insert",
        width=20,
        bg="lightgreen",
        command=insert
    ).pack(pady=5)

    tk.Button(
        window,
        text="View",
        width=20,
        bg="lightblue",
        command=view
    ).pack(pady=5)

    tk.Button(
        window,
        text="Update",
        width=20,
        bg="orange",
        command=update
    ).pack(pady=5)

    tk.Button(
        window,
        text="Delete",
        width=20,
        bg="tomato",
        command=delete
    ).pack(pady=5)

    tk.Button(
        window,
        text="Clear",
        width=20,
        command=clear_fields
    ).pack(pady=5)

    # ---------------- Output ---------------- #

    output = tk.Text(window, width=60, height=12)
    output.pack(pady=10)