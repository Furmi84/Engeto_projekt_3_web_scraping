from bs4 import BeautifulSoup
import requests
import csv
import os
import sys


def vymazani_obrazovky():
    """
        Vymaže přikazovy řádek

        """
    if os.name == 'nt':
        os.system('cls')
    else:  # Posix (Linux, OS X, ...)
        os.system('clear')


def stav_procesu(ukazatel):
    global progress_bar  # Referencování globální proměnné

    vymazani_obrazovky()  # Mazání obrazovky pro každé volání
    if ukazatel == 0:
        progress_bar = "Pracuji "  # Resetování pokud je to začátek procesu
    elif ukazatel % 4 == 2:
        progress_bar += "."  # Přidání tečky pro každý čtvrtý krok

    print(progress_bar)  # Tisk aktuálního stavu


def nacti_stranku(url):
    """
    Načte webovou stránku z dané URL adresy a vrátí její obsah ve formě objektu BeautifulSoup.

    Argumenty:
        url (str): Adresa URL webové stránky.

    Návratové hodnota:
        BeautifulSoup: Objekt BeautifulSoup obsahující zpracovaný obsah webové stránky.
    """
    response = requests.get(url)
    web = response.text
    soup = BeautifulSoup(web, "html.parser")
    return soup


def zpracuj_radek_a_filtruj(radek_textu, vybrane_indexy, nezadouci):
    """
    Zpracuje řádek textu podle zadaných kritérií a vrátí filtrovaný seznam.

    Argumenty:
        radek_textu (str): Řádek textu k zpracování.
        vybrane_indexy (list): Seznam indexů položek, které se mají zachovat.
        nezadouci (list): Seznam výrazů, které mají být odstraněny.

    Návratové hodnoty:
        list: Filtrovaný seznam položek.
    """
    radek_textu = radek_textu.replace(u'\xa0', ' ')
    text = radek_textu.split("\n")
    return [item for i, item in enumerate(text)
            if i in vybrane_indexy and item not in nezadouci]


def ziskej_seznam_okrsku(url):
    """
    Získá seznam okrsků z dané URL adresy.

    Argumenty:
        url (str): Adresa URL stránky s výpisem okrsků.

    Návratové hodnoty:
        zip: Zipový objekt obsahující seznam kódů obcí, názvů obcí a odkazů na stránky okrsků.
    """
    hledane_znaky_url = "nss/"
    dl = len(hledane_znaky_url)
    idx = url.index(hledane_znaky_url)
    prefix_url = url[:idx+dl]
    web = nacti_stranku(url)

    jmena_obci, kod_obci, odkazy = [], [], []

    tabulky = web.find_all("table")
    for tabulka in tabulky:
        for index, radek in enumerate(tabulka.find_all("tr")):
            if index > 1:
                odkaz_el = radek.find("a")
                if odkaz_el:
                    odkaz = prefix_url + odkaz_el["href"]
                    kod, jmeno = zpracuj_radek_a_filtruj(radek.getText(" "), [1, 2],
                        [' Obec ', ' číslo ',
                            ' Výběr okrsku ', ' název '])
                    jmena_obci.append(jmeno)
                    kod_obci.append(kod)
                    odkazy.append(odkaz)
    return zip(kod_obci, jmena_obci, odkazy)


def ziskej_data_ze_stranky(kod, nazev_obce, adresa):
    """
    Získá data ze stránky okrsku na dané adrese.

    Argumenty:
        kod (str): Kód obce.
        nazev_obce (str): Název obce.
        adresa (str): Adresa URL stránky s informacemi o okrsku.

    Návratové hodnoty:
        tuple: Tuple obsahující seznam stran a seznam hodnot ze stránky okrsku.
    """

    zahlavi = ["kod", "nazev_obce"]
    hodnoty = [kod, nazev_obce]

    web = nacti_stranku(adresa)
    tabulky = web.find_all("table")

    akce = {
        0: {'indexy': [2, 5, 6], 'cil': zahlavi, 'nezadouci': []},
        2: {'indexy': [4, 7, 8], 'cil': hodnoty, 'nezadouci': []}
    }

    akce_ost = {
        'zahlavi': {'indexy': [2], 'cil': zahlavi, 'nezadouci': [" Platné hlasy ", " název ", " - "]},
        'hodnoty': {'indexy': [3], 'cil': hodnoty, 'nezadouci': [" Předn. hlasy ", " celkem ", " - "]},
    }

    for idx, radek in enumerate(tabulky[0].find_all('tr')):
        if idx in akce:
            info = akce[idx]
            vysledky = zpracuj_radek_a_filtruj(radek.getText(" "), info['indexy'], info['nezadouci'])
            info['cil'].extend(vysledky)

    for tabulka in tabulky[1:]:
        for radek in tabulka.find_all('tr'):
            vysl_z = zpracuj_radek_a_filtruj(radek.getText(" "), akce_ost['zahlavi']['indexy'],
                                             akce_ost['zahlavi']['nezadouci'])
            akce_ost['zahlavi']['cil'].extend(vysl_z)

            vysl_h = zpracuj_radek_a_filtruj(radek.getText(" "), akce_ost['hodnoty']['indexy'],
                                             akce_ost['hodnoty']['nezadouci'])
            akce_ost['hodnoty']['cil'].extend(vysl_h)

    return zahlavi, hodnoty


def main():

    adresa = sys.argv[1]
    nazev_souboru = sys.argv[2]
    progress_bar = "Pracuji"

    vymazani_obrazovky()

    with open(nazev_souboru, mode='w', newline='',
              encoding='utf-8') as soubor:
        writer = csv.writer(soubor, delimiter=",")
        for index, (kod, obec, odkaz) in enumerate(ziskej_seznam_okrsku(adresa)):
            header, hodnoty = ziskej_data_ze_stranky(
                kod, obec, odkaz)
            if index == 0:
                writer.writerow(header)

            writer.writerow(hodnoty)
            stav_procesu(index)

    print("Prace skoncena, soubor uložen se jmenem", nazev_souboru)


if __name__ == "__main__":
    main()
