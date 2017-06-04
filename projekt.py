import tkinter as tk
import tkinter.messagebox
import model


class PaziMina:
   def __init__(self, okno):
      self.plosca = model.IGRA

      self.obvestilo = tk.Label(okno, text='Dobrodošel v igri Pazi, mina!')
      self.obvestilo.grid(row=0, column=0)

      prikaz_plosce = tk.Frame(okno)
      self.gumbi = []
      for vrstica in range(self.plosca.st_vrstic):
         vrstica_gumbov = []
         for stolpec in range(self.plosca.st_stolpcev):
            def pritisni_gumb(vrstica = vrstica, stolpec = stolpec):
               self.odkrij(vrstica, stolpec)
            gumb = tk.Button(prikaz_plosce, text='', height=2, width=2, command=pritisni_gumb, font=("Arial",14,"bold")) 
            gumb.grid(row=vrstica, column=stolpec)
            vrstica_gumbov.append(gumb)
         self.gumbi.append(vrstica_gumbov)
      prikaz_plosce.grid(row=1, column=0)


   def odkrij(self, vrstica, stolpec):
      self.plosca.seznam_polj[vrstica][stolpec].odkrij_polje()
      self.osvezi_prikaz()
      if self.plosca.seznam_polj[vrstica][stolpec] in self.plosca.seznam_min:
         self.poraz()
      if self.plosca.zmaga():
         self.zmaga2()

   def zastavica(self, vrstica, stolpec):
      self.plosca.seznam_polj[vrstica][stolpec].postavi_zastavico()
      self.gumbi[vrstica][stolpec].config(text='#', state='disabled', bg = 'blue')

   def osvezi_prikaz(self):
      for vrstica in range(self.plosca.st_vrstic):
         for stolpec in range(self.plosca.st_stolpcev):
            if self.plosca.seznam_polj[vrstica][stolpec] in self.plosca.seznam_odkritih:   
               gumb = self.gumbi[vrstica][stolpec]
               gumb.config(text='{}'.format(self.plosca.seznam_polj[vrstica][stolpec].vrednost), state='disabled', bg = 'white')
               
                           
   def poraz(self):
      for vrstica in range(self.plosca.st_vrstic):
         for stolpec in range(self.plosca.st_stolpcev):
            if self.plosca.seznam_polj[vrstica][stolpec] in self.plosca.seznam_min:   
               gumb = self.gumbi[vrstica][stolpec]
               gumb.config(text='*', state='disabled', bg = 'red')
      tk.messagebox.showinfo('Pazi mina', 'Game over')              

   def zmaga2(self):
      for vrstica in range(self.plosca.st_vrstic):
         for stolpec in range(self.plosca.st_stolpcev):
            if self.plosca.seznam_polj[vrstica][stolpec] in self.plosca.seznam_min:   
               gumb = self.gumbi[vrstica][stolpec]
               gumb.config(text='*', state='disabled', bg = 'green')
      tk.messagebox.showinfo('Pazi mina', 'Bravo, zmaga!!!')



okno = tk.Tk()
moja_igra = PaziMina(okno)
okno.mainloop()


