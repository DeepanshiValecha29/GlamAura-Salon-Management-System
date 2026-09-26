import tkinter as tk
from tkinter import messagebox
from employee import Employee


def employee_form():

    obj = Employee()

    window = tk.Toplevel()
    window.title("Employee Management")
    window.geometry("450x600")

    tk.Label(
        window,
        text="Employee Management",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # Employee Name
    tk.Label(window, text="Employee Name").pack()
    name_entry = tk.Entry(window, width=35)
    name_entry.pack(pady=2)

    # Role
    tk.Label(window, text="Role").pack()
    role_entry = tk.Entry(window, width=35)
    role_entry.pack(pady=2)

    # Phone
    tk.Label(window, text="Phone").pack()
    phone_entry = tk.Entry(window, width=35)
    phone_entry.pack(pady=2)

    # Salary
    tk.Label(window, text="Salary").pack()
    salary_entry = tk.Entry(window, width=35)
    salary_entry.pack(pady=2)

    # Employee ID
    tk.Label(window, text="Employee ID (For Update/Delete)").pack()
    id_entry = tk.Entry(window, width=35)
    id_entry.pack(pady=2)

    # ---------------- Clear ---------------- #

    def clear_fields():
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        role_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        salary_entry.delete(0, tk.END)

    # ---------------- Insert ---------------- #

    def insert():

        if (
            name_entry.get() == "" or
            role_entry.get() == "" or
            phone_entry.get() == "" or
            salary_entry.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required")
            return

        obj.insert_employee(
            name_entry.get(),
            role_entry.get(),
            phone_entry.get(),
            salary_entry.get()
        )

        messagebox.showinfo("Success", "Employee Inserted Successfully")
        clear_fields()

    # ---------------- View ---------------- #

    def view():

        rows = obj.view_employee()

        output.delete("1.0", tk.END)

        if len(rows) == 0:
            output.insert(tk.END, "No Employee Found")
            return

        for row in rows:

            output.insert(
                tk.END,
                f"Employee ID : {row.EmployeeID}\n"
                f"Employee Name : {row.EmployeeName}\n"
                f"Role : {row.Role}\n"
                f"Phone : {row.Phone}\n"
                f"Salary : {row.Salary}\n"
                "----------------------------------------\n"
            )

    # ---------------- Update ---------------- #

    def update():

        if id_entry.get() == "":
            messagebox.showerror("Error", "Enter Employee ID")
            return

        obj.update_employee(
            id_entry.get(),
            name_entry.get(),
            role_entry.get(),
            phone_entry.get(),
            salary_entry.get()
        )

        messagebox.showinfo("Success", "Employee Updated Successfully")
        clear_fields()

    # ---------------- Delete ---------------- #

    def delete():

        if id_entry.get() == "":
            messagebox.showerror("Error", "Enter Employee ID")
            return

        obj.delete_employee(id_entry.get())

        messagebox.showinfo("Success", "Employee Deleted Successfully")
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

    # ---------------- Output Box ---------------- #

    output = tk.Text(window, width=55, height=12)
    output.pack(pady=10)