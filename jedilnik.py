#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Pozdravljeni prosim vnesite današnji dnevni menu"

jedilnik = {}

while True:
    jed = raw_input("Prosim vnesite jed: ")
    cena = raw_input("Prosim vnesite ceno za " + jed + ": ")

    jedilnik[jed] = cena

    new = raw_input("ali želiš nadaljevati (da/ne): ")
    if new == "ne":
        break

todo_file = open("menu.txt", "w+") # "w+" odpri za pisanje
todo_file.write("Danes na menuju je: \n")
for k, v in jedilnik.iteritems():
        todo_file.write("jed: " + k + " cena: " + v + " EUR" + "\n")

todo_file.close()