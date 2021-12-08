# Papi Gelato

# Importing time from device operating system.
import time, os

# Assigning preset input values to prevent error.
bestellingNr = 1
aantalBolletjes = 0
aantalHoorntjes = 0
aantalBakjes = 0
aantalToppings = 0
aantalBolletjesTotaal = 0
aantalSlagroom = 0
aantalSpikkels = 0
aantalCaramelHoorntje = 0
aantalCaramelBakje = 0
prijsBolletjes = 0
prijsHoorntjes = 0
prijsBakjes = 0
prijsToppings = 0
prijsSlagroom = 0
prijsSpikkels = 0
prijsCaramelHoorntje = 0
prijsCaramelBakje = 0
eindPrijs = 0
hoorntjeBakje = 'Preset'
doorgaanStoppen = 'Preset'
smaakBol = 'Preset'
topping = 'Preset'

# Function for clearing screen (CLS), parameter is time until execution after initiation.
def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

# Function for canceling the program if requested, trigger: cancelProgram
def cancelProgramRequest():
    if aantalBolletjes == 'CANCELPROGRAM'\
    or smaakBol == 'CANCELPROGRAM'\
    or hoorntjeBakje == 'CANCELPROGRAM'\
    or topping == 'CANCELPROGRAM'\
    or doorgaanStoppen == 'CANCELPROGRAM':
        print('Het programma is gestopt.')
        clearScreen(2)
        exit()


# 
def vraagAantalBolletjes(): # Main function 1
    # This variable is now globally usable.
    global aantalBolletjes
    if bestellingNr == 1:
        print("Welkom bij Papi Gelato!")
    repeat = True
    #
    while repeat:
        repeat = False
        aantalBolletjes = input("Hoeveel bolletjes wilt U? ").upper()
        cancelProgramRequest()
        if aantalBolletjes != 'CANCELPROGRAM':
            aantalBolletjes = int(aantalBolletjes)
        if 0 < aantalBolletjes <= 3:
            print("Ok!")
            clearScreen(1)
        elif 3 < aantalBolletjes <= 8:
            print(f"Dan krijgt u van mij een bakje met {aantalBolletjes} bolletjes.")
            clearScreen(3)
        elif 8 < aantalBolletjes:
            print("Sorry, zulke grote bakken hebben we niet.")
            clearScreen(2)
            repeat = True
        else:
            print("Sorry dat snap ik niet...")
            clearScreen(2)
            repeat = True


# Asking what flavours the customer wants.
def vraagSmaken():
    # This variable is now globally usable.
    global smaakBol
    # While, repeats the question (every time for a different Bolletje) until all Bolletjes have been assigned a flavour.
    Bolletje = 1
    while Bolletje <= aantalBolletjes:
        smaakBol = input(f"Welke smaak wilt u voor bolletje nummer {Bolletje}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ").upper()
        cancelProgramRequest()
        if smaakBol == 'A' or smaakBol == 'C' or smaakBol == 'M' or smaakBol == 'V':
            print("Ok!")
            clearScreen(2)
            Bolletje += 1
        else:
            print("Sorry, dat snap ik niet...")
            clearScreen(2)



# Asking if you want the icecream in a cup or on a cone.
def vraagHoorntjeBakje():
    # These variables are now globally usable.
    global hoorntjeBakje
    global aantalHoorntjes
    global aantalBakjes
    repeat = True
    # While repeat, in case unknown answers are given.
    while repeat:
        repeat = False
        if 3 < aantalBolletjes:
            hoorntjeBakje = 'bakje'
        elif aantalBolletjes == 1:
            hoorntjeBakje = input(f"Wilt U dit bolletje in een A) een hoorntje of B) een bakje? ").upper()
            cancelProgramRequest()
            if hoorntjeBakje == 'A':
                print("Ok!")
                clearScreen(1)
                hoorntjeBakje = 'hoorntje'
                aantalHoorntjes += 1
            elif hoorntjeBakje == 'B':
                print("Ok!")
                clearScreen(1)
                hoorntjeBakje = 'bakje'
                aantalBakjes += 1
            else:
                print("Sorry, dat snap ik niet...")
                clearScreen(2)
                repeat = True
        elif 1 < aantalBolletjes <= 3:
            hoorntjeBakje = input(f"Wilt U deze {aantalBolletjes} bolletjes in A) een hoorntje of B) een bakje? ").upper()
            cancelProgramRequest()
            if hoorntjeBakje == 'A':
                print("Ok!")
                clearScreen(1)
                hoorntjeBakje = 'hoorntje'
                aantalHoorntjes += 1
            elif hoorntjeBakje == 'B':
                print("Ok!")
                clearScreen(1)
                hoorntjeBakje = 'bakje'
                aantalBakjes += 1
            else:
                print("Sorry, dat snap ik niet...")
                clearScreen(2)
                repeat = True


#
def vraagTopping():
    # These variables are now globally usable.
    global topping
    global aantalToppings
    global aantalSlagroom
    global aantalSpikkels
    global aantalCaramelHoorntje
    global aantalCaramelBakje
    repeat = True
    #
    while repeat:
        repeat = False
        topping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ").upper()
        cancelProgramRequest()
        if topping == 'A':
            print("Ok!")
            clearScreen(1)
            topping = 'geen'
            aantalToppings += 0
        elif topping == 'B':
            print("Ok!")
            clearScreen(1)
            topping = 'slagroom'
            aantalToppings += 1
            aantalSlagroom += 1
        elif topping == 'C':
            print("Ok!")
            clearScreen(1)
            topping = 'sprinkels'
            aantalToppings += 1
            aantalSpikkels += 1
        elif topping == 'D':
            print("Ok!")
            clearScreen(1)
            topping = 'caramel'
            aantalToppings += 1
            if hoorntjeBakje == 'hoorntje':
                aantalCaramelHoorntje += 1
            elif hoorntjeBakje == 'bakje':
                aantalCaramelBakje += 1
        else:
            print("Sorry, dat snap ik niet...")
            clearScreen(2)
            repeat = True


# Function for calculating and showing the price ticket of the order.
def Bonnetje():
    # These variables are now globally usable.
    global prijsBolletjes
    global prijsHoorntjes
    global prijsBakjes
    global prijsToppings
    global prijsSlagroom
    global prijsSpikkels
    global prijsCaramelHoorntje
    global prijsCaramelBakje

    # Presetting calculations.
    prijsBolletjes = aantalBolletjesTotaal * 1.10
    prijsHoorntjes = aantalHoorntjes * 1.25
    prijsBakjes = aantalBakjes * 0.75
    prijsSlagroom = aantalSlagroom * 0.50
    prijsSpikkels = aantalSpikkels * 0.30
    prijsCaramelHoorntje = aantalCaramelHoorntje * 0.60
    prijsCaramelBakje = aantalCaramelBakje * 0.90
    prijsToppings = prijsSlagroom + prijsSpikkels + prijsCaramelHoorntje + prijsCaramelBakje
    eindPrijs = prijsBolletjes + prijsHoorntjes + prijsBakjes + prijsToppings

    # Ticket print.
    if aantalBolletjesTotaal < 10:
        print(f'''----------[Papi Gelato]----------

Bolletjes     {aantalBolletjesTotaal} x 1.10   = €{format(prijsBolletjes, '.2f')}''')
    elif aantalBolletjesTotaal >= 10:
        print(f'''----------[Papi Gelato]----------

Bolletjes     {aantalBolletjesTotaal} x 1.10  = €{format(prijsBolletjes, '.2f')}''')
    if aantalHoorntjes > 0:
        print(f'''Hoorntjes     {aantalHoorntjes} x 1.25   = €{format(prijsHoorntjes, '.2f')}''')
    if aantalBakjes > 0:
        print(f'''Bakjes        {aantalBakjes} x 0.75   = €{format(prijsBakjes, '.2f')}''')
    if aantalToppings > 0:
        print(f'''Toppings      {aantalToppings}''')
    if aantalSlagroom > 0:
        print(f'''Slagroom      {aantalSlagroom} x 0.50   = €{format(prijsSlagroom, '.2f')}''')
    if aantalSpikkels > 0:
        print(f'''Spikkels      {aantalSpikkels} x 0.30   = €{format(prijsSpikkels, '.2f')}''')
    if aantalCaramelHoorntje > 0:
        print(f'''Hoorn Caramel {aantalCaramelHoorntje} x 0.60   = €{format(prijsCaramelHoorntje, '.2f')}''')
    if aantalCaramelBakje > 0:
        print(f'''Bakje Caramel {aantalCaramelBakje} x 0.90   = €{format(prijsCaramelBakje, '.2f')}''')
    print(f'''                         -------- +
Totaal                   = €{format(eindPrijs, '.2f')}\n''')


# Asking if you want to repeat ordering/order more.
def vraagDoorgaanStoppen():
    global doorgaanStoppen
    repeat = True
    # While repeat, in case unknown answers are given.
    while repeat:
        repeat = False
        if aantalBolletjes == 1:
            doorgaanStoppen = input(f"Hier is Uw {hoorntjeBakje} met {aantalBolletjes} bolletje. Wilt u nog meer bestellen? (Y/N) ").upper()
        else:
            doorgaanStoppen = input(f"Hier is Uw {hoorntjeBakje} met {aantalBolletjes} bolletjes. Wilt u nog meer bestellen? (Y/N) ").upper()
        cancelProgramRequest()
        if doorgaanStoppen == 'Y':
            print("Ok! Zeg maar wat U wilt.")
            clearScreen(2)
        elif doorgaanStoppen == 'N':
            print("Ok! Hier is Uw bonnetje, bedankt en tot ziens!")
            clearScreen(2)
        else:
            print("Sorry, dat snap ik niet...")
            clearScreen(2)
            repeat = True



# Main function layout.
def papiGelato():
    global bestellingNr
    global eindPrijs
    global aantalBolletjesTotaal
    repeat = True
    # While repeat, in case the program is to be re-executed.
    while repeat:
        repeat = False
        vraagAantalBolletjes()
        vraagSmaken()
        vraagHoorntjeBakje()
        vraagTopping()
        aantalBolletjesTotaal += aantalBolletjes
        vraagDoorgaanStoppen()
        if doorgaanStoppen == 'Y': # If Y, the main function will be repeated.
            bestellingNr += 1
            repeat = True
        elif doorgaanStoppen == 'N':
            print("Ok! Hier is Uw bonnetje, bedankt en tot ziens!")
            Bonnetje()

# Main function execution.
clearScreen(0.5)
papiGelato()