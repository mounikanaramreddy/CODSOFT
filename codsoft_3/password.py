import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("❌ Invalid Input", "Length must be a positive number.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_output.config(state='normal')
        password_output.delete(0, tk.END)
        password_output.insert(0, password)
        password_output.config(state='readonly')
    except ValueError:
        messagebox.showerror("❌ Invalid Input", "Please enter a valid number.")

# === GUI SETUP ===
root = tk.Tk()
root.title("🎨 Colorful Password Generator")
root.geometry("400x300")
root.configure(bg="#E6F2FF")  # Light blue background
root.resizable(False, False)

# === STYLED WIDGETS ===

# Title
title = tk.Label(root, text="🔐 Password Generator", 
                 font=("Arial", 18, "bold"), 
                 fg="#004080", bg="#E6F2FF")
title.pack(pady=10)

# Length Label
length_label = tk.Label(root, text="Enter password length:", 
                        font=("Arial", 12),
                        bg="#E6F2FF", fg="#333")
length_label.pack()

# Entry Box
length_entry = tk.Entry(root, font=("Arial", 12), justify='center')
length_entry.pack(pady=5)

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", 
                         font=("Arial", 12, "bold"),
                         bg="#0080FF", fg="white", 
                         activebackground="#0059b3",
                         relief=tk.RAISED, bd=3,
                         command=generate_password)
generate_btn.pack(pady=10)

# Output Label
output_label = tk.Label(root, text="Generated Password:", 
                        font=("Arial", 12), bg="#E6F2FF", fg="#333")
output_label.pack(pady=(15, 0))

# Output Field
password_output = tk.Entry(root, font=("Courier", 14), 
                           justify='center', width=28,
                           fg="#004d00", bg="#ccffcc",  # green text box
                           state='readonly', relief=tk.SUNKEN, bd=2)
password_output.pack(pady=5)

# Footer
footer = tk.Label(root, text="Built with ❤️ using Tkinter", 
                  font=("Arial", 10), bg="#E6F2FF", fg="#666")
footer.pack(side=tk.BOTTOM, pady=10)

# Run the app
root.mainloop()
