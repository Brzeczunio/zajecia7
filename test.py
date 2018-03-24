#! /usr/bin/python
# -*- coding: utf-8 -*-

# Zaimportowanie niezbędnych bibliotek
from selenium import webdriver
import unittest

# Tworzenie klasy WsbPlCheck dziedziczącej po klasie TestCase z modułu unittest
class WsbPlCheck(unittest.TestCase):
    # Instrukcje, które zostają wykonane przed każdym testem
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_login(self):
        driver = self.driver
        driver.get('http://www.wsb.pl')
        self.assertIn(u'Wyższe Szkoły Bankowe', driver.title)

    def test_login2(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        self.assertIn(u'Uczelnie wyższe', driver.title)

    def test_login2(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        self.assertIn(u'Koczkodan', driver.title)

    # Instrukcje, które zostają wykonane po każdym teście
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
