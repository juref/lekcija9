#!/usr/bin/env python
# -*- coding: utf-8 -*-

class hairColor:
    black = "CCAGCAATCGC"
    brown = "GCCAGTGCCG"
    blonde = "TTAGCTATCGC"

class facialShape:
    square = "GCCACGG"
    round = "ACCACAA"
    oval = "AGGCCTCA"

class eyeColor:
    blue = "TTGTGGTGGC"
    green = "GGGAGGTGGC"
    brown = "AAGTAGTGAC"

class gender:
    female = "TGAAGGACCTTC"
    male = "TGCAGGAACTTC"

class race:
    white = "AAAACCTCA"
    black = "CGACTACAG"
    asian = "CGCGGGCCG"

eva = {
    "gener": gender.female,
    "race": race.white,
    "hair": hairColor.blonde,
    "eye": eyeColor.blue,
    "face": facialShape.oval
}

larisa = {
    "gener": gender.female,
    "race": race.white,
    "hair": hairColor.brown,
    "eye": eyeColor.brown,
    "face": facialShape.oval
}

matej = {
    "gener": gender.male,
    "race": race.white,
    "hair": hairColor.black,
    "eye": eyeColor.blue,
    "face": facialShape.oval
}

miha = {
    "gener": gender.male,
    "race": race.white,
    "hair": hairColor.brown,
    "eye": eyeColor.green,
    "face": facialShape.square
}

# suspects = [eva, larisa, matej, miha]                  # probal z listo, pa nikakor ne morem izpisati imena, ker mi izpisuje vrednosti za ime!
suspects = {                                             # slovar slovarjev :)
    "Eva": eva,
    "Larisa": larisa,
    "Matej": matej,
    "Miha": miha
}

print "\nOseba, ki ti je pojedla sladoled ima spodnji DNA zapis: \n"
dna_file = open("dna.txt", "r")
dna = dna_file.read()
dna_file.close()

print dna + "\n"

for name, name_list in suspects.iteritems():             # gre čez vsa imena in izpostavi vrednosti (vrednost slovarja)
    perpetrator = ""                                     # pripravi prazni variable za storilca
    for car, val in name_list.iteritems():               # gre čez vse car - karakteristike oz. čez slovar v slovarju
        if val in dna:                                   # če se ujema zapiše ime v variable
            perpetrator = name
        else:
            perpetrator = ""                             # če se ne ujema resetira variable
    if perpetrator:                                      # če se ujemajo vsi pogoji ima ima ergo ni prazen zato zaključi iskanje
        perpetrator != ""
        break

print "Storilec je %s!" % perpetrator

