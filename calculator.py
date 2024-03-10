#import tkinter as tk is a way to import the tkinter module and give it a shorter name in this instance we called it tk.
import tkinter as tk
#the from tkinter import font statement is a way to import only the font. This allows us to access features related to fonts
#and manipulate text styles, sizes, and other font-related properties in our Tkinter.
from tkinter import font
#This stament allows us to use any mathmatical functions in our code to calculate results.
import math
#The Thread statement is a part of the threading module.This provides a convenient way to create and manage threads in our program.
from threading import Thread
#This is used to present decimal numbers as this is important in certain calculations.
from decimal import Decimal

#This code uses Tkinter to define a Calculator class for a basic calculator app. The background colour and title of the main window are set in the constructor (__init__ method).
#The Tkinter window reference is kept in the self.root variable, and light blue is set as the background colour. 
#The class is intended to serve as a template to create calculator components that have an expected appearance and layout.
class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("HEM Calculator")
        self.bg_color = 'lightblue'
        root.configure(bg=self.bg_color)

        # This loads a customized font, we found this font in google fonts
        custom_font = font.Font(family="Vidaloka-Regular", size=14)

        logo_image = tk.PhotoImage(file="calc.png")#Here we used the Tkinter's PhotoImage class to load an image file named "calc.png" and assigns it to the variable logo_image.
        width, height = logo_image.width(), logo_image.height()
        new_width, new_height = int(width * 0.5), int(height * 0.5) #calculates the dimensions of the image and Resizes the logo to 50%
        self.logo_image = logo_image.subsample(width // new_width, height // new_height)
        self.logo_label = tk.Label(root, image=self.logo_image, bg=self.bg_color)
        self.logo_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="nsew") #This places the logo label in the Tkinter grid.

        # Entry field for displaying and inputting numbers
        self.entry = tk.Entry(root, font=custom_font)
        self.entry.grid(row=1, column=0, rowspan=2,columnspan=5, padx=10, pady=10, sticky="nsew")  # Add sticky option


         # These are just Basic operation buttons
        operations = [
            ('Square Root', self.square_root),
            ('Power Of', self.power_of),
            ('%', self.percentage),
            ('*', self.multiplication),
            ('+', self.addition),
            ('-', self.subtraction),
            ('/', self.division)
         ]

        #Here we created the operation buttons
        #for loop which iterates over each item in the operations list
        for i, (text, command) in enumerate(operations):
            operation_button = tk.Button(root, text=text, padx=40, pady=20, bg='light yellow', bd=0, command=command, width=2)
            operation_button.grid(row=i // 2 + 3, column=i % 2 + 3, padx=5, pady=5)

        # Number buttons
        # Uses a lambda function to capture the current value of number and passes it to the self.insert_number method.
        buttons = []
        for number in range(10):
            button = tk.Button(root, text=str(number), padx=40, pady=20, bg='light yellow', bd=0, command=lambda num=number: self.insert_number(num), width=2)
            buttons.append(button)

        # Place number buttons (0 to 9)
        # Generates a list of positions for the number buttons
        positions = [(i // 3 + 3, i % 3) for i in range(13)]
        positions[9] = (6, 1)  # Change the position of button "9" to row 5, column 1
        # Modify the position of the "Power Of" button
        for pos, button in zip(positions, buttons[:13]):
            button.grid(row=pos[0], column=pos[1], padx=5, pady=5)

        # Add Clear button
        clear_button = tk.Button(root, text="Clear", padx=40, pady=20, bg='#E8C1C5', command=self.clear, width=2)
        clear_button.grid(row=7, column=1, columnspan=1, padx=5, pady=5)  # Set row and column for clear button

        # Decimal point button
        decimal_button = tk.Button(root, text=".", padx=40, pady=20, bg='light yellow', bd=0, command=lambda: self.insert_decimal())
        decimal_button.grid(row=7, column=2)

        # Equals button
        equals_button = tk.Button(root, text="=", padx=40, pady=20, bg='light yellow', bd=0, command=self.evaluate_expression)
        equals_button.grid(row=7, column=3, padx=5, pady=5)

        # Conversion buttons
        convert_to_binary_btn = tk.Button(root, text="To Binary", padx=40, pady=20, bg='light yellow', command=self.decimal_to_binary, width=2)
        convert_to_binary_btn.grid(row=6, column=0, padx=5, pady=5)

        convert_to_decimal_btn = tk.Button(root, text="To Decimal", padx=40, pady=20, bg='light yellow', command=self.binary_to_decimal, width=2)
        convert_to_decimal_btn.grid(row=6, column=2, padx=5, pady=5)

        # Factorial button
        factorial_button = tk.Button(root, text="Factorial", padx=40, pady=20, bg='light yellow', command=self.calculate_factorial, width=2)
        factorial_button.grid(row=6, column=4, padx=5, pady=5)

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
        self.logo_label.configure(bg=color)

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

    # The insert_decimal method is designed to triggered the tkinker decimal point function. 
    #This code adds a decimal point to the end of the entry field's content if certain conditions are met.  
    def insert_decimal(self):
        current = self.entry.get()
        if current and '.' not in current:
            self.entry.insert(tk.END, '.')

    #the binary_to_decimal method is designed to convert a binary number into its decimal equivalent. 
    #It handles both successful conversions and cases where the input is not a valid binary number.
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
            self.entry.insert(0, "Error")#Clear the entry field and insert the string "Error" to indicate that the operation couldn't be performed due to invalid input.

     
    #This adds the power of function 
    def power_of(self):
        try:
            self.entry.insert(tk.END, '**')  # Insert '**' into the entry box
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")#Clear the entry field and insert the string "Error" to indicate that the operation couldn't be performed due to invalid input.



    #This adds the percentage function 
    def percentage(self):
        try:
            value = float(self.entry.get())
            result = value / 100 #Calculate the percentage of the obtained value by dividing it by 100.
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")#Clear the entry field and insert the string "Error" to indicate that the operation couldn't be performed due to invalid input.

    #This adds the multiplication function 
    def multiplication(self):
        try:
            value = float(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(value) + '*')
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")#Clear the entry field and insert the string "Error" to indicate that the operation couldn't be performed due to invalid input.

    #This adds the additin function 
    def addition(self):
        try:
            value = float(self.entry.get()) # This Retrieve the value from the Tkinter entry widget and convert it to a floating-point number.
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(value) + '+')
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")#Clear the entry field and insert the string "Error" to indicate that the operation couldn't be performed due to invalid input.

    #This adds the subtraction function 
    def subtraction(self):
        try:
            value = float(self.entry.get())#Retrieve the value from the Tkinter entry widget and convert it to a floating-point number.
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(value) + '-')
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")#Clear the entry field and insert the string "Error" to indicate that the operation couldn't be performed due to invalid input.

    #This adds the division function 
    def division(self):
        try:
            value = float(self.entry.get())#This Retrieve the value from the Tkinter entry widget and convert it to a floating-point number.
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(value) + '/')
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")#Clear the entry field and insert the string "Error" to indicate that the operation couldn't be performed due to invalid input.

    #retrieves the current content of the entry field associated with the class instance and stores it in the variable expression.
    def evaluate_expression(self):
        expression = self.entry.get()
        try:
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except (ValueError, SyntaxError):
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")#Clear the entry field and insert the string "Error" to indicate that the operation couldn't be performed due to invalid input.

    #This creates the clear function 
    def clear(self):
        self.entry.delete(0, tk.END)

    def calculate_factorial(self):
        value = self.entry.get()
        try:
            value = int(value)#Convert the input value to an integer.
            if value < 0:
                raise ValueError("Factorial is defined only for non-negative integers.")#Check if the converted value is a non-negative integer. If not, raise a ValueError with an appropriate error message.
            result = Decimal(1)
            for i in range(2, value + 1):
                result *= Decimal(i)
            self.entry.delete(0, tk.END) 
            self.entry.insert(0, str(result))
        except ValueError as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(e))
            #Clear the entry field and insert the error message as a string to indicate that the operation couldn't be performed due to invalid input.

    def calculate_factorial_threaded(self, value):
        result = math.factorial(value)#uses the math function to calculate the factorial of the given value
        self.root.after(0, lambda: self.update_gui_with_factorial(result))#prevents potential delays in responsiveness.

    def update_gui_with_factorial(self, result):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(result))

    #This runs the calculator 
def run_calculator():#Create the main Tkinter window
    root = tk.Tk()
    # the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    #Set the geometry of the window to half of the screen size, centered
    root.geometry(f"{screen_width // 2}x{screen_height // 2}+{screen_width // 4}+{screen_height // 4}")
    global calculator
    calculator = Calculator(root)
    root.mainloop()
# Check if the script is being run directly
if __name__ == "__main__":
    run_calculator()