from tkinter import *

window = Tk()
window.minsize(width=300, height=200)

miles_label = Label(text="Miles")
miles_label.config(font=('Arial', 18, 'normal'))
miles_label.grid(row=0, column=2)



window.mainloop()
