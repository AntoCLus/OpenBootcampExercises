import tkinter

window = tkinter.Tk()

label_greeting = tkinter.Label(window, text="Good Morning. Welcome to our GUI course.", bg="green", fg="black", font=("verdana", 20, "bold"))
label_greeting.pack(ipadx=50, ipady=50, fill='both')
label_farewell = tkinter.Label(window, text="Thanks for watching", bg="blue", fg="black")
label_farewell.pack(ipadx=50, ipady=50, fill='both')


window.mainloop()