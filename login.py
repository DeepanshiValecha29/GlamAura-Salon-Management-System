import tkinter as tk
from tkinter import messagebox
from connection import DBConnection


class Login:

    def check_login(self, username, password):
        db = DBConnection()
        db.connect()

        try:
            db.cursor.execute(
                "EXEC prcLogin ?, ?",
                username,
                password
            )

            result = db.cursor.fetchone()

            if result:
                return True
            else:
                return False

        except Exception as e:
            print("Login Error:", e)
            return False

        finally:
            db.disconnect()


def login_window():

    def login():

        username = user_entry.get()
        password = pass_entry.get()

        if username == "" or password == "":
            messagebox.showwarning(
                "Warning",
                "Please enter Username and Password"
            )
            return

        obj = Login()

        if obj.check_login(username, password):

            messagebox.showinfo(
                "Success",
                "Welcome to GlamAura!"
            )

            window.withdraw()

            import splash
            splash.show_splash()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password"
            )


    def show_hide():

        if pass_entry.cget("show") == "*":
            pass_entry.config(show="")
            show_btn.config(text="Hide")

        else:
            pass_entry.config(show="*")
            show_btn.config(text="Show")


    window = tk.Tk()

    window.title("GlamAura Login")
    window.geometry("500x450")
    window.state("zoomed")
    window.configure(bg="#EAF6F6")
    window.resizable(False, False)
    


    tk.Label(
        window,
        text="✂ GlamAura",
        font=("Arial", 26, "bold"),
        bg="#EAF6F6",
        fg="#00695C"
    ).pack(pady=(20,5))


    tk.Label(
        window,
        text="Salon Management System",
        font=("Arial", 13),
        bg="#EAF6F6",
        fg="gray30"
    ).pack(pady=(0,20))


    tk.Label(
        window,
        text="Username",
        font=("Arial",11,"bold"),
        bg="#EAF6F6"
    ).pack()


    user_entry = tk.Entry(
        window,
        font=("Arial",12),
        width=30
    )
    user_entry.pack(ipady=5,pady=5)


    tk.Label(
        window,
        text="Password",
        font=("Arial",11,"bold"),
        bg="#EAF6F6"
    ).pack()


    pass_entry = tk.Entry(
        window,
        show="*",
        font=("Arial",12),
        width=30
    )
    pass_entry.pack(ipady=5,pady=5)


    show_btn = tk.Button(
        window,
        text="Show",
        width=8,
        bg="#64B5F6",
        fg="white",
        command=show_hide
    )
    show_btn.pack(pady=5)


    tk.Button(
        window,
        text="LOGIN",
        font=("Arial",12,"bold"),
        width=20,
        bg="#26A69A",
        fg="white",
        command=login
    ).pack(pady=15)


    tk.Button(
        window,
        text="EXIT",
        font=("Arial",11,"bold"),
        width=20,
        bg="#E53935",
        fg="white",
        command=window.destroy
    ).pack()


    tk.Label(
        window,
        text="© 2026 GlamAura Salon Management System",
        bg="#EAF6F6",
        fg="gray40",
        font=("Arial",9)
    ).pack(side="bottom", pady=10)


    window.bind(
        "<Return>",
        lambda event: login()
    )


    window.mainloop()



if __name__ == "__main__":
    login_window()