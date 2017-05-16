import tkinter
import tkinter.messagebox

top = tkinter.Tk()

def zmaga():
   tkinter.messagebox.showinfo( 'Pazi mina', 'Bravo, zmaga!!!')

def poraz():
   tkinter.messagebox.showinfo( 'Pazi mina', 'Game over')

B = tkinter.Button(top, text = 'Hello', command = zmaga)
C = tkinter.Button(top, text = 'Živjo', command = poraz)


B.pack()
C.pack()



def action():
    n=0
    tkinter.messagebox.showinfo( 'd', str(n))
	


for i in range(10):
    button = tkinter.Button(top, text='press', command = action)
    button.pack()

top.mainloop()
