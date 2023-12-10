# Patst-vigais-darbs - Masīnu izvele

### Programma Atrast Savu Sapņu Auto

`atrast_auto(marka, gads, ak, degviela, tilpums)`

Šī funkcija tiek izmantota, lai atrastu automašīnas modeļus atbilstoši norādītajiem kritērijiem.

### Ievades parametri:
- `marka` : Norāda automašīnas marku.
- `gads` : Norāda automašīnas izlaišanas gadu.
- `ak` : Norāda automašīnas ātrumkārbas tipu (Manuālā/Automātiskā).
- `degviela` : Norāda automašīnas degvielas tipu (Benzīns/Dīzelis).
- `tilpums` : Norāda automašīnas dzinēja tilpumu.

### Izvades parametri:
- `atbilstosie_auto` (list): Saraksts ar automašīnas modeļiem, kas atbilst norādītajiem kritērijiem. Ja nav atbilstošu automašīnu, izvadīs tukšu sarakstu.

### Funkcijas darbība:
1. Pārbauda `automobili` sarakstu, lai atrastu automašīnas, kas atbilst ievadītajiem kritērijiem.
2. Ja automašīna atbilst visiem kritērijiem, pievieno tās modeļa nosaukumu `atbilstosie_auto` sarakstam.

### Ievades dati:
1. **Lietotājam jāievada šādi dati:**
    - `marka` - Automašīnas marka #(piemēram, "AUDI", "BMW", utt.).
    - `gads` - Automašīnas izlaišanas gads #(piemēram, 2010, 2015, utt.).
    - `ak` - Automašīnas ātrumkārbas tips #("Manuālā" vai "Automātiskā").
    - `degviela` - Automašīnas degvielas tips #("Benzīns" vai "Dīzelis").
    - `tilpums` - Automašīnas dzinēja tilpums #(piemēram, 1.0, 1.6, utt.).
### Izvades dati:
1.  **Lietotājs iegūs šādus datus**
    - Ja funkcija atrada atbilstošas automašīnas, izvadīsies atbilstošo automašīnu modeļi.
    - Ja nekas neatbilst ievadītajiem kritērijiem, izvadīsies paziņojums, ka nekas netika atrasts.

### Piemērs:

```python
rezultats = atrast_auto("AUDI", 2015, "Automātiskā", "Benzīns", 1.6)
print(rezultats)
# Izvads: ["A1"]

