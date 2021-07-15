from tkinter import *
from tkinter import messagebox

def add_digit(digit):
    value = calc.get() + digit
    calc.delete(0, END)
    calc.insert(0, value)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    value = value + operation
    calc.delete(0, END)
    calc.insert(0, value)

def clear():
    value = calc.get()
    value = value[:-1]
    calc.delete(0, END)
    calc.insert(0, value)

def calculate():
    value = calc.get()
    if len(value) and value [-1] in '+-*/':
        value = value[:-1] + value[-1] + value [:-1]
    if len(value):
        try:
            resulr = eval(value)
            calc.delete(0, END)
            calc.insert(0, resulr)
        except ZeroDivisionError:
            messagebox.showinfo('ERROR!', 'You cannot divide by zero!')
            calc.delete(0, END)
        except (NameError, SyntaxError):
            messagebox.showinfo('ERROR!', 'Problems with syntax!')
            calc.delete(0, END)

def make_digit_button(digit):
    return Button(text=digit, font = ('Arial', 20), bd = 2, command=lambda : add_digit(digit))

def make_operation_button(operation):
    return Button(text=operation, font = ('Arial', 20), bd = 2, command=lambda : add_operation(operation))

def make_calc_button(operation):
    return Button(text=operation, font = ('Arial', 20), bd = 2, command=lambda : calculate())

def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == '\x08':
        clear()

root = Tk()
root.title("Calculator")
root.geometry("240x270")

root.bind('<Key>', press_key)

calc = Entry(root, justify=RIGHT, font = ('Arial', 15), width= 15)
calc.grid(row = 0, column = 0, columnspan=4, stick = 'we', padx = 2)

make_digit_button('1').grid(row = 1, column=0, stick = 'wens', padx = 2, pady = 2)
make_digit_button('2').grid(row = 1, column=1, stick = 'wens', padx = 2, pady = 2)
make_digit_button('3').grid(row = 1, column=2, stick = 'wens', padx = 2, pady = 2)
make_digit_button('4').grid(row = 2, column=0, stick = 'wens', padx = 2, pady = 2)
make_digit_button('5').grid(row = 2, column=1, stick = 'wens', padx = 2, pady = 2)
make_digit_button('6').grid(row = 2, column=2, stick = 'wens', padx = 2, pady = 2)
make_digit_button('7').grid(row = 3, column=0, stick = 'wens', padx = 2, pady = 2)
make_digit_button('8').grid(row = 3, column=1, stick = 'wens', padx = 2, pady = 2)
make_digit_button('9').grid(row = 3, column=2, stick = 'wens', padx = 2, pady = 2)
make_digit_button('0').grid(row = 4, column=1, stick = 'wens', padx = 2, pady = 2)

make_operation_button('+').grid(row = 1, column=3, stick = 'wens', padx = 2, pady = 2)
make_operation_button('-').grid(row = 2, column=3, stick = 'wens', padx = 2, pady = 2)
make_operation_button('*').grid(row = 3, column=3, stick = 'wens', padx = 2, pady = 2)
make_operation_button('/').grid(row = 4, column=3, stick = 'wens', padx = 2, pady = 2)
make_operation_button('.').grid(row = 4, column=2, stick = 'wens', padx = 2, pady = 2)


make_calc_button('=').grid(row = 4, column=0, stick = 'wens', padx = 2, pady = 2)

root.grid_columnconfigure(0,minsize = 60)
root.grid_columnconfigure(1,minsize = 60)
root.grid_columnconfigure(2,minsize = 60)
root.grid_columnconfigure(3,minsize = 60)

root.grid_rowconfigure(1,minsize = 60)
root.grid_rowconfigure(2,minsize = 60)
root.grid_rowconfigure(3,minsize = 60)
root.grid_rowconfigure(4,minsize = 60)

root.mainloop()