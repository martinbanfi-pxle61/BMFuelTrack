# BMFuelTrack

**Hallgató**: Bánfi Martin Kevin PXLE61

**Feladat leírása**:  
Egy grafikus felületű alkalmazás, amelyben autós tankolásokat lehet rögzíteni, majd ezek alapján egyszerű statisztikát készíteni a fogyasztásról. A felhasználó megadja a tankolt üzemanyag mennyiségét (liter), az árat (Ft/liter) és a megtett távot (km). A program kiszámolja az adott tankolás fogyasztását (liter/100 km), a teljes költséget, eltárolja a tankolást egy listában, és összegző statisztikát készít az összes eddigi rekord alapján (átlag, medián, minimum, maximum, szórás).  
A program grafikus felületet használ `tkinter`-rel, eseménykezelést gombokkal, valamint saját modullal és saját osztállyal valósítja meg a logikát.

## Modulok és függvények

- **math** (tanult + bemutatandó modul): számítások és kerekítések
  - `ceil(x)`: Felfelé kerekítés (átlag fogyasztás egy tizedesre kerekítése)
  - `floor(x)`: Lefelé kerekítés (minimum és maximum fogyasztás egészre kerekítése)
  - `sqrt(x)`: Négyzetgyök (szórás számításánál)

- **random** (tanult modul): véletlen azonosító generálása a tankolásokhoz
  - `randint(a, b)`: Véletlen egész szám generálása a megadott intervallumból

- **tkinter**: grafikus felület és eseménykezelés
  - `Tk`: Alapablak létrehozása (`root`)
  - `Label`, `Entry`: Szövegek és beviteli mezők (liter, ár, km)
  - `Button`: Gombok (hozzáadás, összegzés, mezők törlése, kiválasztott törlése)
  - `Listbox`: A felvitt tankolások listázása
  - `END`: Listbox végére beszúrás
  - `messagebox`: Hiba- és információs ablakok

- **bm_tankolas** (saját modul): tankolási adatok kezelése
  - `bm_calc_consumption(liters, distance_km)`: Saját függvény, ami kiszámolja a fogyasztást liter/100 km egységben
  - `BMTankolasManager.bm_add_record(liters, price_per_liter, distance_km)`: Új tankolási rekord hozzáadása
  - `BMTankolasManager.bm_delete_record(index)`: Kiválasztott tankolás törlése
  - `BMTankolasManager.get_consumptions()`: Fogyasztások listájának lekérése
  - `BMTankolasManager.get_summary()`: Összegző statisztika előállítása (átlag, medián, min, max, szórás)
  - `BMTankolasManager.format_summary()`: Az összegzés szöveges formázása megjelenítéshez

## Osztályok

- **BMTankolasManager**  
  Feladata a tankolási adatok kezelése és a statisztika számítása.  
  Főbb metódusai:
  - `__init__(self)`: a belső lista (`records`) inicializálása
  - `bm_add_record(self, liters, price_per_liter, distance_km)`: egy új tankolási rekord létrehozása és eltárolása
  - `bm_delete_record(self, index)`: adott indexű rekord törlése
  - `get_consumptions(self)`: az eddig felvitt fogyasztásértékek összegyűjtése
  - `get_summary(self)`: átlag, medián, minimum, maximum, szórás kiszámítása ciklusok segítségével
  - `format_summary(self)`: az összegzés formázott, több soros szövegként való összeállítása

## Program felépítése

- **Indító modul**: `main.py`
  - Létrehozza az alapablakot (`root = Tk()`), beállítja a címet (`app`), létrehozza az űrlap mezőit (liter, ár, km), a gombokat és a listbox-ot.
  - Eseménykezelő függvények:
    - `bm_hozzaad()`: a beírt adatokból új tankolást hoz létre, hozzáadja a listához és a `Listbox`-hoz
    - `bm_osszegzes()`: meghívja a `BMTankolasManager.format_summary()` metódust, és az eredményt `messagebox`-ban jeleníti meg
    - `bm_torles_mezok()`: kiüríti a beviteli mezőket
    - `bm_torles_kivalasztott()`: a `Listbox`-ban kijelölt tankolást törli a listából és a modellből

- **Saját modul**: `bm_tankolas.py`
  - Tartalmazza a `bm_calc_consumption` saját függvényt és a `BMTankolasManager` saját osztályt.

## Telepítési utasítások

1. Python 3.x szükséges a futtatáshoz.
2. A használt modulok (`math`, `random`, `tkinter`) a Python standard könyvtár részei, külön telepítést nem igényelnek.
3. A program futtatása: python main.py

GitHub: https://github.com/martinbanfi-pxle61/BMFuelTrack