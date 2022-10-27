import random as rn
import pygame as pg

## Oppgave 1##
pg.init()

w = 600
h = 650

a = True

while a == True:
    background = pg.display.set_mode((w, h))
    pg.display.set_caption =('Oppgave_medium')
    pg.display.flip()

    a = rn.randint(1,30)
    b = rn.randint(30,40)
    c = rn.randint(400, 600)
    d = rn.randint(3, 200)
    e = rn.randint(1, 500)
    coord1=(a,b)
    coord2=(a,c)
    coord3=(a,d)
    coord4=(a,e)
    coord5=(b,a)
    coord6=(b,c)
    coord7=(b,d)
    coord8=(b,e)
    coord9=(c,a)
    coord10=(c,b)
    coord11=(c,d)
    coord12=(c,e)
    coord13=(d,a)
    coord14=(d,b)
    coord15=(d,c)
    coord16=(d,e)
    coord17=(e,a)
    coord18=(e,b)
    coord19=(e,c)
    coord20=(e,d)

    h = list[coord1,coord2,coord3,coord4,coord5,coord6,coord7,coord8,coord9,coord10,coord11,coord12,coord13,coord13,coord14,coord15,coord16,coord17,coord18,coord19,coord20]
    

    pg.draw.polygon(background,(255,255,255), h)
'''
Variablene a og b inneholder tilfedige verdier mellom 1 og 30 (a), og mellom 30 og 40 (b). Variabelen coord1
inneholder verdiene av a og b. 
Opprett en funksjon som kan tegne tilfeldige figurer. For å løse denne oppgaven må du lage flere variabler som 
brukes som koordinate-punkter for å tegne figurer for eksempel:'''

