from tkinter import *

def Call():
    msg = Label(window, text = "Don't press the button again!")
    msg.place(x = 30, y = 50)
    button["bg"] = "blue"
    button["fg"] = "white"

window = Tk()
window.geometry("200x100")
button = Button(text = "press me", command = Call)
button.place(x = 30, y = 20, width=120, height=25)
window.mainloop()
