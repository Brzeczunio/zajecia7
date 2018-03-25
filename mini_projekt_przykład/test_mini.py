#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

valid_name = 'Jan'
valid_surname = 'Kowalski'
valid_number = '512512345'
valid_email = 'Adam'
valid_password = '123qweASD'
valid_country = "Polska"

class wizzairRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl/")

    # Dodane xpath są kopiowane z chrome co jest złym rozwiązaniem, bo one są bardzo sztywne. Lepiej pisać swoje z ręki
    def test_registration_invalid_email(self):
        login = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/header/div[1]/div/nav/ul/li[7]/button')))
        login.click()
        registration = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="login-modal"]/form/div/p/button')))
        registration.click()
        name = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Imię']")))
        name.send_keys(valid_name)
        surname = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Nazwisko']")))
        surname.send_keys(valid_surname)
        gender = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'register-gender-male')))
        # Klikanie w element na chama
        # self.driver.execute_script("arguments[0].click()", gender)
        gender.click()
        number = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Telefon komórkowy']")))
        number.send_keys(valid_number)
        email = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@data-test='booking-register-email']")))
        email.send_keys(valid_email)
        password = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@data-test='booking-register-password']")))
        password.send_keys(valid_password)
# Nie działa :(
         = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@class='register-form__country-container__locations']/label[164]")))
        # Wyświetlenie listy
        # self.driver.execute_script("arguments[0].scrollIntoView()", country);
        # country.location_once_scrolled_into_view
        # sleep(8)
        # country.click()
        # Inna metoda na Kraj z wpisanie z klawiatury kraju
        # country = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@data-test='booking-register-country']")))
        # country.send_keys(valid_country)
        special_offers = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//label[@for='registration-special-offers-checkbox']")))
        special_offers.click()
        privacy_policy = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//label[@for='registration-privacy-policy-checkbox']")))
        privacy_policy.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
