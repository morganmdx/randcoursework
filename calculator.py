# import libraries
import threading
import tkinter as hem
from tkinter import font

#creating a basic calculator in Python, with a fully functional GUI
class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("HEM Calculator")
        root.configure(bg='lightblue')

        # Load custom font
        custom_font_path = "C:\Users\morga\OneDrive\Documents\GitHub\randcoursework\Vidaloka-Regular.ttf"  # Replace with the actual path to your font file
        custom_font = font.Font(family="YourCustomFont", size=14, file=custom_font_path)

        # Entry field for displaying and inputting numbers
        self.entry = tk.Entry(root, font=custom_font)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# use any library they see fit to help implement the GUI
        
def BinarytoDecimal():
    # use the bin() function to convert from a decimal value to its corresponding binary value.
    print()
    a = 79
    # Base 2(binary)
    bin_a = bin(a)
    print(bin_a)
    print(int(bin_a, 2)) #Base 2(binary)

def SquareRoot():
    # find out the square root of a number
    print()

def PowerOf():
    # make use of power of function
    print()

def PerIncrease():
    # percentage increase
    print(number*1.2)

def PerDecrease():
    # percentage decrease
    print()

#Multiplication/Division x /
def Multiplication():
    # multiply numbers
    print()

def Addition():
    # add numbers together
    print()

def Subtraction():
    # when user selects this subtract
    print()

def Division():
    # when user presses this divide
    print()

def Equals():
    # when user presses equals execute this
    print()

def Clear():
    # clear the contents of any user input
    print()


# Our criteria as follows:
# Subtraction/Additional - +
# Equal/Clear = C
# Should operate fully with precision, there should be no rounding or missing decimal places

# Multi-threading 
    
#function for running calculator
def run_calculator():
    root = hem.Tk()
    my_calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    run_calculator()