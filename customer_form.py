import tkinter as tk
from tkinter import messagebox
from customer import Customer


def customer_form():

    window = tk.Toplevel()
    window.title("Customer Management")
    window.geometry("450x520")
    window.configure(bg="#EAF6F6")
    window.resizable(False, False)


    tk.Label(
        window,
        text="👤 Customer Management",
        font=("Arial",18,"bold"),
        bg="#EAF6F6",
        fg="#00695C"
    ).pack(pady=15)


    tk.Label(
        window,
        text="Customer Name",
        bg="#EAF6F6",
        font=("Arial",11,"bold")
    ).pack()

    name_entry = tk.Entry(window,width=30)
    name_entry.pack(pady=5)



    tk.Label(
        window,
        text="Gender",
        bg="#EAF6F6",
        font=("Arial",11,"bold")
    ).pack()

    gender_entry = tk.Entry(window,width=30)
    gender_entry.pack(pady=5)



    tk.Label(
        window,
        text="Phone",
        bg="#EAF6F6",
        font=("Arial",11,"bold")
    ).pack()

    phone_entry = tk.Entry(window,width=30)
    phone_entry.pack(pady=5)



    tk.Label(
        window,
        text="Email",
        bg="#EAF6F6",
        font=("Arial",11,"bold")
    ).pack()

    email_entry = tk.Entry(window,width=30)
    email_entry.pack(pady=5)



    tk.Label(
        window,
        text="Customer ID (Update/Delete)",
        bg="#EAF6F6",
        font=("Arial",11,"bold")
    ).pack()

    id_entry = tk.Entry(window,width=30)
    id_entry.pack(pady=5)



    obj = Customer()



    def insert():

        if name_entry.get()=="" or phone_entry.get()=="":
            messagebox.showwarning(
                "Warning",
                "Name and Phone are required"
            )
            return

        obj.insert_customer(
            name_entry.get(),
            gender_entry.get(),
            phone_entry.get(),
            email_entry.get()
        )

        messagebox.showinfo(
            "Success",
            "Customer Inserted"
        )

        clear()



    def view():

        obj.view_customer()



    def update():

        obj.update_customer(
            id_entry.get(),
            name_entry.get(),
            gender_entry.get(),
            phone_entry.get(),
            email_entry.get()
        )

        messagebox.showinfo(
            "Success",
            "Customer Updated"
        )

        clear()



    def delete():

        obj.delete_customer(
            id_entry.get()
        )

        messagebox.showinfo(
            "Success",
            "Customer Deleted"
        )

        clear()



    def clear():

        name_entry.delete(0,tk.END)
        gender_entry.delete(0,tk.END)
        phone_entry.delete(0,tk.END)
        email_entry.delete(0,tk.END)
        id_entry.delete(0,tk.END)



    button_style = {
        "width":15,
        "font":("Arial",10,"bold"),
        "fg":"white",
        "bd":0
    }



    tk.Button(
        window,
        text="Insert",
        bg="#26A69A",
        command=insert,
        **button_style
    ).pack(pady=5)


    tk.Button(
        window,
        text="View",
        bg="#42A5F5",
        command=view,
        **button_style
    ).pack(pady=5)


    tk.Button(
        window,
        text="Update",
        bg="#FF9800",
        command=update,
        **button_style
    ).pack(pady=5)


    tk.Button(
        window,
        text="Delete",
        bg="#E53935",
        command=delete,
        **button_style
    ).pack(pady=5)


    tk.Button(
        window,
        text="Clear",
        bg="#757575",
        command=clear,
        **button_style
    ).pack(pady=5)


    window.mainloop()