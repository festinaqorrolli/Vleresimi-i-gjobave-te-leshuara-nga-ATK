
# Vleresimi i gjobave te leshuara nga ATK

## Hyrje
Ky repozitor është përmbledhje e kodit Python për përpunimin dhe analizimin e një dataseti lidhur me gjobat e lëshuara nga [Administrata Tatimore e Kosovës](https://www.atk-ks.org/open-data/). Kodi fokusohet në pastrimin e të dhënave, analizën statistikore dhe vizualizimin, duke ofruar një pasqyrë të tendencave dhe modeleve në të dhëna.

## Librari të Përdorura
- **Pandas**: Për manipulimin dhe analizën e të dhënave.
- **Scikit-learn (PCA)**: Për reduktimin e dimensionalitetit përmes Analizës së Komponentit Kryesor.
- **Matplotlib.pyplot & Seaborn**: Për vizualizimin e të dhënave.
- **Numpy & Scipy**: Për llogaritje numerike dhe funksione statistikore.

## Dataseti
Dataseti, `gjobat-e-leshuara.csv`, përmban informacione të detajuara rreth ndryshme gjobave dhe penaliteteve të vendosura.

## Përshkrimi i Dataset-it
Dataset-i përmban informacione të detajuara mbi gjobat, duke përfshirë:

- VITI: Viti kur është dhënë gjoba.
- MUAJI: Muaji kur është dhënë gjoba.
- PERSHKRIMI_SEKTORIT: Përshkrimi i sektorit të cilës i takon kompania e gjobitur.
- LLOJI_KOMPAN: Lloji i kompanisë së gjobitur.
- KOMUNA: Komuna ku është dhënë gjoba.
- PEN_NO dhe PEN_TYPE_DESC_F: Id dhe neni për të cilin është dënuar.
- NR_TATIM dhe NR_GJOBAVE: Numri i tatimeve dhe numri total i gjobave.
- VLERA: Vlera totale e gjobave të marra.

## Gjendja e dataset-it para: 
```
Numri i rreshtave dhe kolonave para pastrimit
(29707, 12)
```

## Gjendja e dataset-it pas pastrimit: 
```
Numri i rreshtave dhe kolonave pas pastrimit
(29301, 11)
```

## Karakteristikat
Skripti përfshin disa operacione kyçe për menaxhimin e të dhënave:
- **Leximi i të Dhënave**: Lexon datasetin përmes Pandas.
- **Përpunimi**: Përfshin kontrollin për vlera që mungojnë, riemërimin e kolonave dhe integrimin e të dhënave.
- **Pastrimi i të Dhënave**: Standardizon vlerat e kolonave, heq regjistrimet e dyfishta dhe menaxhon outliers.
- **Binarizimi**: Binarizon një kolonë bazuar në vlerën mesatare të saj.
- **Zgjedhja e Nënëngrupeve**: Verifikon unicitetin e asocimeve midis kolonave të caktuara.
- **Paraqitja e të Dhënave**: Krahasimi i dataseteve fillestare dhe të përpunuara.
- **Zbulimi dhe Pastrimi i Outliers**: Vizualizon dhe pastron të dhënat nga outliers.
- **Zbulimi i Anomalive**: Kontrollon dhe heq anomali në kolona të ndryshme.
- **Parandalimi i Zbulimeve të Pasakta**: Kryen analiza për të shmangur interpretimet e gabuara.
- **Analiza Eksploruese e të Dhënave**: Ofron statistika përshkruese dhe vizualizime.
- **Trajtimi i Shtrembërimit**: Analizon dhe vizualizon shtrembërimin e variablave të zgjedhura.

## Përdorimi
Skripti është ndarë në seksione, secila e shënuar me `#%%`, për pjesë të ndryshme të procesit të analizës së të dhënave. Përdoruesit mund të ekzekutojnë gjithë skriptin për një analizë nga fillimi në fund ose të ekzekutojnë seksione të veçanta sipas nevojave.

## Instalimi
Para se të ekzekutoni skriptin, sigurohuni që të gjitha librariat e nevojshme janë të instaluar. Mund ti instaloni ato duke përdorur pip:

```bash
pip install pandas scikit-learn matplotlib seaborn numpy scipy
```

Sigurohuni që skedari i datasetit `gjobat-e-leshuara.csv` është i disponueshëm në direktorinë e saktë.

## Kontributet
Kontributet në këtë projekt janë të mirëpritura. Ju lutemi hapni një çështje së pari për të diskutuar se çfarë dëshironi të ndryshoni ose shtoni.

## Liçensa
[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/festinaqorrolli/Vleresimi-i-gjobave-te-leshuara-nga-ATK/blob/main/LICENSE.txt)
