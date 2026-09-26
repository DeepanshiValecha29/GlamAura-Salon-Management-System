import tkinter as tk
from tkinter import messagebox
from bill import Bill


def bill_form():

    obj = Bill()

    window = tk.Toplevel()
    window.title("Bill Management")
    window.geometry("500x650")

    tk.Label(
        window,
        text="Bill Management",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # Appointment ID
    tk.Label(window, text="Appointment ID").pack()
    appointment_entry = tk.Entry(window, width=35)
    appointment_entry.pack(pady=2)

    # Bill Date
    tk.Label(window, text="Bill Date (YYYY-MM-DD)").pack()
    billdate_entry = tk.Entry(window, width=35)
    billdate_entry.pack(pady=2)

    # Total Amount
    tk.Label(window, text="Total Amount").pack()
    amount_entry = tk.Entry(window, width=35)
    amount_entry.pack(pady=2)

    # Payment Mode
    tk.Label(window, text="Payment Mode").pack()
    payment_entry = tk.Entry(window, width=35)
    payment_entry.pack(pady=2)

    # Bill ID
    tk.Label(window, text="Bill ID (For Update/Delete)").pack()
    id_entry = tk.Entry(window, width=35)
    id_entry.pack(pady=2)

    # ---------------- Clear ---------------- #

    def clear_fields():
        id_entry.delete(0, tk.END)
        appointment_entry.delete(0, tk.END)
        billdate_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        payment_entry.delete(0, tk.END)

    # ---------------- Insert ---------------- #

    def insert():

        if (
            appointment_entry.get() == "" or
            billdate_entry.get() == "" or
            amount_entry.get() == "" or
            payment_entry.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required")
            return

        obj.insert_bill(
            appointment_entry.get(),
            billdate_entry.get(),
            amount_entry.get(),
            payment_entry.get()
        )

        messagebox.showinfo("Success", "Bill Inserted Successfully")
        clear_fields()

    # ---------------- View ---------------- #

    def view():

        rows = obj.view_bill()

        output.delete("1.0", tk.END)

        if len(rows) == 0:
            output.insert(tk.END, "No Bill Found")
            return

        for row in rows:

            output.insert(
                tk.END,
                f"Bill ID : {row.BillID}\n"
                f"Appointment ID : {row.AppointmentID}\n"
                f"Bill Date : {row.BillDate}\n"
                f"Total Amount : {row.TotalAmount}\n"
                f"Payment Mode : {row.PaymentMode}\n"
                "----------------------------------------\n"
            )

    # ---------------- Update ---------------- #

    def update():

        if id_entry.get() == "":
            messagebox.showerror("Error", "Enter Bill ID")
            return

        obj.update_bill(
            id_entry.get(),
            appointment_entry.get(),
            billdate_entry.get(),
            amount_entry.get(),
            payment_entry.get()
        )

        messagebox.showinfo("Success", "Bill Updated Successfully")
        clear_fields()

    # ---------------- Delete ---------------- #

    def delete():

        if id_entry.get() == "":
            messagebox.showerror("Error", "Enter Bill ID")
            return

        obj.delete_bill(id_entry.get())

        messagebox.showinfo("Success", "Bill Deleted Successfully")
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