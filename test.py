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

    def test_Search(self):
        driver = self.driver
        driver.get('http://www.wsb.pl')
        search = driver.find_element_by_id('edit-search-block-form--2')
        search.send_keys('fraza')
        search.click()
        content = driver.find_element_by_class_name('content')
        # h2 = content.find_element_by_tag_name('h2')
        self.assertIn(u'Nie znaleziono żadnych dokumentów zawierających podane słowo.', h2.text)

    # Instrukcje, które zostają wykonane po każdym teście
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
