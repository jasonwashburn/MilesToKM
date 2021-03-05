from tkinter import *
from tkinter import ttk

FONT = ('Arial', 24, 'normal')


def calc_clicked():
    miles = float(miles_entry.get())
    kilometers = miles * 1.609
    answer_label.config(text=f"{kilometers}")


# Main Window
window = Tk()
window.minsize(width=50, height=50)
window.config(padx=20, pady=20)


# Miles Entry
miles_entry = Entry(width=10, font=FONT, justify='center')
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles")
miles_label.config(font=FONT)
miles_label.grid(column=2, row=0)

# Is Equal Label
is_equal_label = Label(text="is equal to")
is_equal_label.config(font=FONT)
is_equal_label.grid(column=0, row=1)

# Answer Label
answer_label = Label(text='0')
answer_label.config(font=FONT)
answer_label.grid(column=1, row=1)

# Km Label
km_label = Label(text='Km')
km_label.config(font=FONT)
km_label.grid(column=2, row=1)

# Calculate Button (used ttk.Button rather than tk.Button because of MacOS rendering issues
s = ttk.Style()
s.configure('my.TButton', font=FONT)
calc_button = ttk.Button(text="Calculate", style='my.TButton', command=calc_clicked)
calc_button.grid(column=1, row=2)

window.mainloop()
