import tkinter as tk

# Function to add a number or operator to the display
def button_click(item):
    current = display.get()
    if item in '0123456789':
        display.insert(tk.END, str(item))
    elif item in '+-*/':
       
 

# Function to clear the display
def button_clear():
    display.delete(0, tk.END)

# Function to evaluate the expression
def button_equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Error")
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Function to handle key presses
def key_press(event):
    char = event.char
    if char in '0123456789+-*/':
        button_click(char)
    elif char == '\r':  # Enter key
        button_equal()
    elif char == '\b':  # Backspace key
        button_clear()

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Define colors
button_bg = '#f0f0f0'  # Light grey
button_active_bg = '#e0e0e0'  # Light grey (slightly darker for active state)
button_fg = '#000000'  # Black
button_font = ('Helvetica', 18, 'bold')

# Create the display area
display = tk.Entry(root, width=35, borderwidth=5, font=('Helvetica', 24))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create digit and operator buttons
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('0', 4, 1), ('C', 4, 0), ('=', 4, 2), ('/', 4, 3)
]

for (text, row, col) in buttons:
    if text in '0123456789':
        btn = tk.Button(root, text=text, padx=20, pady=20, bg=button_bg, activebackground=button_active_bg,
                        fg=button_fg, font=button_font, command=lambda t=text: button_click(t))
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=20, bg='#ff6347', activebackground='#ff6347',
                        fg='white', font=button_font, command=button_clear)
    elif text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, bg='#008080', activebackground='#008080',
                        fg='white', font=button_font, command=button_equal)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, bg='#87ceeb', activebackground='#87ceeb',
                        fg=button_fg, font=button_font, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col)

# Bind keyboard inputs
root.bind('<Key>', key_press)

root.mainloop()
