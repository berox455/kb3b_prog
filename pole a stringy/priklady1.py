def pocet_samohlasek(text):
    pocet = 0

    for znak in text.lower():
        if znak == 'a' or znak == 'e' or znak == 'i' or znak == 'o' or znak == 'u':
            pocet += 1
    
    return pocet


def duplikuj(text):
    vys_text = ""

    for znak in text:
        vys_text += znak + znak

    return vys_text


def kolik_specialnich_znaku(text):
    specialni_znak = "!@#$^&*()_+=-[]{}|\,<.>/?`~:;"
    pocet_spzn = 0

    for znak in text:
        for sp_znak in specialni_znak:
            if znak == sp_znak:
                   pocet_spzn += 1

    return pocet_spzn       


def kolik_cislic(text):
    pocet_cislic = 0

    for znak in text:
        if znak.isdigit():
            pocet_cislic += 1

    return pocet_cislic
                         

def silne_heslo(text):
    if len(text) >= 7 and pocet_samohlasek(text) >= 2 and kolik_cislic(text) >= 1 and kolik_specialnich_znaku(text) >= 1:
        return True
    
    return False



print(silne_heslo("12345"))