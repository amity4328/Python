import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    user_input = entry.get().lower().strip()

    if user_input == "":
        messagebox.showinfo("Input Error", "Please enter an expression.")
        return

    try:
        # Replace natural language with operators
        expression = user_input.replace("plus", "+")
        expression = expression.replace("minus", "-")
        expression = expression.replace("multiply", "*")
        expression = expression.replace("times", "*")
        expression = expression.replace("divide", "/")
        expression = expression.replace("power", "**")
        expression = expression.replace("^", "**")

        if expression.startswith("sqrt"):
            number = float(expression.split("sqrt")[-1].strip())
            result = math.sqrt(number)
        else:
            result = eval(expression)

        result_label.config(text=f"= {result}")
    except Exception as e:
        result_label.config(text="Invalid input!")

# GUI setup
root = tk.Tk()
root.title("Smart Calculator")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Smart Calculator", font=("Arial", 16)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)

tk.Button(root, text="Calculate", command=calculate, font=("Arial", 12)).pack(pady=5)

result_label = tk.Label(root, text="= ", font=("Arial", 14))
result_label.pack(pady=20)

tk.Label(root, text="Try: 5 plus 6, sqrt 16, 3 power 2", font=("Arial", 10), fg="gray").pack()

root.mainloop()