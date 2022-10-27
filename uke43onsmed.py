import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as pp

# startsetting
rep = True

while rep == True:
    b = float(input('hva er din og din partners fellesintekt?(skriv i millioner og bruk punktum istedefor komma) '))
    b *= 1000000
    #kjøpssum
    kjøpssum = float(input('hva koster huset?(--||--) '))
    #fellesintekt > 18% av kjøpsum
    fellesintekt = kjøpssum * 0,18
    if b > sum(fellesintekt):
        #variabler
        rente = 3.78
        ønsketlån = int(input('hvor mye ønsker du å låne?(--||--) ')) * 1000000
        lånprår = float(ønsketlån / 20)
        lånprmåned = lånprår / 12
        #2 eller mer barn betaler 0.015% mer
        barn = int(input('hvor mange barn har du? '))
        if barn >= 2:
            rente = rente + 0.015
        #--||-- betaler 0,005% mer
        bil = int(input('hvor mange biler har du? '))
        if bil >= 2:
            rente = rente + 0.005
        #egenkapital > 20% av ønsketlån betaler -0.010% mindre
        egenkapital = int(input('hva er din egenkapital? '))
        if egenkapital > ønsketlån * 0.2:
            rente = rente - 0.01
        #fellesgjeld > 5 mil betaler 0.01% mer
        fellesgjeld = int(input('hva er din/deres fellesgjeld? '))
        if fellesgjeld > 5000000:
            rente = rente + 0.01
        renteavlån = float(lånprmåned) * (rente / 100) + lånprmåned
        vekstfaktor = (rente / 100) + 0.1

        #regne ut renta og lage en liste med renta for hvert år
        renteår = []
        
        a = 0
        while a < 20:
            renteår.append(lånprår)
            lånprår = lånprår * vekstfaktor
            a += 1
        print('lånsutgift hvert år:')
        print(renteår)
        
        #regne ut avdrag og lage liste med avdrag per måned,
        rentemnd = []
        
        a = 0
        while a < 120:
            rentemnd.append(lånprmåned)
            lånprmåned = lånprmåned * vekstfaktor
            a += 1
        print('lånsutgift hvert år:')
        print(rentemnd)

        #lage diagram med matplotlib
        måneder = []
        def måned():
            g = 0
            while g <= 120:
                måneder.append(g)
                g += 1
        måneder = [måned()]

        pp.plot([måneder], [rentemnd])
        pp.ylabel('lånkostnader')
        pp.xlabel('måned')
        pp.show()


    else:
        print('sorry intekten din er for lav')
        break
        

    rep = input("again?(y/n) ")
    if rep == str("y"):
        print('yay')
        rep = 1
    elif rep == str("n"):
        print('ok')
        rep = 0
    else:
        print("?")