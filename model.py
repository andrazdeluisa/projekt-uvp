import random

class Polje:
    def __init__(self, vrstica, stolpec):
        self.vrstica = vrstica
        self.stolpec = stolpec
        self.vrednost = 0

    def __repr__(self):
        return 'Polje(vrstica={}, stolpec={}, vrednost={})'.format(
            self.vrstica, self.stolpec, self.vrednost)



class Igra:
    def __init__(self, st_vrstic, st_stolpcev, st_min):
        self.st_vrstic = st_vrstic
        self.st_stolpcev = st_stolpcev
        self.st_min = st_min
        self.seznam_polj = []
        for i in range(self.st_vrstic):
            self.seznam_polj_v_vrstici = []     
            for j in range(self.st_stolpcev):
                Polje(i, j)
                self.seznam_polj_v_vrstici.append(Polje(i, j))     
            self.seznam_polj.append(self.seznam_polj_v_vrstici)   

    def __repr__(self):
        return str(self.seznam_polj)

    def __str__(self):
        niz = ''
        for x in range(self.st_vrstic):
            for y in range(self.st_stolpcev):
                polje = self.seznam_polj[x][y]
                if polje.vrednost < 0:
                    niz += '*'
                else:
                    niz += '{}'.format(polje.vrednost)
            niz += '\n'
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
            
        
        
igra = Igra(10,10,10)
igra.postavi_mine()
igra.doloci_vrednosti()
print(igra)

        
