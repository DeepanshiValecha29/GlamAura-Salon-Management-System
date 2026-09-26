import tkinter as tk
from tkinter import messagebox
from service import Service


def service_form():

    obj = Service()

    window = tk.Toplevel()
    window.title("Service Management")
    window.geometry("450x600")

    tk.Label(
        window,
        text="Service Management",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # Service Name
    tk.Label(window, text="Service Name").pack()
    name_entry = tk.Entry(window, width=35)
    name_entry.pack(pady=2)

    # Price
    tk.Label(window, text="Price").pack()
    price_entry = tk.Entry(window, width=35)
    price_entry.pack(pady=2)

    # Duration
    tk.Label(window, text="Duration").pack()
    duration_entry = tk.Entry(window, width=35)
    duration_entry.pack(pady=2)

    # Service ID
    tk.Label(window, text="Service ID (For Update/Delete)").pack()
    id_entry = tk.Entry(window, width=35)
    id_entry.pack(pady=2)

    # ---------------- Clear ---------------- #

    def clear_fields():
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        duration_entry.delete(0, tk.END)

    # ---------------- Insert ---------------- #

    def insert():

        if (
            name_entry.get() == "" or
            price_entry.get() == "" or
            duration_entry.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required")
            return

        obj.insert_service(
            name_entry.get(),
            price_entry.get(),
            duration_entry.get()
        )

        messagebox.showinfo("Success", "Service Inserted Successfully")
        clear_fields()

    # ---------------- View ---------------- #

    def view():

        rows = obj.view_service()

        output.delete("1.0", tk.END)

        if len(rows) == 0:
            output.insert(tk.END, "No Service Found")
            return

        for row in rows:

            output.insert(
                tk.END,
                f"Service ID : {row.ServiceID}\n"
                f"Service Name : {row.ServiceName}\n"
                f"Price : {row.Price}\n"
                f"Duration : {row.Duration}\n"
                "----------------------------------------\n"
            )

    # ---------------- Update ---------------- #

    def update():

        if id_entry.get() == "":
            messagebox.showerror("Error", "Enter Service ID")
            return

        obj.update_service(
            id_entry.get(),
            name_entry.get(),
            price_entry.get(),
            duration_entry.get()
        )

        messagebox.showinfo("Success", "Service Updated Successfully")
        clear_fields()

    # ---------------- Delete ---------------- #

    def delete():

        if id_entry.get() == "":
            messagebox.showerror("Error", "Enter Service ID")
            return

        obj.delete_service(id_entry.get())

        messagebox.showinfo("Success", "Service Deleted Successfully")
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