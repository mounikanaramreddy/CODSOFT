import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            messagebox.showwarning("Warning", "Choose a valid operation.")
            return

        label_result.config(text=f"Result: {result:.2f}", fg="green")
    except ZeroDivisionError:
        label_result.config(text="Error: Division by Zero", fg="red")
    except ValueError:
        label_result.config(text="Error: Enter valid numbers", fg="red")

# GUI Setup
root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("400x300")
root.configure(bg="#e8f8f5")

# Title
tk.Label(root, text="Simple Calculator", font=("Arial", 16, "bold"), bg="#e8f8f5", fg="#117a65").pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#d1f2eb", padx=10, pady=10)
frame.pack(pady=10)

# Number 1
tk.Label(frame, text="Enter Number 1:", bg="#d1f2eb").grid(row=0, column=0, sticky="w")
entry_num1 = tk.Entry(frame, width=20)
entry_num1.grid(row=0, column=1)

# Number 2
tk.Label(frame, text="Enter Number 2:", bg="#d1f2eb").grid(row=1, column=0, sticky="w")
entry_num2 = tk.Entry(frame, width=20)
entry_num2.grid(row=1, column=1)

# Operation
tk.Label(frame, text="Choose Operation:", bg="#d1f2eb").grid(row=2, column=0, sticky="w")
operation_var = tk.StringVar()
operation_menu = tk.OptionMenu(frame, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1)
operation_menu.config(width=10)

# Calculate Button
tk.Button(root, text="Calculate", command=calculate, bg="#58d68d", fg="white", width=15).pack(pady=10)

# Result Label
label_result = tk.Label(root, text="", font=("Arial", 14), bg="#e8f8f5")
label_result.pack(pady=10)

# Run the app
root.mainloop()
