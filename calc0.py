import tkinter as tk
from tkinter import ttk
import math

class Calculator:

    # This defines a method and takes 2 parameteres (self and color)
    def change_bg_color(self, color):
        self.bg_color = color  # This line assigns the value of the color parameter to the bg_color attribute of the instance. It's storing the current background color within the class instance.
        self.root.configure(bg=color) # This updates the background colour

    def __init__(self, root):
        self.root = root
        root.title("HEM Calculator")
        self.bg_color = '#ffffff'
        root.configure(bg=self.bg_color)

        # Load custom font
        custom_font = tk.font.Font(family="Vidaloka-Regular", size=14)

        # Load and display the resized logo
        logo_image = tk.PhotoImage(file="calc.png")
        width, height = logo_image.width(), logo_image.height()
        new_width, new_height = int(width * 0.5), int(height * 0.5)  # Resize the logo to 50%
        self.logo_image = logo_image.subsample(width // new_width, height // new_height)
        self.logo_label = tk.Label(root, image=self.logo_image, bg=self.bg_color)
        self.logo_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")  # Placed on a new line

        # Entry field for displaying and inputting numbers
        self.entry = tk.Entry(root, font=custom_font)
        self.entry.grid(row=1, column=0, rowspan=2,columnspan=5, padx=10, pady=10, sticky="nsew")  # Add sticky option


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
            operation_button = ttk.Button(root, text=text, relief=tk.RAISED, bd=0, command=command, width=20, style='Rounded.TButton')
            operation_button.grid(row=i // 2 + 3, column=i % 2 + 3, padx=5, pady=5)

        # Number buttons
        # Uses a lambda function to capture the current value of number and passes it to the self.insert_number method.
        buttons = []
        for number in range(10):
            button = ttk.Button(root, text=str(number), relief=tk.RAISED, bd=0, command=lambda num=number: self.insert_number(num), width=20, style='Rounded.TButton')
            buttons.append(button)

        # Place number buttons (0 to 9)
        # Generates a list of positions for the number buttons
        positions = [(i // 3 + 3, i % 3) for i in range(13)]
        positions[9] = (6, 1)  # Change the position of button "9" to row 5, column 1
        # Modify the position of the "Power Of" button
        for pos, button in zip(positions, buttons[:13]):
            button.grid(row=pos[0], column=pos[1], padx=5, pady=5)

        # Add Clear button
        clear_button = ttk.Button(root, text="Clear", relief=tk.RAISED, bd=0, command=self.clear, width=20, style='Rounded.TButton')
        clear_button.grid(row=7, column=1, columnspan=1, padx=5, pady=5)  # Set row and column for clear button

        # Decimal point button
        decimal_button = ttk.Button(root, text=".", relief=tk.RAISED, bd=0, command=lambda: self.insert_decimal(), width=20, style='Rounded.TButton')
        decimal_button.grid(row=7, column=2)

        # Equals button
        equals_button = ttk.Button(root, text="=", relief=tk.RAISED, bd=0, command=self.evaluate_expression, width=20, style='Rounded.TButton')
        equals_button.grid(row=7, column=3, padx=5, pady=5)

        # Conversion buttons
        convert_to_binary_btn = ttk.Button(root, text="To Binary", relief=tk.RAISED, bd=0, command=self.decimal_to_binary, width=20, style='Rounded.TButton')
        convert_to_binary_btn.grid(row=6, column=0, padx=5, pady=5)

        convert_to_decimal_btn = ttk.Button(root, text="To Decimal", relief=tk.RAISED, bd=0, command=self.binary_to_decimal, width=20, style='Rounded.TButton')
        convert_to_decimal_btn.grid(row=6, column=2, padx=5, pady=5)

        # Adding a button that allows the user to change the background color
        color_btn1 = ttk.Button(root, text="", relief=tk.RAISED, bd=0, command=lambda: self.change_bg_color('lightblue'), width=20, style='Rounded.TButton')
        color_btn1.grid(row=9, column=0, padx=(0, 20))  # Add spacing after the button

        color_btn2 = ttk.Button(root, text="", relief=tk.RAISED, bd=0, command=lambda: self.change_bg_color('lightgreen'), width=20, style='Rounded.TButton')
        color_btn2.grid(row=9, column=1, padx=(20, 20))  # Add spacing before and after the button

        color_btn3 = ttk.Button(root, text="", relief=tk.RAISED, bd=0, command=lambda: self.change_bg_color('lightcoral'), width=20, style='Rounded.TButton')
        color_btn3.grid(row=9, column=2, padx=(20, 20))  # Add spacing before and after the button

        color_btn4 = ttk.Button(root, text="", relief=tk.RAISED, bd=0, command=lambda: self.change_bg_color('black'), width=20, style='Rounded.TButton')
        color_btn4.grid(row=9, column=3, padx=(20, 20))  # Add spacing before and after the button

        color_btn5 = ttk.Button(root, text="", relief=tk.RAISED, bd=0, command=lambda: self.change_bg_color('violet'), width=20, style='Rounded.TButton')
        color_btn5.grid(row=9, column=4, padx=(20, 20))  # Add spacing before the button

    # Retrieves current content in the data field and stores it in the varriable 'current'
    # Checks wether the current content of the data field contains a valid numeric value
