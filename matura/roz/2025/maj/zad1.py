liczba_wywolan = 0
def liczba_wywolan_dekorator(func):
    global liczba_wywolan
    if liczba_wywolan > 0: liczba_wywolan = 0
    
    def wrapper(*args, **kwargs):
        global liczba_wywolan
        liczba_wywolan += 1
        print(f"Wywołanie nr {liczba_wywolan} funkcji {func.__name__}")
        return func(*args, **kwargs)
    
    return wrapper

@liczba_wywolan_dekorator
def przestaw(liczba:int) -> int:
    dwie_cyfry_od_prawej: int = liczba % 100
    prawa_cyfra: int = dwie_cyfry_od_prawej // 10
    lewa_cyfra: int = dwie_cyfry_od_prawej % 10
    liczba = liczba // 100
    
    if liczba > 0:
        wynik = 100*przestaw(liczba) + 10*lewa_cyfra + prawa_cyfra 
    else:
        if prawa_cyfra > 0:
            wynik = prawa_cyfra + 10*lewa_cyfra
        else:
            wynik = lewa_cyfra
    return wynik

print(przestaw(134689));liczba_wywolan=0
print(przestaw(43657688));liczba_wywolan=0
print(przestaw(154005710));liczba_wywolan=0
print(przestaw(998877665544321));liczba_wywolan=0
# 1.2 - FPPF

# 1.3
def przestaw2(liczba:int) -> int:
    wynik = 0
    n = 0
    
    while liczba > 0:
        obecna_para: int = liczba % 100
        
        if (obecna_para // 10) > 0:
            zamienione = 10*(obecna_para%10) + (obecna_para//10)
        else:
            zamienione = obecna_para
        
        wynik = wynik + zamienione * (100**n)
        
        n += 1
        liczba = liczba//100
        
    return wynik

print(przestaw2(1))
print(przestaw(1))
print(przestaw(1234) == przestaw2(1234))
print(przestaw(12345) == przestaw2(12345))
print(przestaw(123456) == przestaw2(123456))
print(przestaw(1234567) == przestaw2(1234567))
print(przestaw(12345678) == przestaw2(12345678))
print(przestaw(123456789) == przestaw2(123456789))
