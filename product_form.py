import tkinter as tk
from tkinter import messagebox
from product import Product


def product_form():

    obj = Product()

    window = tk.Toplevel()
    window.title("Product Management")
    window.geometry("450x650")

    tk.Label(
        window,
        text="Product Management",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # Product Name
    tk.Label(window, text="Product Name").pack()
    name_entry = tk.Entry(window, width=35)
    name_entry.pack(pady=2)

    # Brand
    tk.Label(window, text="Brand").pack()
    brand_entry = tk.Entry(window, width=35)
    brand_entry.pack(pady=2)

    # Price
    tk.Label(window, text="Price").pack()
    price_entry = tk.Entry(window, width=35)
    price_entry.pack(pady=2)

    # Stock
    tk.Label(window, text="Stock").pack()
    stock_entry = tk.Entry(window, width=35)
    stock_entry.pack(pady=2)

    # Product ID
    tk.Label(window, text="Product ID (For Update/Delete)").pack()
    id_entry = tk.Entry(window, width=35)
    id_entry.pack(pady=2)

    # ---------------- Clear ---------------- #

    def clear_fields():
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        brand_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        stock_entry.delete(0, tk.END)

    # ---------------- Insert ---------------- #

    def insert():

        if (
            name_entry.get() == "" or
            brand_entry.get() == "" or
            price_entry.get() == "" or
            stock_entry.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required")
            return

        obj.insert_product(
            name_entry.get(),
            brand_entry.get(),
            price_entry.get(),
            stock_entry.get()
        )

        messagebox.showinfo("Success", "Product Inserted Successfully")
        clear_fields()

    # ---------------- View ---------------- #

    def view():

        rows = obj.view_product()

        output.delete("1.0", tk.END)

        if len(rows) == 0:
            output.insert(tk.END, "No Product Found")
            return

        for row in rows:

            output.insert(
                tk.END,
                f"Product ID : {row.ProductID}\n"
                f"Product Name : {row.ProductName}\n"
                f"Brand : {row.Brand}\n"
                f"Price : {row.Price}\n"
                f"Stock : {row.Stock}\n"
                "----------------------------------------\n"
            )

    # ---------------- Update ---------------- #

    def update():

        if id_entry.get() == "":
            messagebox.showerror("Error", "Enter Product ID")
            return

        obj.update_product(
            id_entry.get(),
            name_entry.get(),
            brand_entry.get(),
            price_entry.get(),
            stock_entry.get()
        )

        messagebox.showinfo("Success", "Product Updated Successfully")
        clear_fields()

    # ---------------- Delete ---------------- #

    def delete():

        if id_entry.get() == "":
            messagebox.showerror("Error", "Enter Product ID")
            return

        obj.delete_product(id_entry.get())

        messagebox.showinfo("Success", "Product Deleted Successfully")
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

    output = tk.Text(window, width=55, height=12)
    output.pack(pady=10)