import tkinter as tk

def press_button(value):
    entry.insert(tk.END, value)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    tk.Button(root, text=button, width=7, command=lambda value=button: press_button(value)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="C", width=7, command=clear).grid(row=row, column=0)

tk.Button(root, text="=", width=7, command=calculate).grid(row=row, column=1)

root.mainloop()
