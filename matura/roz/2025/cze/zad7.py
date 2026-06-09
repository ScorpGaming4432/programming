klienci_file = 'informatyka-2025-czerwiec-matura-rozszerzona-zalaczniki\\klienci.txt'
fryzjerzy_file = 'informatyka-2025-czerwiec-matura-rozszerzona-zalaczniki\\fryzjerzy.txt'
uslugi_file = 'informatyka-2025-czerwiec-matura-rozszerzona-zalaczniki\\uslugi.txt'
wizyty_file = 'informatyka-2025-czerwiec-matura-rozszerzona-zalaczniki\\wizyty.txt'


danes = {}
for a in [klienci_file, fryzjerzy_file, uslugi_file, wizyty_file]:
    with open(a, 'r') as f:
        