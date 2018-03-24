# ZAJĘCIA 7

karol.kolanski@wsb.wroclaw.pl

### Prezentacje publiczne oraz assertywność
```
1. Różne pozycje otwarta, zamknięta itd. podczas prezentacji
2. Jak dobrze prezentować
3. Cechy dobrego testera
4. Własna prezentacja
```


### Testowanie aplikacji internetowych z wykorzystaniem Selenium Webdriver
```
pip - służy do instalacji pakietów [pythona]
"PIP = PYTHON INSTALLS PYTHON"

1. Sprawdzenie czy jest pip:
  a) su - //zmiana użytkownika na root (bez zapisów plików - przełącznik "-")

  b) yum -y update //instalacja aktualizacji

  c) yum -y install python-pip //instalacja python-pip

  d) pip install --upgrade pip //aktualizacja pip

2. Instalacja selenium

  a) pip install -U selenium //instalacja selenium z aktualizacja

  b) pip freeze//sprawdzenie zainstalowanych paczek

3. Instalacja stabilnego chrome i usunięcie niestabilnego

  a) yum remove google-chrome google-chrome-unstable //usuniecie chrome-unstable

  b) yum install google-chrome-stable //instalacja stabilnego chrome

4. Ściągnięcie chromedriver

  a) google.pl -> chromedriver
  (https://chromedriver.storage.googleapis.com/index.html?path=2.37/)//instalacja chromedriver

  b) unzip chromedriver_linux64.zip //wypakowanie chromedriver

  c) mv chromedriver /usr/local/bin/ //przenosimy plik do bin (wcześniej przęłączyć się na root i przejść do ścieżki /home/tester/Probrane/)
```
