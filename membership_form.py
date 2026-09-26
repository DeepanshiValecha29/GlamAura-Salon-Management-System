import tkinter as tk
from tkinter import messagebox
from membership import Membership


def membership_form():

    obj = Membership()

    window = tk.Toplevel()
    window.title("Membership Management")
    window.geometry("500x650")

    tk.Label(
        window,
        text="Membership Management",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # Membership Name
    tk.Label(window, text="Membership Name").pack()
    name_entry = tk.Entry(window, width=35)
    name_entry.pack(pady=2)

    # Duration
    tk.Label(window, text="Duration (Months)").pack()
    duration_entry = tk.Entry(window, width=35)
    duration_entry.pack(pady=2)

    # Price
    tk.Label(window, text="Price").pack()
    price_entry = tk.Entry(window, width=35)
    price_entry.pack(pady=2)

    # Description
    tk.Label(window, text="Description").pack()
    description_entry = tk.Entry(window, width=35)
    description_entry.pack(pady=2)

    # Membership ID
    tk.Label(window, text="Membership ID (For Update/Delete)").pack()
    id_entry = tk.Entry(window, width=35)
    id_entry.pack(pady=2)

    # ---------------- Clear ---------------- #

    def clear_fields():
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        duration_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)

    # ---------------- Insert ---------------- #

    def insert():

        if (
            name_entry.get() == "" or
            duration_entry.get() == "" or
            price_entry.get() == "" or
            description_entry.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required")
            return

        obj.insert_membership(
            name_entry.get(),
            duration_entry.get(),
            price_entry.get(),
            description_entry.get()
        )

        messagebox.showinfo("Success", "Membership Inserted Successfully")
        clear_fields()

    # ---------------- View ---------------- #

    def view():

        rows = obj.view_membership()

        output.delete("1.0", tk.END)

        if len(rows) == 0:
            output.insert(tk.END, "No Membership Found")
            return

        for row in rows:

            output.insert(
                tk.END,
                f"Membership ID : {row.MembershipID}\n"
                f"Membership Name : {row.MembershipName}\n"
                f"Duration : {row.DurationMonths} Months\n"
                f"Price : {row.Price}\n"
                f"Description : {row.Description}\n"
                "----------------------------------------\n"
            )

    # ---------------- Update ---------------- #

    def update():

        if id_entry.get() == "":
            messagebox.showerror("Error", "Enter Membership ID")
            return

        obj.update_membership(
            id_entry.get(),
            name_entry.get(),
            duration_entry.get(),
            price_entry.get(),
            description_entry.get()
        )

        messagebox.showinfo("Success", "Membership Updated Successfully")
        clear_fields()

    # ---------------- Delete ---------------- #

    def delete():

        if id_entry.get() == "":
            messagebox.showerror("Error", "Enter Membership ID")
            return

        obj.delete_membership(id_entry.get())

        messagebox.showinfo("Success", "Membership Deleted Successfully")
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