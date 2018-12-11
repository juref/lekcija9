#!/usr/bin/env python
# -*- coding: utf-8 -*-

ime1 = "Janez"
ime2 = "Marija"
x = 1
y = 2

seznam_imen = ["Janez 2", "Janez 3", "Janez 4"]
seznam_imen2 = [ime1, ime2, x, y]

for s in seznam_imen:
    print s

print "---------------"

for s in seznam_imen2:
    print s

print "---------------"

seznam_imen.append("Janez 5")
for s in seznam_imen:
    print s

print seznam_imen