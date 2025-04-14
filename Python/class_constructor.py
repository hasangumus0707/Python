# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 13:01:24 2025

@author: gumus
"""


class Calisan:

    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@gmail.com"
        
    def giveNameSurname(self):
        return self.isim +" "+self.soyisim


isci1 = Calisan("ali", "veli", 100)
print(isci1.giveNameSurname())

