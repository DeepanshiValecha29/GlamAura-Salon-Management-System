import tkinter as tk


def show_splash():

    splash = tk.Toplevel()

    splash.title("GlamAura")
    splash.geometry("500x300")
    splash.state("zoomed")
    splash.configure(bg="#26A69A")
    splash.resizable(False, False)


    # ================= Title =================

    tk.Label(
        splash,
        text="✂ GlamAura",
        font=("Arial", 40, "bold"),
        bg="#26A69A",
        fg="white"
    ).pack(pady=(180, 20))


    tk.Label(
        splash,
        text="Salon Management System",
        font=("Arial", 18, "bold"),
        bg="#26A69A",
        fg="white"
    ).pack()


    tk.Label(
        splash,
        text="Loading...",
        font=("Arial", 14),
        bg="#26A69A",
        fg="white"
    ).pack(pady=40)



    # ================= Open Dashboard =================

    def open_dashboard():

        splash.destroy()

        import main
        main.dashboard()



    splash.after(
        2000,
        open_dashboard
    )