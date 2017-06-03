import random

class Polje:
    def __init__(self, vrstica, stolpec):
        self.vrstica = vrstica
        self.stolpec = stolpec
        self.vrednost = 0
        self.zastavica = False

    def __repr__(self):
        return 'Polje(vrstica={}, stolpec={}, vrednost={})'.format(
            self.vrstica, self.stolpec, self.vrednost)

    def postavi_zastavico(self):
        self.zastavica = not self.zastavica
        return print(IGRA)

    def odkrij_polje(self):
        igra = IGRA
        if self in igra.seznam_odkritih:
            return 
        elif self.vrednost < 0:
            igra.seznam_odkritih.append(self)
            print(igra)
            print('Zadel si mino')
        elif self.vrednost > 0:
            igra.seznam_odkritih.append(self)
            print('Naslednja poteza')
        elif self.vrednost == 0:
            igra.seznam_odkritih.append(self)
            self.odkrij_sosednja()
        if len(igra.seznam_odkritih) + igra.st_min == igra.st_vrstic * igra.st_stolpcev:
            print('Zmaga!')
            
    
    def odkrij_sosednja(self):
        igra = IGRA
        for x in range(self.vrstica - 1, self.vrstica + 2):
            for y in range(self.stolpec - 1, self.stolpec + 2):   
                    if 0 <= x < igra.st_vrstic and 0 <= y < igra.st_stolpcev:
                        sosednje_polje = igra.seznam_polj[x][y]
                        if sosednje_polje not in igra.seznam_odkritih:
                            sosednje_polje.odkrij_polje()
        return igra.seznam_odkritih



class Igra:
    def __init__(self, st_vrstic, st_stolpcev, st_min):
        self.st_vrstic = st_vrstic
        self.st_stolpcev = st_stolpcev
        self.st_min = st_min
        self.seznam_polj = []
        self.seznam_odkritih = []
        for i in range(self.st_vrstic):
            self.seznam_polj_v_vrstici = []     
            for j in range(self.st_stolpcev):
                Polje(i, j)
                self.seznam_polj_v_vrstici.append(Polje(i, j))     
            self.seznam_polj.append(self.seznam_polj_v_vrstici)   

    def __repr__(self):
        return str(self.seznam_polj)

    def __str__(self):
        niz = ' ' + self.st_stolpcev * '-' + '\n'
        for x in range(self.st_vrstic):
            niz += '|'
            for y in range(self.st_stolpcev):
                polje = self.seznam_polj[x][y]
                if polje.zastavica:
                    niz += '#'
                elif polje not in self.seznam_odkritih:
                    niz += ' '
                else:
                    if polje.vrednost < 0:
                        niz += '*'
                    elif polje.vrednost >= 0:
                        niz += '{}'.format(polje.vrednost)     
            niz += '| \n'
        niz += ' ' + self.st_stolpcev * '-'
        return niz
    
    def postavi_mine(self):
        self.seznam_min = []
        for i in range(self.st_min):
            while True:
                polje = random.choice(random.choice(self.seznam_polj))
                if polje not in self.seznam_min:
                    polje.vrednost = -10
                    self.seznam_min.append(polje)
                    break
        return self.seznam_polj

    def doloci_vrednosti(self):
        for polje in self.seznam_min:
                for x in range(polje.vrstica -1, polje.vrstica + 2):
                    for y in range(polje.stolpec - 1, polje.stolpec + 2):
                        if 0 <= x < self.st_vrstic and 0 <= y < self.st_stolpcev:
                            sosednje_polje = self.seznam_polj[x][y]
                            sosednje_polje.vrednost += 1
        return self.seznam_polj

                
        
        
IGRA = Igra(10,10,10)
IGRA.postavi_mine()
IGRA.doloci_vrednosti()
IGRA.seznam_polj[1][1].odkrij_polje()




print(IGRA)

        
