#!/usr/bin/env python
# -*- coding: utf-8 -*-

oseba = {
    "ime": "Janez",
    "priimek": "Novak"
}

print oseba["ime"]
print oseba["priimek"]

print oseba

for key, value in oseba.iteritems():
    print key
    print value
    print "---------"
    print oseba[key]

mesta = {
    1000: "Ljubljana",
    2000: "Maribor",
    4000: "Kranj"

}

mesta[6000] = "Koper"

for k, v in mesta.iteritems():
    print "mesto " + mesta[k] + " ima poštno številko " + str(k)