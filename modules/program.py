#! /usr/bin/python
# -*- coding: utf-8 -*-

import my_module as m

# Klasa
class Human():

    # Konstruktor klasy
    def __init__(self, type = 'Human'):
        self.type = type
        print self.type

        # Funkcja klasy
    def Run():
        print "I run"

print(m.variable)

m.write()

# Stworzenie instancji (obiektu) klasy
h = Human()
