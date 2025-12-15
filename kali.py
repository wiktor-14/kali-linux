import json
import time
import random
import os
import sys
from datetime import datetime

#\033[31m  – czerwony
#\033[32m  – zielony
#\033[33m  – żółty
#\033[34m  – niebieski
#\033[35m  – fioletowy
#\033[36m  – cyjan
#\033[37m  – biały
#\033[0m   – reset

frames = [
    "[]                  ",
    "[][]                ",
    "[][][]              ",
    "[][][][]            ",
    "[][][][][]          ",
    "[][][][][][]        ",
    "[][][][][][][]      ",
    "[][][][][][][][]    ",
    "[][][][][][][][][]  ",
    "[][][][][][][][][][]",
    "[][][][][][][][][][][]",
    "[][][][][][][][][][][][]",
    "[][][][][][][][][][][][][]"
]

odpalanie = 0

logo = r"""
          ______________
     ,===:'.,            `-._
          :.---.__         `-._
            `:.     `--.         `.
              \.        `.         `.
      (,,(,    \.         .   ____,-.,
   (,'     /   \.   ,--.___.'
 ,  ,'  ,--.  `,   \.;'
 `{D, {    \  :    \;
   V,,'    /  /    //
   j;;    /  ,' ,-//.    ,---.      ,
   \;'   /  ,' /  _  \  /  _  \   ,'/
        \   `'  / \  `'  / \  `.' /
         `.,'   `.,'   `._,' 
"""

print("\033[36m", logo, "\033[0m")

while odpalanie < 13:
    for f in frames:
        print("\r" + f, end="")
        time.sleep(random.randint(1, 3))
        odpalanie += 1

print("\nładowanie ukończone linux odpalony")

cmd = {
    "nmap": " ",
    "help": "dostępne komendy to nmap, clear, ping, hack, echo, whoami, scan, ipconfig,  exit",
    "exit": "pa pa",
    "clear": " ",
    "ping": " ",
    "ls": " ",
    "XXX": "o odryłeś esteregga ale i tak po nic ci to",
    "hack": " ",
    "echo": " ",
    "date": " ",
    "whoami": " ",
    "ipconfig": "975.89.775.09",
    "scan": " ",
    "install": " ",
    "kankulator": " ",
    "zmiana_nazwy_użytkownika": " ",
    "zmiana_użądzenia": " "
}

foldery = {
    "zdjęcia": {},
    "dokumenty": {},
    "pobrane": {}
}

curent_folder = "~"

def kankulator():
    try:
        liczba1 = int(input("podaj 1 liczbę "))
        liczba2 = int(input("podaj 2 liczbę "))
        zala = input("podaj działanie ")

        if zala == "+":
            print("\n", liczba1 + liczba2)
        elif zala == "-":
            print("\n", liczba1 - liczba2)
        elif zala == "*":
            print("\n", liczba1 * liczba2)
        elif zala == "/":
            print("\n", liczba1 / liczba2)
        else:
            print("nie ma takiej komendy")
    except:
        print("tak nie można")

if os.path.exists("coś.json"):
    with open("coś.json", "r") as f:
        dane = json.load(f)
    b = dane["user"]
    c = dane["urządzenie"]
    haslo = dane["haslo"]
else:
    b = input("nazwa użytkownika ")
    c = input("użądzenie ")
    haslo = input("podaj nowe hasło ")
    dane = {"user": b, "urządzenie": c, "haslo": haslo}
    with open("coś.json", "w") as f:
        json.dump(dane, f, indent=4)

with open("coś.json", "r") as f:
    dane = json.load(f)

próby = 5

while True:
    logowanie = input("podaj hasło do logowania ")
    if logowanie == dane["haslo"]:
      print("zalogowano pomyślnie")
      break
    else:
        print("\033[31mzłe hasło")
        próby -= 1
        print("zostały ci", próby, "próby\033[0m")
        if próby == 0:
            print("\033[31mza dużo prób spróbuj ponownie później\033[0m")
            exit()

while True:
    a = input(f"{b}@{c}: {curent_folder}$ ")
    a = a.lower()

    if a in cmd:
        print(cmd[a])

        if a == "exit":
            break

        elif a == "clear":
            print("\n" * 1000)

        elif a == "ping":
            input("podaj adres ")
            print("sprawdzanie...")
            time.sleep(3)
            print("sprawdzone")
            time.sleep(0.5)
            print("żart")

        elif a == "nmap":
            input("podaj adres ")
            print("mapowanie...")
            time.sleep(3)
            print("mapowanie zakończone pomyślnie")
            time.sleep(0.5)
            print("żart")

        elif a == "ls":
            print(" ".join(foldery.keys()))

        elif a.startswith("cd"):
            parts = a.split()
            if len(parts) == 1:
                curent_folder = "~"
            else:
                folder = parts[1]
                if folder in foldery:
                    curent_folder = folder
                else:
                    print("nie ma takiego folderu")

        elif a == "hack":
            sto = input("podaj adres żeby zhakować ")
            if sto == "ster":
                print("esteregg")

            z = 0
            while z < 501:
                print(
                    "\033[32m",
                    random.randint(0, 9),
                    random.randint(0, 9),
                    random.randint(0, 9),
                    random.randint(0, 9),
                    random.randint(0, 9),
                    random.randint(0, 9),
                    random.randint(0, 9),
                    random.randint(0, 9),
                    random.randint(0, 9),
                    random.randint(0, 9),
                    "\033[0m"
                )
                z += 1
                time.sleep(0.01)

            print("zhakowano")

        elif a == "echo":
            echo = input(f"{b}@{c}: {curent_folder}$ echo ")
            print(echo)

        elif a == "date":
            print(datetime.now())

        elif a == "whoami":
            print(b)

        elif a == "scan":
            input("podaj ip ")
            time.sleep(2)
            print("port", random.randint(10, 99), "open")
            print("port", random.randint(10, 99), "open")
            print("port", random.randint(100, 999), "closed")
            print("port", random.randint(1000, 9999), "filtred")

        elif a == "install":
            instal1 = 0
            install = input("powiedz jaki pakiet zainstalować ")

            installanimation = [
                "[]                  ",
                "[][]                ",
                "[][][]              ",
                "[][][][]            ",
                "[][][][][]          ",
                "[][][][][][]        ",
                "[][][][][][][]      ",
                "[][][][][][][][]    ",
                "[][][][][][][][][]  ",
                "[][][][][][][][][][]",
            ]

            while instal1 < 10:
                for f in installanimation:
                    print("\r" + f, end="")
                    time.sleep(2)
                    instal1 += 1

            print(f"\n instalowanie {install} zakończone")

        elif a == "kankulator":
            kankulator()
    if a == "zmiana_nazwy_użytkownika":
        with open("coś.json", "r") as f:
            dane = json.load(f)
        dane["user"] = input("podaj nową nazwę użytkownika ")
        with open("coś.json", "w") as f:
            json.dump(dane, f, indent=4)
    if a == "zmiana_użądzenia":
        with open("coś.json", "r") as f:
            dane = json.load(f)
        dane["urządzenie"] = input("podaj nowe użądzenie ")
        with open("coś.json", "w") as f:
            json.dump(dane, f, indent=4)