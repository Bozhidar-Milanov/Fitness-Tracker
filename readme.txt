====================================================
  FITNESS TRACKER — Python Project
====================================================

OPISANIE:
---------
Tova e konzolen fitness tracker, koito pozvolqva na
potrebitelq da zapisva sportni aktivnosti, da gi
sortiira po kalorii, da gi filtriira po vid i da
viji obshotena statistika.

STRUKTURA NA PROEKTA:
---------------------
  models.py        — Sdrjha klasa FitnessTracker s metodite
  main.py          — Stvoryava obekt i demonstrira funktsionalnostta
  requirements.txt — Izpolzvani biblioteki
  readme.txt       — Tazi instruktsiq

KLАС FitnessTracker (models.py):
---------------------------------
  __init__(potrebitel)
      Inicializira trakera s ime na potrebitel i prazen
      spisak s aktivnosti.

  dobavi_aktivnost(vid, minuti, kalorii)
      Dobavya nova aktivnost s tekushta data, vid,
      prodaljitelnost v minuti i izgoryani kalorii.

  pokaji_vsichki()
      Pokazva vsichki zapisani aktivnosti v tablichen vid.

  sortiraj_po_kalorii(nizhodyashto=True)
      Sortira aktivnostite po izgoryani kalorii.
      Po podrazbirana naredba e nizhodyashta (naj-visoki napred).
      Podaj nizhodyashto=False za vazhodyashto naredjane.

  filtriraj_po_vid(vid)
      Vrashta i pokazva samo aktivnostite ot dadenia vid
      (npr. "Byagane", "Kolelo", "Yoga").

  oboshtenie()
      Pressmqta i pokazva obshto minuti, obshto kalorii,
      srednite kalorii na sesiq i dava preporaka.

IZPOLZVANI BIBLIOTEKI:
-----------------------
  tabulate — za krasivo formatirana tablitsa v terminala
             (https://pypi.org/project/tabulate/)

KAK DA STАРТИРАТЕ:
------------------
  1. Инсталирайте зависимостите:
       pip install -r requirements.txt

  2. Стартирайте програмата:
       python main.py

IZISKVANA VERSIQ NA PYTHON:
----------------------------
  Python 3.8 ili po-nova versiq

====================================================
