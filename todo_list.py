#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Pozdravljeni v TODO programu"

todo_list = {}

while True:
    task = raw_input("Vnesi novo opravilo: ")
    print "Tvoje novo opravilo je " + task
    finished = raw_input("Ali je opravilo končano (da/ne): ")

    todo_list[task] = finished

    new = raw_input("ali želiš nadaljevati (da/ne): ")
    if new == "ne":
        break

print "Končana opravila"
for k, v in todo_list.iteritems():
    if v == "da":
        print k

print "Nedokončana opravila"
for key, value in todo_list.iteritems():
    if value == "ne":
        print k

todo_file = open("./txt/todo.txt", "w+") # "w+" odpri za pisanje
todo_file.write("Končana opravila\n")
for k, v in todo_list.iteritems():
    if v == "da":
        todo_file.write("- " + k + "\n")

todo_file.write("\nNedokončana opravila\n")
for key, value in todo_list.iteritems():
    if value == "ne":
        todo_file.write("- " + k + "\n")

todo_file.close()