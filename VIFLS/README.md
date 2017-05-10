# VIFLS - Videoinnholdsfortegnelses Latex-skaper
* Automatiserer prosessen med å lage Latex-koden til hver forelesning i videoinnholdsfortegnelsen.

# Vanlig bruk
* Endre 'forelesning.txt' (bruk samme format som den kommer med).
* Kjør 'VIFLS.py' ved å f.eks. navigere deg til mappen 'VIFLS' ligger i med terminal. Skriv så kommandoen 'python3 VIFLS.py' for å utføre scriptet.
* Etter at scriptet er kjørt vil det automatisk kopiére LATEX-koden til utklippstavlen din.

# OBS
* Scriptet fungerer kun på macOS (men kan relativt enkelt utvides til Windows).
* Kulepunktene i forelesning.txt kan ikke inneholde tegnrekkefølgen ' - ' annet enn når tidspunkt og kulepunktstekst skal skilles.
* Prøv å unngå bruk av '\' ettersom python tolker f.eks. '\t' som et innrykk og ikke som ren tekst.
