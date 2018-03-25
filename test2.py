#! /usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
from time import sleep

class WsbSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get('http://www.wsb.pl/chorzow')
        driver.maximize_window()

    def test_link(self):
        cookie = self.driver.find_element_by_link_text(u'AKCEPTUJĘ')
        cookie.click()
        sleep(3)
        link = self.driver.find_element_by_link_text('Studia I stopnia')
        link.click()
        sleep(3)

    def test_wsb_search_box(self):
        search = self.driver.find_element_by_id('edit-search-block-form--2')
        search.send_keys('fraza')
        search_button = self.driver.find_element_by_id('edit-submit')
        search_button.click()
        sleep(5)
        h2 = self.driver.find_element_by_xpath("//div[@class='content']/h2")
        self.assertIn(u'Nie znaleziono żadnych dokumentów zawierających podane słowo.', h2.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
