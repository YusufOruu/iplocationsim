import time
import random
from colorama import init, Fore

init(autoreset=True)

countries = [
    ("Russia", "Moscow", "55.7558° N, 37.6173° E"),
    ("USA", "New York", "40.7128° N, 74.0060° W"),
    ("Turkey", "Istanbul", "41.0082° N, 28.9784° E"),
    ("Germany", "Berlin", "52.5200° N, 13.4050° E"),
    ("Japan", "Tokyo", "35.6895° N, 139.6917° E"),
    ("France", "Paris", "48.8566° N, 2.3522° E"),
    ("China", "Beijing", "39.9042° N, 116.4074° E"),
    ("Brazil", "Rio de Janeiro", "22.9068° S, 43.1729° W")
]

def hacker_style(text, delay=0.03):
    for char in text:
        print(Fore.GREEN + char, end='', flush=True)
        time.sleep(delay)
    print()

def kontrol_ediliyor(lang):
    dots = ["." * i for i in range(1, 4)] + ["." * i for i in range(2, 0, -1)]
    for dot in dots:
        if lang == "en":
            print(Fore.GREEN + "Checking IP" + dot)
        else:
            print(Fore.GREEN + "IP kontrol ediliyor" + dot)
        time.sleep(0.5)
        print("\033[F\033[K", end='')  # clear line

def simulatör():
    hacker_style("Select Language / Dil Seçin:", 0.02)
    print(Fore.GREEN + "1 - English")
    print(Fore.GREEN + "2 - Türkçe")
    lang_choice = input(Fore.GREEN + "> ")

    lang = "en" if lang_choice == "1" else "tr"

    if lang == "en":
        hacker_style("Enter the IP address you want to check:", 0.02)
    else:
        hacker_style("Sorgulamak istediğiniz IP adresini girin:", 0.02)

    ip = input(Fore.GREEN + "> ")

    kontrol_ediliyor(lang)

    if lang == "en":
        hacker_style("\nLocation Found!\n", 0.04)
    else:
        hacker_style("\nKonum bulundu!\n", 0.04)

    ulke, sehir, koordinat = random.choice(countries)

    if lang == "en":
        hacker_style(f"Country: {ulke}", 0.02)
        hacker_style(f"City: {sehir}", 0.02)
        hacker_style(f"Coordinates: {koordinat}", 0.02)
    else:
        hacker_style(f"Ülke: {ulke}", 0.02)
        hacker_style(f"Şehir: {sehir}", 0.02)
        hacker_style(f"Koordinatlar: {koordinat}", 0.02)

simulatör()