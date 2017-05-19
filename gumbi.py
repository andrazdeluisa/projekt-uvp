import tkinter
import tkinter.messagebox

okno=tkinter.Tk()

class Gumb:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        self.gumb=tkinter.Button(okno,text=str(i)+','+str(j),command=self.funkcija)
    def funkcija(self):
        tkinter.messagebox.showinfo('pritisnili ste '+str(self.i)+str(self.j))

class Gumbi:
    def __init__(self):
        for i in range(10):
            for j in range(10):
                gumb=Gumb(i,j)
                gumb.gumb.place(x=30*i,y=30*j)

g=Gumbi()

okno.mainloop()
