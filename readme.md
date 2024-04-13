# Python Web Scraper pro Volební Data

## Popis
Tento Python skript je nástrojem pro extrakci dat z webových stránek obsahujících informace o volebních okrscích. Skript načte stránku, extrahuje potřebné informace a ukládá je do CSV souboru. Tento projekt je užitečný pro automatizaci sběru volebních dat bez manuálního kopírování.

## Funkcionalita
Skript provádí následující úkoly:
- Načítání specifikované webové stránky.
- Extrahování dat z tabulek na stránce.
- Filtrace a zpracování dat podle potřeby.
- Ukládání výsledků do souboru CSV.

## Technologie
Projekt je napsán v Pythonu a využívá knihovny:
- `BeautifulSoup4` pro parsování HTML.
- `requests` pro získání obsahu webu.
- `csv` pro práci s CSV soubory.
- `os` a `sys` pro manipulaci se soubory a systémové volání.

## Instalace
Pro spuštění skriptu je potřeba mít nainstalovaný Python a následující knihovny:
```bash
pip install beautifulsoup4
pip install request
```
## Spuštěni aplikace
Skript se spouští s přikazového řádku viz příklad:
```bash
python main.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' 'vysledky_voleb.csv'
```
První argument -
Druhý argument - 
## Běh aplikace
##