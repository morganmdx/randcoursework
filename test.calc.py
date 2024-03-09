import tkinter as tk
from tkinter import font
import math
from threading import Thread

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("HEM Calculator")
        self.bg_color = 'lightblue'
        root.configure(bg=self.bg_color)

        # Load custom font
        custom_font = font.Font(family="Vidaloka-Regular", size=14)

        # Load and display the resized logo
        logo_image = tk.PhotoImage(file="calc.png")  # Ensure "calc.png" exists in your directory
        width, height = logo_image.width(), logo_image.height()
        new_width, new_height = int(width * 0.5), int(height * 0.5)  # Resize the logo to 50%
        self.logo_image = logo_image.subsample(width // new_width, height // new_height)
        self.logo_label = tk.Label(root, image=self.logo_image, bg=self.bg_color)
        self.logo_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

        self.entry = tk.Entry(root, font=custom_font)
        self.entry.grid(row=1, column=0, rowspan=2, columnspan=5, padx=10, pady=10, sticky="nsew")

        operations = [
            ('Square Root', self.square_root),
            ('Power Of', self.power_of),
            ('%', self.percentage),
            ('*', self.multiplication),
            ('+', self.addition),
            ('-', self.subtraction),
            ('/', self.division)
        ]

        for i, (text, command) in enumerate(operations):
            operation_button = tk.Button(root, text=text, padx=40, pady=20, bg='light yellow', bd=0, command=command, width=2)
            operation_button.grid(row=i // 2 + 3, column=i % 2 + 3, padx=5, pady=5)

        buttons = []
        for number in range(10):
            button = tk.Button(root, text=str(number), padx=40, pady=20, bg='light yellow', bd=0, command=lambda num=number: self.insert_number(num), width=2)
            buttons.append(button)

        positions = [(i // 3 + 3, i % 3) for i in range(1, 10)]  # Adjusted for correct layout
        positions.append((6, 0))  # Position for 0
        for pos, button in zip(positions, buttons):
            button.grid(row=pos[0], column=pos[1], padx=5, pady=5)

        clear_button = tk.Button(root, text="Clear", padx=40, pady=20, bg='#E8C1C5', command=self.clear, width=2)
        clear_button.grid(row=7, column=1, columnspan=1, padx=5, pady=5)

        decimal_button = tk.Button(root, text=".", padx=40, pady=20, bg='light yellow', bd=0, command=self.insert_decimal)
        decimal_button.grid(row=7, column=2)

        equals_button = tk.Button(root, text="=", padx=40, pady=20, bg='light yellow', bd=0, command=self.evaluate_expression)
        equals_button.grid(row=7, column=3, padx=5, pady=5)

        # Conversion buttons
        convert_to_binary_btn = tk.Button(root, text="To Binary", padx=40, pady=20, bg='light yellow', command=self.decimal_to_binary, width=2)
        convert_to_binary_btn.grid(row=6, column=0, padx=5, pady=5)

        convert_to_decimal_btn = tk.Button(root, text="To Decimal", padx=40, pady=20, bg='light yellow', command=self.binary_to_decimal, width=2)
        convert_to_decimal_btn.grid(row=6, column=2, padx=5, pady=5)

        # Conversion and color change buttons omitted for brevity

    # Calculator functionality methods omitted for brevity
    # Adding a button that allows the user to change the background color
        color_btn1 = tk.Button(root, text="", padx=10, pady=5, bg='lightblue', command=lambda: self.change_bg_color('lightblue'))
        color_btn1.grid(row=9, column=0, padx=(0, 20))  # Add spacing after the button

        color_btn2 = tk.Button(root, text="", padx=10, pady=5, bg='lightgreen', command=lambda: self.change_bg_color('lightgreen'))
        color_btn2.grid(row=9, column=1, padx=(20, 20))  # Add spacing before and after the button

        color_btn3 = tk.Button(root, text="", padx=10, pady=5, bg='lightcoral', command=lambda: self.change_bg_color('lightcoral'))
        color_btn3.grid(row=9, column=2, padx=(20, 20))  # Add spacing before and after the button

        color_btn4 = tk.Button(root, text="", padx=10, pady=5, bg='black', command=lambda: self.change_bg_color('black'))
        color_btn4.grid(row=9, column=3, padx=(20, 20))  # Add spacing before and after the button

        color_btn5 = tk.Button(root, text="", padx=10, pady=5, bg='violet', command=lambda: self.change_bg_color('violet'))
        color_btn5.grid(row=9, column=4, padx=(20, 20))  # Add spacing before the button


    # This defines a method and takes 2 parameteres (self and color)
    def change_bg_color(self, color):
        self.bg_color = color  # This line assigns the value of the color parameter to the bg_color attribute of the instance. It's storing the current background color within the class instance.
        self.root.configure(bg=color) # This updates the background colour

    # Retrieves current content in the data field and stores it in the varriable 'current'
    # Checks wether the current content of the data field contains a valid numeric value
    # Either current is a positive integer or a negative integer
    def insert_number(self, number):
        current = self.entry.get()
        if current and (current[0] == '-' and current[1:].isdigit() or current.isdigit()):
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(current) + str(number))
        else:
            self.entry.insert(tk.END, str(number))

    # This adds a decimal point function 
    def insert_decimal(self):
        current = self.entry.get()
        if current and '.' not in current:
            self.entry.insert(tk.END, '.')

    # function to convert a binary number to decimal
    def binary_to_decimal(self):
        binary_input = self.entry.get()
        try:
            decimal_output = int(binary_input, 2)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(decimal_output))
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    # Function to convert a decimal number to binary 
    def decimal_to_binary(self):
        decimal_input = self.entry.get()
        try:
            decimal_input = int(decimal_input)
            binary_output = bin(decimal_input)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(binary_output))
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

     # This adds the square foot function 
    def square_root(self):
        try:
            value = float(self.entry.get())
            result = math.sqrt(value)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

     #This adds the power of function 
    # This adds the power of function 
    def power_of(self):
        try:
            self.entry.insert(tk.END, '**')  # Insert '**' into the entry box
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")



    #This adds the percentage function 
    def percentage(self):
        try:
            value = float(self.entry.get())
            result = value / 100
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    #This adds the multiplication function 
    def multiplication(self):
        try:
            value = float(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(value) + '*')
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    #This adds the additin function 
    def addition(self):
        try:
            value = float(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(value) + '+')
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    #This adds the subtraction function 
    def subtraction(self):
        try:
            value = float(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(value) + '-')
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    #This adds the division function 
    def division(self):
        try:
            value = float(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(value) + '/')
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    #retrieves the current content of the entry field associated with the class instance and stores it in the variable expression.
    def evaluate_expression(self):
        expression = self.entry.get()
        try:
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except (ValueError, SyntaxError):
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    #This creates the clear function 
    def clear(self):
        self.entry.delete(0, tk.END)

    def thread_task(self, value):
        # Here you'd call some_lengthy_calculation(value)
        result = self.some_lengthy_calculation(value)  # Placeholder function
        self.root.after(0, lambda: self.update_gui_with_result(result))

    def update_gui_with_result(self, result):
        # Update GUI with result
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(result))

    def some_lengthy_calculation(self, value):
        # Placeholder for a lengthy calculation
        # Replace with your actual calculation
        return value * 2  # Example operation

    def start_threaded_calculation(self, value):
        thread = Thread(target=self.thread_task, args=(value,))
        thread.start()

def run_calculator():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    run_calculator()
