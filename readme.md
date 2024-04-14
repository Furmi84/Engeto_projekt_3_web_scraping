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
```
pip install beautifulsoup4
pip install requests
```
## Spouštění aplikace
Pomoci příkazového řádku.
Příklad:
```
python main.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' 'vysledky_voleb.csv'
```

První argument - adresa ze kterého ma program načítat informace
Druhý argument - jméno souboru ve formatu csv

## Běh aplikace
Pokud aplikace běži správně, zobrazí se tato hlaška v terminálu:
```
Pracuji .........................
```
Po skončení aplikace se zobrazi informace o ukončeni a 
## Konec aplikace a výsledky
Po skončení aplikace se zobrazi hlaška o ukončení programu a jmenem souboru kde jsou uloženy výsledky.
Ukončení programu může vypadat takto:
```
Prace skoncena, soubor uložen se jmenem vysledky_voleb.csv

```
Úkazka výsledku:
```
kod;nazev_obce; Voliči v seznamu ; Odevzdané obálky ; Platné hlasy ; Občanská demokratická strana ; Řád národa - Vlastenecká unie ; CESTA ODPOVĚDNÉ SPOLEČNOSTI ; Česká str.sociálně demokrat. ; Radostné Česko ; STAROSTOVÉ A NEZÁVISLÍ ; Komunistická str.Čech a Moravy ; Strana zelených ; ROZUMNÍ-stop migraci,diktát.EU ; Strana svobodných občanů ; Blok proti islam.-Obran.domova ; Občanská demokratická aliance ; Česká pirátská strana ; Referendum o Evropské unii ; TOP 09 ; ANO 2011 ; Dobrá volba 2016 ; SPR-Republ.str.Čsl. M.Sládka ; Křesť.demokr.unie-Čs.str.lid. ; Česká strana národně sociální ; REALISTÉ ; SPORTOVCI ; Dělnic.str.sociální spravedl. ; Svob.a př.dem.-T.Okamura (SPD) ; Strana Práv Občanů 
 506761 ; Alojzov ; 205 ; 145 ; 144 ; 29 ; 0 ; 0 ; 9 ; 0 ; 5 ; 17 ; 4 ; 1 ; 1 ; 0 ; 0 ; 18 ; 0 ; 5 ; 32 ; 0 ; 0 ; 6 ; 0 ; 0 ; 1 ; 1 ; 15 ; 0 
 589268 ; Bedihošť ; 834 ; 527 ; 524 ; 51 ; 0 ; 0 ; 28 ; 1 ; 13 ; 123 ; 2 ; 2 ; 14 ; 1 ; 0 ; 34 ; 0 ; 6 ; 140 ; 0 ; 0 ; 26 ; 0 ; 0 ; 0 ; 0 ; 82 ; 1 
 
```