import threading
import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Python Calculator")

        # Entry field for displaying and inputting numbers
        self.entry = tk.Entry(root, font=('Arial', 34))
        self.entry.grid(row=0, column=0, columnspan=4, padx=15, pady=15)

        # Button labels
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create buttons
        for i, button in enumerate(buttons):
            row = i // 4 + 1
            col = i % 4
            if button == '=':
                tk.Button(root, text=button, command=self.calculate).grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
            else:
                tk.Button(root, text=button, command=lambda b=button: self.entry.insert(tk.END, b)).grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

def run_calculator():
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    run_calculator()
