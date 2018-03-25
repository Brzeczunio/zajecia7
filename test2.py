#! /usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        submit = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,"edit-submit")))
        submit.click()
        h2 = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='content']/h2")))
        self.assertIn(u'Nie znaleziono żadnych dokumentów zawierających podane słowo.', h2.text)

    def test_wsb_search_box_submit(self):
        search = self.driver.find_element_by_id('edit-search-block-form--2')
        search.send_keys('fraza')
        search.submit()
        h2 = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='content']/h2")))
        self.assertIn(u'Nie znaleziono żadnych dokumentów zawierających podane słowo.', h2.text)

    def test_wsb_search_box_submit(self):
        search = self.driver.find_element_by_id('edit-search-block-form--2')
        search.send_keys('tester')
        search.submit()
        h2 = WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="block-system-main"]/div/ol/li')))
        assert 3 == len(h2)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
