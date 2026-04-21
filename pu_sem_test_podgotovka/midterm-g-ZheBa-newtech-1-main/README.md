[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/aLJY-hx9)
# Půlsemestrální test 2025/2026 - varianta G


### Klonování a nastavení repozitáře v PyCharmu
1. V PyCharmu vyber možnost <kbd>Pycharm</kbd> → <kbd>Open...</kbd>.
    
    Ve vyskakovacím okně nastav cestu na vytvořenou složku pro půlsemestrální test:

    `C:\Users\xxxxxx\Desktop\prg_midterm`
    
    → <kbd>Select Folder</kbd> → <kbd>This Window</kbd> → <kbd>Trust Project</kbd>
2. Otevři Terminál (<kbd>Alt</kbd> + <kbd>F12</kbd>).
3. V příkazové řádce přejdi do této složky:
    ```commandline
    cd C:\Users\xxxxxx\Desktop\prg_midterm
    ```
4. Naklonuj repozitář s testem:
    ```commandline
    git clone https://path.to.git.repository
    ```
5. V PyCharmu otevři naklonovaný repozitář:

    <kbd>Pycharm</kbd> → <kbd>File</kbd> → <kbd>Open...</kbd>

    Ve vyskakovacím okně nastav cestu na hlavní adresář s půlsemestrálním testem: 

    `C:\Users\xxxxxx\Desktop\prg_midterm\midterm-test-xxx`

    → <kbd>Select Folder</kbd> → <kbd>This Window</kbd> → <kbd>Trust Project</kbd>
6. Vytvoř virtuální prostředí přes Terminál:
    ```commandline
    uv sync
    ```

---

# Analýza růstu buněk

Pochopení dynamiky růstu buněčných kultur je klíčové v biotechnologiích a medicíně. Analýza růstových fází umožňuje optimalizovat podmínky pro produkci biologických látek a předvídat chování buněčných systémů.

Cílem je vytvořit program v souboru `cell_growth.py`, který analyzuje růst buněčné kultury podle měření počtu buněk v čase.

Program má:
- načíst data ze souboru,
- spočítat rychlost růstu mezi měřeními,
- určit růstové fáze,
- najít interval s nejrychlejším růstem,
- vypsat výsledky.

Používané fáze růstu:
- lag - pomalý růst (adaptace)
- log - rychlý růst
- stationary - téměř žádný růst

---

## Vstupní data (CSV)

Soubor může obsahovat metadata, ale pro výpočet se používají pouze sloupce `time_hours` a `cell_count`.

Příklad struktury CSV:
- Hlavička obsahuje minimálně názvy sloupců `time_hours` a `cell_count`.
- Sloupce mohou být doplněny o metadata (např. `experiment_id`, `strain`, `temperature_c`).
- Sloupce mohou být i v jiném pořadí.

Příklad řádků dat:
- čas 0 hodin, počet buněk 100
- čas 2 hodina, počet buněk 120
- čas 3 hodiny, počet buněk 160
- čas 4 hodiny, počet buněk 210
- čas 6 hodiny, počet buněk 240

---

## Úkol 1: Výpočet rychlosti růstu

Implementuj funkci `get_growth_rates()`, která vypočítá rychlost růstu mezi po sobě jdoucími měřeními.
Kladná rychlost znamená růst, záporná pokles, a nulová rychlost znamená stabilní počet buněk.

### Popis

Funkce přijme seznam časových bodů a odpovídající seznam počtů buněk. Pro každou dvojici sousedních měření vypočítá rychlost změny počtu buněk za čas.

Vzorec: $$rychlost = \frac{{pocet\\_bunek\\_nasledujici} - pocet\\_bunek\\_aktualni}{cas\\_nasledujici - cas\\_aktualni}$$

### Vstupy

- `times` - seznam časů měření v hodinách (list of float)
- `cell_counts` - seznam počtů buněk v odpovídajících časech (list of float), stejná délka jako seznam časů

### Výstup

- seznam rychlostí růstu (list of float), délka o 1 menší než délka vstupních seznamů

### Příklad

- Vstup: časy `[0.0, 2.0, 3.0, 4.0, 6.0]` a počty buněk `[100.0, 120.0, 160.0, 210.0, 240.0]`
- Výstup: rychlosti `[10.0, 40.0, 50.0, 15.0]`

---

## Úkol 2: Určení růstové fáze

Implementuj funkci `get_growth_phases()`, která přiřadí každé rychlosti růstu odpovídající fázi.

### Popis

Funkce přijme seznam rychlostí a pro každou z nich určí fázi růstu na základě porovnání s prahy. 
Prahy jsou volitelné parametry s výchozími hodnotami. Fáze jsou reprezentovány řetězci `'lag'`, `'log'` a `'stationary'`.

### Pravidla klasifikace

- rychlost menší než dolní práh → `'stationary'`
- rychlost větší než horní práh → `'log'`
- jinak (včetně přesné shody s prahy) → `'lag'`

### Vstupy

- `growth_rates` - seznam rychlostí růstu (list of float)
- `low_threshold` - dolní práh, výchozí hodnota `20.0` (float)
- `high_threshold` - horní práh, výchozí hodnota `80.0` (float)

### Výstup

- seznam fází růstu (list of str), stejná délka jako seznam rychlostí

### Příklad

- Vstup: rychlosti `[10.0, 40.0, 110.0, 5.0]`
- Výstup: fáze `['stationary', 'lag', 'log', 'stationary']`

---

## Úkol 3: Interval nejrychlejšího růstu

Implementuj funkci `get_peak_growth_interval()`, která najde interval s nejvyšší rychlostí růstu.

### Popis

Funkce přijme seznam časů a seznam rychlostí růstu. Určí, ve kterém intervalu nastala nejvyšší rychlost, 
a vrátí začátek a konec tohoto intervalu spolu s hodnotou rychlosti. Při shodě více maxim se vrátí první výskyt.

### Vstupy

- `times` - seznam časů měření v hodinách (list of float)
- `growth_rates` - seznam rychlostí růstu (list of float), délka o 1 menší než délka seznamu časů

### Výstup

- trojice `(start_time, end_time, peak_rate)`
  - `start_time` - čas začátku intervalu s nejvyšší rychlostí (float)
  - `end_time` - čas konce intervalu s nejvyšší rychlostí (float)
  - `peak_rate` - hodnota nejvyšší rychlosti růstu (float)

### Příklad

- Vstup: časy `[0, 1, 2, 3, 4]` a rychlosti `[10.0, 40.0, 110.0, 5.0]`
- Výstup: začátek `2.0`, konec `3.0`, rychlost `110.0`

---

## Úkol 4: Načtení dat ze souboru

Implementuj funkci `read_growth_data()`, která načte data z CSV souboru.

### Popis

Funkce otevře soubor, na základě názvů sloupců v hlavičce najde sloupce `time_hours` a `cell_count`, 
a načte jejich hodnoty do dvou oddělených seznamů. Ostatní sloupce ignoruje. Pořadí sloupců v souboru nesmí ovlivnit
chování funkce. Soubor může obsahovat libovolné další sloupce, které se ignorují.

### Vstupy

- `filename` - cesta k CSV souboru (str)

### Výstup

- dvojice `(times, cell_counts)`
  - `times` - seznam časů v hodinách (list of float)
  - `cell_counts` - seznam počtů buněk (list of float)

### Příklad

- Vstup: cesta k souboru `'data/cell_growth_0.csv'` s daty pro 5 měření
- Výstup: časy `[0.0, 1.0, 2.0, 3.0, 4.0]`, počty buněk `[100.0, 110.0, 150.0, 260.0, 265.0]`

---

## Úkol 5: Hlavní funkce

Implementuj funkci `main()`, která propojí všechny předchozí funkce a vypíše výsledky analýzy.

### Popis

Funkce přijme cestu k CSV souboru, spustí celou analýzu a výsledky vypíše na standardní výstup. Nic nevrací.

### Vstup

- `filename` - cesta k CSV souboru (str)

### Výstup

Funkce nic nevrací. Na standardní výstup vypíše v tomto pořadí:

- seznam časů
- seznam počtu buněk
- seznam rychlostí růstu
- seznam fází růstu
- interval nejrychlejšího růstu (formát: X-Y h)
- hodnota nejvyšší rychlosti

### Příklad výpisu

```
Times: [0.0, 1.0, 2.0, 3.0, 4.0]
Cell counts: [100.0, 110.0, 150.0, 260.0, 265.0]
Growth rates: [10.0, 40.0, 110.0, 5.0]
Growth phases: ['stationary', 'lag', 'log', 'stationary']
Peak growth interval: 2.0-3.0 h
Peak growth rate: 110.0
```

---

### Příkazy pro git
1. Přidat soubor:
   ```commandline
   git add cell_growth.py
   ```
2. Vytvořit commit:
   ```commandline
   git commit -m "Commit message"
   ```
3. Odeslat na GitHub:
   ```commandline
   git push origin main
   ```

### Příkazy pro pytest
* Instalace:
  ```commandline
  uv sync
  ```
* Spuštění všech testů:
  ```commandline
  uv run pytest -v
  ```
* Spuštění konkrétního souboru s testy:
  ```commandline
  uv run pytest tests/name_of_the_test_file.py
  ```
