#! /usr/bin/python
# -*- coding: utf-8 -*-

# Zaimportowanie niezbędnych bibliotek
from selenium import webdriver
import time

# Stwórz nowy sterownik do Chrome
driver = webdriver.Chrome()

# Maksymalizuj okno
driver.maximize_window()
driver.get("http://www.wsb.pl")
# Poczekaj 5 sekund, by nacieszyć oczy. BARDZO ZŁA METODA
time.sleep(5)
# Zamknij sterownik
driver.quit()
