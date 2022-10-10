from Tkinter import *
from tkFileDialog import askopenfilename

window = Tk()
window.title("Sample Python GUI program")
lbl = Label(window, text="Sample Label", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=0, row=1)
txt2 = Entry(window, width=10)
txt2.grid(column=0, row=2)
def clicked():
	file = askopenfilename()
btn = Button(window,text='Open', command=clicked)
btn.grid(column=0, row=3)
window.geometry('550x400')
window.mainloop()
