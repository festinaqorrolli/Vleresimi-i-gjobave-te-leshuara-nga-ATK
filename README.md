# Vleresimi-i-gjobave-te-leshuara-nga-ATK
[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/festinaqorrolli/Vleresimi-i-gjobave-te-leshuara-nga-ATK/blob/main/LICENSE.txt)

#### Analiza e Gjobave të lëshuara nga Administrata Tatimore e Kosovës

####  Dataset-i është marrë nga: [Administrata Tatimore e Kosovës](https://www.atk-ks.org/open-data/)

##### Ky repositor përmban të dhëna dhe skripte lidhur me analizën e gjobave të lëshuara nga Agjencia Tatimore e Kosovës (ATK). Projekti synon të eksplorojë dhe të paraqesë informacionin e detajuar rreth gjobave , duke përfshirë shumëllojshmërinë e tyre në disa aspekte:

#### Përshkrimi i Dataset-it
##### Dataset-i përmban informacione të detajuara mbi gjobat, duke përfshirë:

###### - VITI: Viti kur është dhënë gjoba.
###### - MUAJI: Muaji kur është dhënë gjoba.
###### - PERSHKRIMI_SEKTORIT: Përshkrimi i sektorit të cilës i takon kompania e gjobitur.
###### - LLOJI_KOMPAN: Lloji i kompanisë së gjobitur.
###### - KOMUNA: Komuna ku është dhënë gjoba.
###### - PEN_NO dhe PEN_TYPE_DESC_F: Id dhe neni për të cilin është dënuar.
###### - NR_TATIM dhe NR_GJOBAVE: Numri i tatimeve dhe numri total i gjobave.
###### - VLERA: Vlera totale e gjobave të marra.

#### Gjendja e dataset-it para: 
```
Numri i rreshtave dhe kolonave para pastrimit
(29707, 12)
```

#### Gjendja e dataset-it pas pastrimit: 
```
Numri i rreshtave dhe kolonave pas pastrimit
(29301, 11)
```

#### Përdorimi

Për të përdorur këtë projekt në makinën tuaj lokale, bëni këto hapa:

#### Klononi repozitorin:

```
git clone https://github.com/festinaqorrolli/Vleresimi-i-gjobave-te-leshuara-nga-ATK.git
```

#### Shkoni në direktoriumin e projektit:

```
cd Vleresimi-i-gjobave-te-leshuara-nga-ATK
```

#### Instaloni librari të nevojshme të Python-it:

```
pip install -r requirements.txt
```

#### Hapni dhe ekzekutoni Jupyter Notebook (main.ipynb) për të parë analizën dhe vizualizimin e rezultateve.
