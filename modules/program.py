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
    def run(self):
        print "I run: " + self.type

# Tworzenie klasy dziedziczacej po Human
class Child(Human):
    def __init__(self, type = 'Child'):
        self.type = type
        print self.type

print(m.variable)

m.write()

# Stworzenie instancji (obiektu) klasy
h = Human()
h.run()

print u'Tworzenie klasy dziedziczącej'

c = Child()
Human.run(c)
