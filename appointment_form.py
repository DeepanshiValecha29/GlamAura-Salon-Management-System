import tkinter as tk
from tkinter import messagebox
from appointment import Appointment


def appointment_form():

    obj = Appointment()

    window = tk.Toplevel()
    window.title("Appointment Management")
    window.geometry("500x700")

    tk.Label(
        window,
        text="Appointment Management",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # Customer ID
    tk.Label(window, text="Customer ID").pack()
    customer_entry = tk.Entry(window, width=35)
    customer_entry.pack(pady=2)

    # Employee ID
    tk.Label(window, text="Employee ID").pack()
    employee_entry = tk.Entry(window, width=35)
    employee_entry.pack(pady=2)

    # Service ID
    tk.Label(window, text="Service ID").pack()
    service_entry = tk.Entry(window, width=35)
    service_entry.pack(pady=2)

    # Appointment Date
    tk.Label(window, text="Appointment Date (YYYY-MM-DD)").pack()
    date_entry = tk.Entry(window, width=35)
    date_entry.pack(pady=2)

    # Appointment Time
    tk.Label(window, text="Appointment Time (HH:MM:SS)").pack()
    time_entry = tk.Entry(window, width=35)
    time_entry.pack(pady=2)

    # Status
    tk.Label(window, text="Status").pack()
    status_entry = tk.Entry(window, width=35)
    status_entry.pack(pady=2)

    # Appointment ID
    tk.Label(window, text="Appointment ID (For Update/Delete)").pack()
    id_entry = tk.Entry(window, width=35)
    id_entry.pack(pady=2)

    # ---------------- Clear ---------------- #

    def clear_fields():
        id_entry.delete(0, tk.END)
        customer_entry.delete(0, tk.END)
        employee_entry.delete(0, tk.END)
        service_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
        status_entry.delete(0, tk.END)

    # ---------------- Insert ---------------- #

    def insert():

        if (
            customer_entry.get() == "" or
            employee_entry.get() == "" or
            service_entry.get() == "" or
            date_entry.get() == "" or
            time_entry.get() == "" or
            status_entry.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required")
            return

        obj.insert_appointment(
            customer_entry.get(),
            employee_entry.get(),
            service_entry.get(),
            date_entry.get(),
            time_entry.get(),
            status_entry.get()
        )

        messagebox.showinfo("Success", "Appointment Inserted Successfully")
        clear_fields()

    # ---------------- View ---------------- #

    def view():

        rows = obj.view_appointment()

        output.delete("1.0", tk.END)

        if len(rows) == 0:
            output.insert(tk.END, "No Appointment Found")
            return

        for row in rows:

            output.insert(
                tk.END,
                f"Appointment ID : {row.AppointmentID}\n"
                f"Customer ID : {row.CustomerID}\n"
                f"Employee ID : {row.EmployeeID}\n"
                f"Service ID : {row.ServiceID}\n"
                f"Date : {row.AppointmentDate}\n"
                f"Time : {row.AppointmentTime}\n"
                f"Status : {row.Status}\n"
                "----------------------------------------\n"
            )

    # ---------------- Update ---------------- #

    def update():

        if id_entry.get() == "":
            messagebox.showerror("Error", "Enter Appointment ID")
            return

        obj.update_appointment(
            id_entry.get(),
            customer_entry.get(),
            employee_entry.get(),
            service_entry.get(),
            date_entry.get(),
            time_entry.get(),
            status_entry.get()
        )

        messagebox.showinfo("Success", "Appointment Updated Successfully")
        clear_fields()

    # ---------------- Delete ---------------- #

    def delete():

        if id_entry.get() == "":
            messagebox.showerror("Error", "Enter Appointment ID")
            return

        obj.delete_appointment(id_entry.get())

        messagebox.showinfo("Success", "Appointment Deleted Successfully")
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