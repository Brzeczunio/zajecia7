#! /usr/bin/python
# -*- coding: utf-8 -*-

# Zaimportowanie niezbędnych bibliotek
from selenium import webdriver
import unittest
from time import sleep

# Tworzenie klasy WsbPlCheck dziedziczącej po klasie TestCase z modułu unittest
class WsbPlCheck(unittest.TestCase):
    # Instrukcje, które zostają wykonane przed każdym testem
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get('http://www.wsb.pl')

    def test_Search(self):
        search = self.driver.find_element_by_id('edit-search-block-form--2')
        search.send_keys('fraza')
        search_button = self.driver.find_element_by_id('edit-submit')
        search_button.click()
        sleep(5)
        h2 = self.driver.find_element_by_xpath("//div[@class='content']/h2")
        self.assertIn(u'Nie znaleziono żadnych dokumentów zawierających podane słowo.', h2.text)

    # Instrukcje, które zostają wykonane po każdym teście
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
