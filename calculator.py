import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("HEM Calculator")
        root.configure(bg='lightblue')

        # Load custom font
        custom_font = font.Font(family="Vidaloka-Regular", size=14)

        # Entry field for displaying and inputting numbers
        self.entry = tk.Entry(root, font=custom_font)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Number buttons
        buttons = []
        for number in range(10):
            button = tk.Button(root, text=str(number), padx=40, pady=20, bg='light yellow', bd=0, command=lambda num=number: insert_number(num))
            buttons.append(button)

        # Place number buttons (0 to 9)
        positions = [(i // 3 + 2, i % 3) for i in range(13)]
        positions[9] = (5, 1)  # Change the position of button "9" to row 4, column 1
        for pos, button in zip(positions, buttons[:13]):
            button.grid(row=pos[0], column=pos[1])

        # Add Clear button
        clear_button = tk.Button(root, text="Clear", padx=40, pady=20, command=Clear)
        clear_button.grid(row=6, column=2)

        # Conversion buttons
        convert_to_binary_btn = tk.Button(root, text="To Binary", padx=29, pady=20, command=decimal_to_binary)
        convert_to_binary_btn.grid(row=5, column=0)

        convert_to_decimal_btn = tk.Button(root, text="To Decimal", padx=29, pady=20, command=binary_to_decimal)
        convert_to_decimal_btn.grid(row=5, column=2)


# Function to insert a number into the entry field
def insert_number(number):
    current = calculator.entry.get()
    calculator.entry.delete(0, tk.END)
    calculator.entry.insert(0, str(current) + str(number))

def binary_to_decimal():
    # use the bin() function to convert from a decimal value to its corresponding binary value.
    binary_input = calculator.entry.get()
    try:
        decimal_output = int(binary_input, 2)
        calculator.entry.delete(0, tk.END)
        calculator.entry.insert(0, str(decimal_output))
    except ValueError:
        calculator.entry.delete(0, tk.END)
        calculator.entry.insert(0, "Error")

def decimal_to_binary():
    # Convert a decimal number to its binary equivalent
    decimal_input = calculator.entry.get()
    try:
        decimal_input = int(decimal_input)
        binary_output = bin(decimal_input)
        calculator.entry.delete(0, tk.END)
        calculator.entry.insert(0, str(binary_output))
    except ValueError:
        calculator.entry.delete(0, tk.END)
        calculator.entry.insert(0, "Error")

def SquareRoot():
    # find out the square root of a number
    pass

def PowerOf():
    # make use of power of function
    pass

def PerIncrease():
    # percentage increase
    pass

def PerDecrease():
    # percentage decrease
    pass

#Multiplication/Division x /
def Multiplication():
    # multiply numbers
    pass

def Addition():
    # add numbers together
    pass

def Subtraction():
    # when user selects this subtract
    pass

def Division():
    # when user presses this divide
    pass

def Equals():
    # when user presses equals execute this
    pass

def Clear():
    # clear the contents of any user input
    calculator.entry.delete(0, tk.END)

# Function for running calculator
def run_calculator():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width // 2}x{screen_height // 2}+{screen_width // 4}+{screen_height // 4}")  # Set geometry to fit 50% of the screen
    global calculator
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    run_calculator()
