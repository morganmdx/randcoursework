import tkinter as tk
from tkinter import font
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("HEM Calculator")
        self.bg_color = 'lightblue'
        root.configure(bg=self.bg_color)

        # Load custom font
        custom_font = font.Font(family="Vidaloka-Regular", size=14)

        # Entry field for displaying and inputting numbers
        self.entry = tk.Entry(root, font=custom_font)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")  # Add sticky option

        # Load and display the resized logo
        self.logo_image = tk.PhotoImage(file="logo.png").subsample(2)  # Resizing by a factor of 2
        self.logo_label = tk.Label(root, image=self.logo_image, bg=self.bg_color)
        self.logo_label.grid(row=0, column=5, rowspan=2, padx=10, pady=10, sticky="nsew")

        # Basic operation buttons
        operations = [
            ('Square Root', self.square_root),
            ('Power Of', self.power_of),
            ('%', self.percentage),
            ('*', self.multiplication),
            ('+', self.addition),
            ('-', self.subtraction),
            ('/', self.division)
         ]

        #creating operation buttons
        #for loop which iterates over each item in the operations list
        for i, (text, command) in enumerate(operations):
            operation_button = tk.Button(root, text=text, padx=40, pady=20, bg='light yellow', bd=0, command=command)
            operation_button.grid(row=i // 2 + 2, column=i % 2 + 3)

        # Number buttons
        # Uses a lambda function to capture the current value of number and passes it to the self.insert_number method.
        buttons = []
        for number in range(10):
            button = tk.Button(root, text=str(number), padx=40, pady=20, bg='light yellow', bd=0, command=lambda num=number: self.insert_number(num))
            buttons.append(button)

        # Place number buttons (0 to 9)
        # Generates a list of positions for the number buttons
        positions = [(i // 3 + 2, i % 3) for i in range(13)]
        positions[9] = (5, 1)  # Change the position of button "9" to row 5, column 1
        for pos, button in zip(positions, buttons[:13]):
            button.grid(row=pos[0], column=pos[1])

        # Add Clear button
        clear_button = tk.Button(root, text="Clear", padx=40, pady=20, command=self.clear)
        clear_button.grid(row=6, column=1, columnspan=1)  # Set row and column for clear button

        # Decimal point button
        decimal_button = tk.Button(root, text=".", padx=40, pady=20, bg='light yellow', bd=0, command=lambda: self.insert_decimal())
        decimal_button.grid(row=6, column=2)

        # Equals button
        equals_button = tk.Button(root, text="=", padx=40, pady=20, bg='light yellow', bd=0, command=self.evaluate_expression)
        equals_button.grid(row=6, column=3)

        # Conversion buttons
        convert_to_binary_btn = tk.Button(root, text="To Binary", padx=29, pady=20, command=self.decimal_to_binary)
        convert_to_binary_btn.grid(row=5, column=0)

        convert_to_decimal_btn = tk.Button(root, text="To Decimal", padx=29, pady=20, command=self.binary_to_decimal)
        convert_to_decimal_btn.grid(row=5, column=2)

        # Adding a button that allows the user to change the background color
        color_btn1 = tk.Button(root, text="", padx=10, pady=5, bg='lightblue', command=lambda: self.change_bg_color('lightblue'))
        color_btn1.grid(row=7, column=0, padx=(0, 20))  # Add spacing after the button

        color_btn2 = tk.Button(root, text="", padx=10, pady=5, bg='lightgreen', command=lambda: self.change_bg_color('lightgreen'))
        color_btn2.grid(row=7, column=1, padx=(20, 20))  # Add spacing before and after the button

        color_btn3 = tk.Button(root, text="", padx=10, pady=5, bg='lightcoral', command=lambda: self.change_bg_color('lightcoral'))
        color_btn3.grid(row=7, column=2, padx=(20, 20))  # Add spacing before and after the button

        color_btn4 = tk.Button(root, text="", padx=10, pady=5, bg='black', command=lambda: self.change_bg_color('black'))
        color_btn4.grid(row=7, column=3, padx=(20, 20))  # Add spacing before and after the button

        color_btn5 = tk.Button(root, text="", padx=10, pady=5, bg='violet', command=lambda: self.change_bg_color('violet'))
        color_btn5.grid(row=7, column=4, padx=(20, 20))  # Add spacing before the button

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

    # Function to convert a decimal
