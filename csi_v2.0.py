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
    "face": facialShape.square
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
dna_file = open("./_txt/dna.txt", "r")
dna = dna_file.read()
dna_file.close()

print dna + "\n"

for name, name_list in suspects.iteritems():             # gre čez vsa imena in izpostavi vrednosti (vrednost slovarja)
    print "\ntesting " + name + " for DNA match:"
    perpetrator = ""                                     # pripravi prazni variable za storilca
    for car, val in name_list.iteritems():               # gre čez vse car - karakteristike oz. čez slovar v slovarju
        if val in dna:                                   # če se ujema zapiše ime v variable
            print car + " (" + val + ")" + " = match"
            perpetrator = name
        else:
            print car + " (" + val + ")" + " = NO match"
            perpetrator = ""                             # če se ne ujema resetira variable
            break                                        # Zelo pomemben breake!!! Če tu ni breake, vrne za storilca Mateja, ker ima zadnji parameter, ki se ujema z DNA in zato vpiše ime v varable. S tem breakeom nehamo testirati ob prvem neskladju!
    if perpetrator:                                      # če se ujemajo vsi pogoji ima ima ergo ni prazen zato zaključi iskanje
        print "\nPrekini test. Storilec je znan! Vsi DNA parametri se ujemajo!"
        perpetrator != ""
        break

print "\nStorilec je %s!" % perpetrator

