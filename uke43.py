import math

#spør om hvilken oppg
oppg = int(input("which task?(1, 2, 3) "))

if oppg == int(1):

        ##Oppgave 1##
    ''' Hvis du  blir tilbudt 300 krone for å vaske et hus, ville du gjort det
    da? hva om du ble tilbudt dette i 2 månader, hvor betalingen ville økes 15%
    hver dag. Det vil si kr300 første dag, 345 andre dag, kr396.75 neste dag, osv.  '''

      ### your task##
    '''Lag en funksjon som regner ut total lønn etter 2 måneder, og lønn for 
    dag 15, 30, 45 og 50. Bruk print() for å vise disse verdiene i terminalen'''

    #forklarer oppgaven
    print("you get offerd x amount of money for washing a house, if you did this for 2 months or longer the price would increase by 15% each day(y)")
    
    '''repeat variable'''
    rep = int(1)

    '''repeat'''
    while rep == int(1):
        '''asks for starting salary'''
        a = int(input("starting salary(x): "))

        '''function for calculating 115%'''
        def lønn():
            b = a + ((a / 100) * 15)
            return(b)

        '''calculating day'''
        d = int(input("which day?(y) "))
        while range(d):
            a = lønn()
            lønn()
            d = int(d) -1
        print(lønn())    

        rep = input("want to know more?(y/n) ")
        if rep == str("y"):
            rep = 1
        elif rep == str("n"):
            rep = 0
        else:
            print("?")
        
elif oppg == int(2):
    ##Oppgave 2##
    ''' Opprett en funksjon som kan tegne følgende figur i terminalen:
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *********
    **********
    ***********
              *
             **
            ***
           ****
          *****
         ******
        *******
       ********
      *********
     **********
    ***********
    '''
    #variable
    rep = int(1)
    while rep == int(1):
        a = "*"
        #spør hvor mange rader personen ønsker
        b = int(input("how many rows? "))

        def star():
                print(a)

        while range(b):
            star()
            a = a + "*"
            b = b - 1
        rep = input("again?(y/n) ")
        if rep == str("y"):
            rep = 1
        elif rep == str("n"):
            rep = 0
        else:
            print("?")

else:
    #   #Oppgave 3##
    ''' Opprett en funksjon som kan printe alle primtall i variabel prime_numbers '''
    prime_numbers = [1, 5, 6, 7, 10, 11, 19, 23, 25, 26, 31, 26, 37, 40, 43, 67, 73, 99, 101]

    print("Your List is : ", prime_numbers) 
    print("Prime numbers in your list is/are : ") 
    for num in prime_numbers:  
        if num > 1: 
            for i in range(2,num): 
                if (num % i) == 0: 
                    break 
            else: 
                print(num) 