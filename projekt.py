import tkinter as tk
import tkinter.messagebox
import model

FONT = ("Arial",14,"bold")
IGRA = model.Igra(10, 10, 10)


class PaziMina:
   def __init__(self, okno):
      self.plosca = IGRA

      self.obvestilo = tk.Label(okno, text='Dobrodošel v igri Pazi, mina!')
      self.obvestilo.grid(row=0, column=0)

      prikaz_plosce = tk.Frame(okno)
      self.gumbi = []
      for vrstica in range(self.plosca.st_vrstic):
         vrstica_gumbov = []
         for stolpec in range(self.plosca.st_stolpcev):
            def pritisni_gumb(event, vrstica = vrstica, stolpec = stolpec):
               self.odkrij(vrstica, stolpec)
            def postavi_zastavico(event, vrstica = vrstica, stolpec = stolpec):
               self.zastavica(vrstica, stolpec)
            gumb = tk.Button(prikaz_plosce, text='', height=1, width=2, font=FONT) 
            gumb.grid(row=vrstica, column=stolpec)
            gumb.bind('<Button-1>', pritisni_gumb)
            gumb.bind('<Button-3>', postavi_zastavico)
            vrstica_gumbov.append(gumb)
         self.gumbi.append(vrstica_gumbov)
      prikaz_plosce.grid(row=1, column=0)


   def odkrij(self, vrstica, stolpec):
      polje = self.plosca.seznam_polj[vrstica][stolpec]
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
         self.gumbi[vrstica][stolpec].config(text='#', bg='blue')
      elif not polje.zastavica:
         self.gumbi[vrstica][stolpec].config(text='', bg='grey')

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


