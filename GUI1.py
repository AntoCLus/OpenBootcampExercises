import tkinter
from tkinter import Tk
from tkinter import ttk
window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

selected = tkinter.StringVar()

r1 = ttk.Radiobutton(window, text='si', value='1', variable=selected)
r2 = ttk.Radiobutton(window, text='no', value='1', variable=selected)
r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)


##check
def miFuncion():
    print('clicado')
checkbox  = ttk.Checkbutton(window, text='Reiniciar', variable=selected, command=miFuncion)
checkbox.grid(row=0, column=0)
window.mainloop()

#revisar cuando lo ejecuto se clickea todo. deberia ser uno a la vez.