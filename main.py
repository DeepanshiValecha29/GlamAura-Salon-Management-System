import tkinter as tk
from tkinter import messagebox
from datetime import datetime

import customer_form
import employee_form
import service_form
import product_form
import appointment_form
import bill_form
import productsale_form
import membership_form


def dashboard():

    window = tk.Toplevel()
    window.title("GlamAura Salon Management System")
    window.state("zoomed")
    window.configure(bg="#FFF5F8")

    # ================= Header =================

    tk.Label(
        window,
        text="✂ GlamAura Salon ✂",
        font=("Arial", 26, "bold"),
        bg="#FFF5F8",
        fg="#C2185B"
    ).pack(pady=(15, 5))

    tk.Label(
        window,
        text="Salon Management System",
        font=("Arial", 14, "bold"),
        bg="#FFF5F8",
        fg="#6A1B9A"
    ).pack()

    tk.Label(
        window,
        text="✨ Welcome To GlamAura Salon ✨",
        font=("Arial", 15, "bold"),
        bg="#FFF5F8",
        fg="#E91E63"
    ).pack(pady=(8,2))

    tk.Label(
        window,
        text="Where Beauty Meets Elegance",
        font=("Arial",11,"italic"),
        bg="#FFF5F8",
        fg="#8E24AA"
    ).pack()

    tk.Label(
        window,
        text="Enhancing beauty with professional salon services.",
        font=("Arial",10),
        bg="#FFF5F8",
        fg="gray35"
    ).pack(pady=(2,8))

    # ================= Admin =================

    info_frame = tk.Frame(window,bg="#FFF5F8")
    info_frame.pack()

    tk.Label(
        info_frame,
        text="👋 Welcome Admin",
        font=("Arial",11,"bold"),
        bg="#FFF5F8",
        fg="#00695C"
    ).pack()

    time_label = tk.Label(
        info_frame,
        font=("Arial",10),
        bg="#FFF5F8",
        fg="gray40"
    )
    time_label.pack()

    def update_time():

        current=datetime.now().strftime(
            "%d-%m-%Y   %I:%M:%S %p"
        )

        time_label.config(text=current)

        time_label.after(
            1000,
            update_time
        )

    update_time()

    # ================= Qualities =================

    tk.Label(
        window,
        text="🌸 Why Choose GlamAura? 🌸",
        font=("Arial",13,"bold"),
        bg="#FFF5F8",
        fg="#00695C"
    ).pack(pady=(10,3))

    qualities=(
        "✔ Hair Styling\n"
        "✔ Bridal Makeup\n"
        "✔ Skin Care\n"
        "✔ Hygienic Environment"
    )

    tk.Label(
        window,
        text=qualities,
        font=("Arial",10),
        justify="left",
        bg="#FFF5F8"
    ).pack(pady=(0,10))

    # ================= Buttons =================

    button_style={

        "width":22,
        "height":2,
        "font":("Arial",11,"bold"),
        "bg":"#EC407A",
        "fg":"white",
        "activebackground":"#C2185B",
        "activeforeground":"white",
        "bd":0,
        "cursor":"hand2"

    }

    button_frame=tk.Frame(
        window,
        bg="#FFF5F8"
    )

    button_frame.pack(pady=5)
    tk.Button(
        button_frame,
        text="👤 Customer",
        command=customer_form.customer_form,
        **button_style
    ).grid(row=0, column=0, padx=8, pady=5)

    tk.Button(
        button_frame,
        text="👨‍💼 Employee",
        command=employee_form.employee_form,
        **button_style
    ).grid(row=0, column=1, padx=8, pady=5)

    tk.Button(
        button_frame,
        text="💇 Service",
        command=service_form.service_form,
        **button_style
    ).grid(row=1, column=0, padx=8, pady=5)

    tk.Button(
        button_frame,
        text="🧴 Product",
        command=product_form.product_form,
        **button_style
    ).grid(row=1, column=1, padx=8, pady=5)

    tk.Button(
        button_frame,
        text="📅 Appointment",
        command=appointment_form.appointment_form,
        **button_style
    ).grid(row=2, column=0, padx=8, pady=5)

    tk.Button(
        button_frame,
        text="🧾 Bill",
        command=bill_form.bill_form,
        **button_style
    ).grid(row=2, column=1, padx=8, pady=5)

    tk.Button(
        button_frame,
        text="🛒 Product Sale",
        command=productsale_form.productsale_form,
        **button_style
    ).grid(row=3, column=0, padx=8, pady=5)

    tk.Button(
        button_frame,
        text="💎 Membership",
        command=membership_form.membership_form,
        **button_style
    ).grid(row=3, column=1, padx=8, pady=5)

    # ================= Logout =================

    def logout():

        confirm = messagebox.askyesno(
            "Logout",
            "Do you want to logout?"
        )

        if confirm:
            window.destroy()

            import login
            login.login_window()

    bottom_frame = tk.Frame(
        window,
        bg="#FFF5F8"
    )
    bottom_frame.pack(pady=15)

    tk.Button(
        bottom_frame,
        text="🚪 Logout",
        width=16,
        height=2,
        font=("Arial",11,"bold"),
        bg="#FF9800",
        fg="white",
        bd=0,
        command=logout
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        bottom_frame,
        text="❌ Exit",
        width=16,
        height=2,
        font=("Arial",11,"bold"),
        bg="#E53935",
        fg="white",
        bd=0,
        command=window.destroy
    ).grid(row=0, column=1, padx=10)

    # ================= Footer =================

    tk.Label(
        window,
        text="❤️ Thank You For Visiting GlamAura Salon ❤️",
        font=("Arial",11,"bold"),
        fg="#C2185B",
        bg="#FFF5F8"
    ).pack(pady=(8,2))

    tk.Label(
        window,
        text="Your Beauty, Our Passion",
        font=("Arial",10,"italic"),
        fg="#6A1B9A",
        bg="#FFF5F8"
    ).pack()

    tk.Label(
        window,
        text="Developed using Python Tkinter & SQL Server",
        font=("Arial",9),
        fg="gray40",
        bg="#FFF5F8"
    ).pack(pady=(3,10))


if __name__ == "__main__":
    dashboard()