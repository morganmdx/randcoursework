import tkinter as tk
from tkinter import messagebox
import threading

def calculate():
    try:
        result = eval(entry.get())
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def calculate_thread():
    thread = threading.Thread(target=calculate)
    thread.start()

def main():
    root = tk.Tk()
    root.title("Calculator")

    entry = tk.Entry(root, width=30)
    entry.pack(pady=10)

    calculate_button = tk.Button(root, text="Calculate", command=calculate_thread)
    calculate_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
