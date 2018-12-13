#!/usr/bin/env python
# -*- coding: utf-8 -*-
week = ["ponedeljek", "torek", "sreda", "četrtek", "petek", "sobota", "nedelja"]

def menu(day):
    print "Pozdravljeni prosim vnesite dnevni menu za " + day + ":"
    jedilnik = {}
    while True:
        jed = raw_input("Prosim vnesite jed: ")
        cena = raw_input("Prosim vnesite ceno za " + jed + ": ")

        jedilnik[jed] = cena

        new = raw_input("ali želiš nadaljevati vnos za " +day + "(da/ne): ")
        if new == "ne":
            break

    todo_file = open("./_txt/" + day + ".txt", "w+") # "w+" odpri za pisanje
    todo_file.write("Danes je " + day + ". Na menuju je: \n")
    for k, v in jedilnik.iteritems():
            todo_file.write("jed: " + k + " cena: " + v + " EUR" + "\n")

    todo_file.close()

for day in week:
    menu(day)