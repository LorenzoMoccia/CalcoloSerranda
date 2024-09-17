import math

print("Scegli il modello di DOGA")
tipo_serranda = input("[1]. DOGA LISCIA |  [2]. DOGA ANTITEMPESTA\n")

if tipo_serranda == '1':
    print("Hai selezionato DOGA LISCIA, scegli ora lo spessore:")
    spessore = input("[1]. 8/10 | [2]. 10/10\n")
    
    altezza = input("Inserisci l'ALTEZZA in cm:\n")
    altezza = int(altezza) - 18
    larghezza = int(input("Inserisci la LARGHEZZA in cm:\n"))

    altezza_netto_terminale = altezza / 11.5
    altezza_netto_terminale = round(altezza_netto_terminale, 0)

    altezza_netto_terminale = altezza_netto_terminale * 11.5
    altezza_netto_terminale = altezza_netto_terminale * float(larghezza)
    
    area_serranda = altezza_netto_terminale / 10000
    
    if spessore == '1':
        area_serranda = area_serranda * 9
    elif spessore == '2':
        area_serranda = area_serranda * 11.5

    larghezza = larghezza / 100
    larghezza = larghezza * 3

    peso_totale = larghezza + area_serranda
    print(int(peso_totale))

elif  tipo_serranda == '2':
    print("Hai selezionato DOGA ANTITEMPESTA, scegli ora lo spessore:")
    spessore = input("[1]. 8/10 | [2]. 10/10\n")
    
    altezza = input("Inserisci l'ALTEZZA in cm:\n")
    altezza = int(altezza) - 18
    larghezza = int(input("Inserisci la LARGHEZZA in cm:\n"))

    altezza_netto_terminale = altezza / 9
    altezza_netto_terminale = round(altezza_netto_terminale, 0)

    altezza_netto_terminale = altezza_netto_terminale * 9
    altezza_netto_terminale = altezza_netto_terminale * float(larghezza)
    
    area_serranda = altezza_netto_terminale / 10000
    
    if spessore == '1':
        area_serranda = area_serranda * 9
    elif spessore == '2':
        area_serranda = area_serranda * 11.5

    larghezza = larghezza / 100
    larghezza = larghezza * 3

    peso_totale = larghezza + area_serranda
    print(int(peso_totale))

    



