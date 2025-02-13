import tkinter as tk
from tkinter import ttk, messagebox

# Helper function to validate binary strings
def is_valid_binary(binary_str):
    return all(bit in ('0', '1') for bit in binary_str)

# Function to perform binary calculations
def calculate():
    # Retrieve inputs from user
    binary_num1 = entry_bin1.get()
    binary_num2 = entry_bin2.get()
    operation = operation_var.get()
    
    # Check if both binary numbers are valid
    if not (is_valid_binary(binary_num1) and is_valid_binary(binary_num2)):
        messagebox.showerror("Invalid Input", "Please enter valid binary numbers.")
        return
    
    try:
        # Convert binary numbers to decimal
        decimal_num1 = int(binary_num1, 2)
        decimal_num2 = int(binary_num2, 2)
    except ValueError:
        messagebox.showerror("Invalid Input", "There was an error with the input. Please try again.")
        return
    
    try:
        # Perform the selected operation
        if operation == '+':
            result = decimal_num1 + decimal_num2
        elif operation == '-':
            result = decimal_num1 - decimal_num2
        elif operation == '*':
            result = decimal_num1 * decimal_num2
        elif operation == '/':
            # Handle division by zero
            if decimal_num2 == 0:
                raise ZeroDivisionError
            result = decimal_num1 // decimal_num2
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero. Please adjust the input.")
        return
    
    # Convert result back to binary and update the label
    result_binary = bin(result).replace('0b', '')
    result_label.config(text=f"Result: {result_binary}")

# Function to convert binary to decimal
def convert_binary_to_decimal():
    binary_str = entry_conv_bin.get()
    
    if not is_valid_binary(binary_str):
        messagebox.showerror("Invalid Binary", "Please enter a valid binary number.")
        return
    
    decimal_value = int(binary_str, 2)
    label_conv_bin_result.config(text=f"Decimal: {decimal_value}")

# Function to convert decimal to binary
def convert_decimal_to_binary():
    decimal_str = entry_conv_dec.get()
    
    try:
        decimal_value = int(decimal_str)
    except ValueError:
        messagebox.showerror("Invalid Decimal", "Please enter a valid decimal number.")
        return
    
    binary_value = bin(decimal_value).replace('0b', '')
    label_conv_dec_result.config(text=f"Binary: {binary_value}")

# Set up the main application window
root = tk.Tk()
root.title("Cute Binary Calculator")
root.geometry("600x500")
root.config(bg="#f0f8ff")

# Define style for widgets
style = ttk.Style()
style.configure('TButton', background='#b0e0e6', foreground='#333333', font=('Arial', 12, 'bold'))
style.configure('TLabel', background='#f0f8ff', font=('Arial', 12), foreground='#333333')
style.configure('TEntry', font=('Arial', 12), relief="solid")
style.configure('TOptionMenu', font=('Arial', 12))

# Create the binary calculator frame
calc_frame = tk.Frame(root, bg="#b0e0e6", padx=20, pady=20)
calc_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

# First binary number input
ttk.Label(calc_frame, text="Enter First Binary Number", anchor="w").grid(row=0, column=0, padx=5, pady=10, sticky="w")
entry_bin1 = tk.Entry(calc_frame, relief="solid", font=('Arial', 14), width=20)
entry_bin1.grid(row=0, column=1, padx=5, pady=10)

# Operation dropdown menu
ttk.Label(calc_frame, text="Choose Operation", anchor="w").grid(row=1, column=0, padx=5, pady=10, sticky="w")
operation_var = tk.StringVar(value='+')
operations = ['+', '-', '*', '/']
operation_menu = ttk.OptionMenu(calc_frame, operation_var, operation_var.get(), *operations)
operation_menu.grid(row=1, column=1, sticky="ew", padx=5, pady=10)

# Second binary number input
ttk.Label(calc_frame, text="Enter Second Binary Number", anchor="w").grid(row=2, column=0, padx=5, pady=10, sticky="w")
entry_bin2 = tk.Entry(calc_frame, relief="solid", font=('Arial', 14), width=20)
entry_bin2.grid(row=2, column=1, padx=5, pady=10)

# Result label
result_label = ttk.Label(calc_frame, text="Result: ", anchor="w", font=('Arial', 14))
result_label.grid(row=3, column=0, columnspan=2, pady=15, sticky="w")

# Calculate button
ttk.Button(calc_frame, text="Calculate", command=calculate).grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")

# Create the conversion frame
conv_frame = tk.Frame(root, bg="#b0e0e6", padx=20, pady=20)
conv_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

# Binary to Decimal conversion
ttk.Label(conv_frame, text="Convert Binary to Decimal", anchor="w").grid(row=0, column=0, padx=5, pady=10, sticky="w")
entry_conv_bin = tk.Entry(conv_frame, relief="solid", font=('Arial', 14), width=20)
entry_conv_bin.grid(row=0, column=1, padx=5, pady=10)
ttk.Button(conv_frame, text="Convert", command=convert_binary_to_decimal).grid(row=0, column=2, padx=10, pady=10)
label_conv_bin_result = ttk.Label(conv_frame, text="Decimal: ", anchor="w", font=('Arial', 14))
label_conv_bin_result.grid(row=0, column=3, padx=5)

# Decimal to Binary conversion
ttk.Label(conv_frame, text="Convert Decimal to Binary", anchor="w").grid(row=1, column=0, padx=5, pady=10, sticky="w")
entry_conv_dec = tk.Entry(conv_frame, relief="solid", font=('Arial', 14), width=20)
entry_conv_dec.grid(row=1, column=1, padx=5, pady=10)
ttk.Button(conv_frame, text="Convert", command=convert_decimal_to_binary).grid(row=1, column=2, padx=10, pady=10)
label_conv_dec_result = ttk.Label(conv_frame, text="Binary: ", anchor="w", font=('Arial', 14))
label_conv_dec_result.grid(row=1, column=3, padx=5)

# About section
about_frame = ttk.Frame(root)
about_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
ttk.Label(about_frame, text="A simple binary calculator and converter", anchor="center", font=("Arial", 12, 'italic'), background="#f0f8ff").pack()

# Start the main loop
root.mainloop()
