import tkinter as tk
from tkinter import messagebox

def validate_login():
    email = entry_email.get()
    password = entry_password.get()

    # Validasi login sederhana
    if email == "sifa" and password == "admin123":
        root.destroy()  # Menutup window login
        open_homepage()  # Membuka halaman home
    else:
        messagebox.showerror("Login Gagal", "ID atau Password salah!")

def open_homepage():
    homepage = tk.Tk()
    homepage.title("Homepage")
    homepage.geometry("800x600")
    homepage.configure(bg="#fdfdfd")

    # Header
    header = tk.Frame(homepage, bg="#fff", height=60)
    header.pack(fill="x")

    logo = tk.Label(header, text="LOGO", bg="#fff", fg="#d6336c", font=("Roboto", 16, "bold"))
    logo.pack(side="left", padx=20, pady=10)

    nav = tk.Frame(header, bg="#fff")
    nav.pack(side="right", padx=20)

    for item in ["Home", "Blog", "About"]:
        btn = tk.Button(nav, text=item, bg="#fff", fg="#d6336c", font=("Roboto", 12),
                        bd=0, highlightthickness=0, activeforeground="#ff4081")
        btn.pack(side="left", padx=10)

    # Main Content
    content = tk.Frame(homepage, bg="#fdfdfd")
    content.pack(expand=True, fill="both", padx=20, pady=20)

    title = tk.Label(content, text="Homepage", font=("Roboto", 24, "bold"), bg="#fdfdfd", fg="#333")
    title.pack(pady=20)

    description = tk.Label(content, text="Ini adalah contoh halaman jika berhasil login.\n\n"
                                         "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                                         "Aenean commodo ligula eget dolor. Aenean massa.",
                           font=("Roboto", 12), bg="#f5f0e6", fg="#555", justify="center", wraplength=600)
    description.pack(pady=40, fill="x", padx=20)

    homepage.mainloop()

# Window Login
root = tk.Tk()
root.title("Login Page")
root.geometry("400x400")
root.configure(bg="#f5f0e6")

container = tk.Frame(root, bg="white", bd=0, relief="solid")
container.place(relx=0.5, rely=0.5, anchor="center", width=300, height=350)

# Judul
label_title = tk.Label(container, text="LOGIN", font=("Roboto", 18, "bold"), fg="#333", bg="white")
label_title.pack(pady=20)

# Input Email
entry_email = tk.Entry(container, font=("Roboto", 12), fg="#333", bd=0, highlightthickness=0)
entry_email.insert(0, "Email")
entry_email.bind("<FocusIn>", lambda e: entry_email.delete(0, "end"))
entry_email.pack(pady=10)
tk.Frame(container, height=1, bg="#a8e063").pack(fill="x", padx=10)

# Input Password
entry_password = tk.Entry(container, font=("Roboto", 12), fg="#333", bd=0, highlightthickness=0, show="*")
entry_password.insert(0, "Password")
entry_password.bind("<FocusIn>", lambda e: entry_password.delete(0, "end"))
entry_password.pack(pady=10)
tk.Frame(container, height=1, bg="#a8e063").pack(fill="x", padx=10)

# Tombol Lupa Password
btn_forgot = tk.Label(container, text="Forgot password?", font=("Roboto", 10), fg="#a8e063", bg="white", cursor="hand2")
btn_forgot.pack(pady=5)

# Tombol Login
btn_login = tk.Button(container, text="LOGIN", font=("Roboto", 12), fg="white", bg="#a8e063",
                      activebackground="#56ab2f", activeforeground="white", bd=0, relief="solid", cursor="hand2",
                      command=validate_login)
btn_login.pack(pady=20, ipadx=40, ipady=5)

# Label Belum Punya Akun
label_signup = tk.Label(container, text="Don't have an account yet?", font=("Roboto", 10), fg="#a8e063", bg="white")
label_signup.pack()

root.mainloop()
