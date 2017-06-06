import tkinter as tk
import tkinter.messagebox
import model

FONT = ("Arial", 14, "bold")
VRSTICE = 10
STOLPCI = 10
MINE = 10



class PaziMina:
   def __init__(self, okno):
      self.plosca = model.Igra(VRSTICE, STOLPCI, MINE)

      self.obvestilo = tk.Label(okno, text='Dobrodošel v igri Pazi, mina!', height=2, font=FONT)
      self.obvestilo.grid(row=0, column=0)

      self.stevec_min = tk.Label(okno, text='{}'.format(MINE), width=4, font=FONT)
      self.stevec_min.grid(row=0, column=1)


      prikaz_plosce = tk.Frame(okno)
      self.gumbi = []
      for vrstica in range(self.plosca.st_vrstic):
         vrstica_gumbov = []
         for stolpec in range(self.plosca.st_stolpcev):
            def pritisni_gumb(event, vrstica = vrstica, stolpec = stolpec):
               self.odkrij(vrstica, stolpec)
            def postavi_zastavico(event, vrstica = vrstica, stolpec = stolpec):
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
      self.stevec_min.config(text='{}'.format(MINE - st_zastavic))


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
            if self.plosca.seznam_polj[vrstica][stolpec] in self.plosca.seznam_min:   
               gumb = self.gumbi[vrstica][stolpec]
               gumb.config(text='*', state='disabled', bg = 'tomato')
      tk.messagebox.showerror('Pazi mina', 'Game over')              


   def zmaga2(self):
      for vrstica in range(self.plosca.st_vrstic):
         for stolpec in range(self.plosca.st_stolpcev):
            if self.plosca.seznam_polj[vrstica][stolpec] in self.plosca.seznam_min:   
               gumb = self.gumbi[vrstica][stolpec]
               gumb.config(text='*', state='disabled', bg = 'lawn green')
      tk.messagebox.showinfo('Pazi mina', 'Bravo, zmaga!!!')



okno = tk.Tk()
moja_igra = PaziMina(okno)
okno.mainloop()


