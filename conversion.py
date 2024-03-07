import tkinter as tk

def insert_number(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def binary_to_decimal():
    binary_input = entry.get()
    try:
        decimal_output = int(binary_input, 2)
        entry.delete(0, tk.END)
        entry.insert(0, str(decimal_output))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def decimal_to_binary():
    decimal_input = entry.get()
    try:
        binary_output = bin(int(decimal_input))[2:]
        entry.delete(0, tk.END)
        entry.insert(0, str(binary_output))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Converter")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Number buttons
buttons = []
for number in range(10):
    button = tk.Button(root, text=str(number), padx=40, pady=20, command=lambda num=number: insert_number(num))
    buttons.append(button)

# Place number buttons
positions = [(i // 3 + 1, i % 3) for i in range(9, -1, -1)]
for pos, button in zip(positions, buttons[::-1]):
    button.grid(row=pos[0], column=pos[1])

# Conversion buttons
convert_to_binary_btn = tk.Button(root, text="To Binary", padx=29, pady=20, command=decimal_to_binary)
convert_to_binary_btn.grid(row=4, column=0)

convert_to_decimal_btn = tk.Button(root, text="To Decimal", padx=29, pady=20, command=binary_to_decimal)
convert_to_decimal_btn.grid(row=4, column=1)

root.mainloop()
