import random as rn

#vriables
freia = 0
your_number = 0

#deffinerer funksjonen sjokolade_fabrikk
def skjokolade_fabrikk():
    #variabelen freia blir satt til et random nummer mellom 0 og 10
    freia = rn.randint(0,10)
    #printer det randomet nummeret
    print(freia)

#deffinerer funksjonen rep
def rep():
    # spør om å repetere
    repeat = input('again?(y/n) ')
    # repeterer
    if repeat == 'y':
        #kaller funksjonen chatch_the_number
        catch_the_number()
    #repeterer ikke
    else:
        print('ok')

#deffinerer funksjonene chach the number
def catch_the_number():
    #lager variabelen your_ number
    your_number = int(input('Please enter a number between 0 to 10. '))
    #kaller sjokoladefabrikk
    ran_num = skjokolade_fabrikk()
    if your_number == ran_num:
        print('congratulations you won!!')

        rep()
    else:
        print('sorry, you lost:(')
        
        rep()

#starter spillet    
catch_the_number()