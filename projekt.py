import tkinter as tk
import tkinter.messagebox
import model

FONT = ("Arial", 14, "bold")
FONT2 = ("Arial", 12, "bold")

class PaziMina:
   def __init__(self, okno, vrstice, stolpci, mine):
      self.vrstice = vrstice
      self.stolpci = stolpci
      self.mine = mine
      self.okno = okno
      
      self.plosca = model.Igra(self.vrstice, self.stolpci, self.mine)

      self.obvestilo = tk.Label(self.okno, text='Dobrodošel v igri Pazi, mina!', height=2, font=FONT)
      self.obvestilo.grid(row=0, column=0)

      self.stevec_min = tk.Label(self.okno, text='{}'.format(self.mine), width=4, font=FONT)
      self.stevec_min.grid(row=0, column=1)

      prikaz_plosce = tk.Frame(self.okno)
      self.gumbi = []
      for vrstica in range(self.plosca.st_vrstic):
         vrstica_gumbov = []
         for stolpec in range(self.plosca.st_stolpcev):
            def pritisni_gumb(event, vrstica=vrstica, stolpec=stolpec):
               self.odkrij(vrstica, stolpec)
            def postavi_zastavico(event, vrstica=vrstica, stolpec=stolpec):
               self.zastavica(vrstica, stolpec)
            gumb = tk.Button(prikaz_plosce, text='', height=1, width=2, font=FONT, bg='light grey') 
            gumb.grid(row=vrstica, column=stolpec)
            gumb.bind('<Button-1>', pritisni_gumb)
            gumb.bind('<Button-3>', postavi_zastavico)
            vrstica_gumbov.append(gumb)
         self.gumbi.append(vrstica_gumbov)
      prikaz_plosce.grid(row=1, column=0)


   def odkrij(self, vrstica, stolpec):
      polje = self.plosca.seznam_polj[vrstica][stolpec]
      if polje.zastavica:
         return

      self.plosca.odkrij_polje(vrstica, stolpec)
      self.osvezi_prikaz()

      if polje in self.plosca.seznam_min:
         self.poraz()
      if self.plosca.zmaga():
         self.zmaga2()


   def zastavica(self, vrstica, stolpec):
      polje = self.plosca.seznam_polj[vrstica][stolpec]
      if polje in self.plosca.seznam_odkritih:
         return

      self.plosca.postavi_zastavico(vrstica, stolpec)
      if polje.zastavica:
         self.gumbi[vrstica][stolpec].config(text='#', bg='cyan')
      elif not polje.zastavica:
         self.gumbi[vrstica][stolpec].config(text='', bg='light grey')
      st_zastavic = 0

      for vrstica in range(self.plosca.st_vrstic):
         for stolpec in range(self.plosca.st_stolpcev):
            polje = self.plosca.seznam_polj[vrstica][stolpec]
            if polje.zastavica:
               st_zastavic += 1
      self.stevec_min.config(text='{}'.format(self.mine - st_zastavic))


   def osvezi_prikaz(self):
      for vrstica in range(self.plosca.st_vrstic):
         for stolpec in range(self.plosca.st_stolpcev):
            polje = self.plosca.seznam_polj[vrstica][stolpec]
            if polje in self.plosca.seznam_odkritih:   
               gumb = self.gumbi[vrstica][stolpec]
               if polje.vrednost > 0:
                  gumb.config(text='{}'.format(polje.vrednost), state='disabled', bg='white')
               elif polje.vrednost == 0:
                  gumb.config(text='', state='disabled', bg='white')

                           
   def poraz(self):
      for vrstica in range(self.plosca.st_vrstic):
         for stolpec in range(self.plosca.st_stolpcev):
            gumb = self.gumbi[vrstica][stolpec]
            gumb.config(state='disabled') 
            if self.plosca.seznam_polj[vrstica][stolpec] in self.plosca.seznam_min:   
               gumb.config(text='*', bg='tomato')     
      tk.messagebox.showerror('Pazi mina', 'Game over')
      self.okno.destroy()


   def zmaga2(self):
      for vrstica in range(self.plosca.st_vrstic):
         for stolpec in range(self.plosca.st_stolpcev):
            gumb = self.gumbi[vrstica][stolpec]
            if self.plosca.seznam_polj[vrstica][stolpec] in self.plosca.seznam_min:     
               gumb.config(text='*', state='disabled', bg='lawn green')
      tk.messagebox.showinfo('Pazi mina', 'Bravo, zmaga!!!')
      self.okno.destroy()




def lahko():
   okno2 = tk.Toplevel()
   moja_igra = PaziMina(okno2, 9, 9, 10)

def srednje():
   okno2 = tk.Toplevel()
   moja_igra = PaziMina(okno2, 16, 16, 40)

def tezko():
   okno2 = tk.Toplevel()
   moja_igra = PaziMina(okno2, 16, 30, 99)
   



okno1 = tk.Tk()

tezavnost = tk.Label(okno1, text='Izberi težavnost', font=FONT, height=2, width=14)
tezavnost.pack()

gumb1 = tk.Button(text='Lahko', command=lahko, font=FONT2, height=2, width=10)
gumb1.pack()

gumb2 = tk.Button(text='Srednje', command=srednje, font=FONT2, height=2, width=10)
gumb2.pack()

gumb3 = tk.Button(text='Težko', command=tezko, font=FONT2, height=2, width=10)
gumb3.pack()

okno1.mainloop()
