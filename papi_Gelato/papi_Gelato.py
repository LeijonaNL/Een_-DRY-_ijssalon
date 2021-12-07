# Papi Gelato

# Importing time from device operating system.
import time, os

# Assigning preset input values to prevent error.
aantalBolletjes = 0
aantalHoorntjes = 0
aantalBakjes = 0
prijsBolletjes = 0
prijsHoorntjes = 0
prijsBakjes = 0
prijsTotaal = 0
hoorntjeBakje = 'Preset'
doorgaanStoppen = 'Preset'
smaakBol = 'Preset'
smaakBol1 = 'Preset'
smaakBol2 = 'Preset'
smaakBol3 = 'Preset'
smaakBol4 = 'Preset'
smaakBol5 = 'Preset'
smaakBol6 = 'Preset'
smaakBol7 = 'Preset'
smaakBol8 = 'Preset'

# Function for clearing screen (CLS), parameter is time until execution after initiation.
def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

# Function for canceling the program if requested, trigger: cancelProgram
def cancelProgramRequest():
    if aantalBolletjes == 'CANCELPROGRAM' or hoorntjeBakje == 'CANCELPROGRAM' or doorgaanStoppen == 'CANCELPROGRAM':
        print('Het programma is gestopt.')
        clearScreen(2)
        exit()


# 
def vraagAantalBolletjes(): # Main function 1
    print("Welkom bij Papi Gelato!")
    global aantalBolletjes # This variable is now globally usable.
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
    global smaakBol # This variable is now globally usable.
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
    global hoorntjeBakje # This variable is now globally usable.
    global aantalHoorntjes # This variable is now globally usable.
    global aantalBakjes # This variable is now globally usable.
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
                aantalHoorntjes = 1
            elif hoorntjeBakje == 'B':
                print("Ok!")
                clearScreen(1)
                hoorntjeBakje = 'bakje'
                aantalBakjes = 1
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
                aantalHoorntjes = 1
            elif hoorntjeBakje == 'B':
                print("Ok!")
                clearScreen(1)
                hoorntjeBakje = 'bakje'
                aantalBakjes = 1
            else:
                print("Sorry, dat snap ik niet...")
                clearScreen(2)
                repeat = True


# Asking if you want to repeat ordering/order more.
def vraagDoorgaanStoppen():
    global doorgaanStoppen # This variable is now globally usable.
    repeat = True
    # While repeat, in case unknown answers are given.
    while repeat:
        repeat = False
        if aantalBolletjes == 1:
            doorgaanStoppen = input(f"Hier is uw {hoorntjeBakje} met {aantalBolletjes} bolletje. Wilt u nog meer bestellen? (Y/N) ").upper()
        else:
            doorgaanStoppen = input(f"Hier is uw {hoorntjeBakje} met {aantalBolletjes} bolletjes. Wilt u nog meer bestellen? (Y/N) ").upper()
        cancelProgramRequest()
        if doorgaanStoppen == 'Y':
            clearScreen(1)
        elif doorgaanStoppen == 'N':
            print("Bedankt en tot ziens!")
            clearScreen(2)
        else:
            print("Sorry, dat snap ik niet...")
            clearScreen(2)
            repeat = True


# Function for calculating and showing the price ticket of the order.
def Bonnetje():
    global prijsBolletjes # This variable is now globally usable.
    global prijsHoorntjes # This variable is now globally usable.
    global prijsBakjes # This variable is now globally usable.
    global prijsTotaal # This variable is now globally usable.

    # Presetting calculations.
    prijsBolletjes = aantalBolletjes * 1.10
    prijsHoorntjes = aantalHoorntjes * 1.25
    prijsBakjes = aantalBakjes * 0.75
    prijsTotaal = prijsBolletjes + prijsHoorntjes + prijsBakjes

    # Ticket print.
    print(f'''----------[Papi Gelato]----------

Bolletjes     {aantalBolletjes} x 1.10   = €{format(prijsBolletjes, '.2f')}''')
    if aantalHoorntjes > 0:
        print(f'''Hoorntjes     {aantalHoorntjes} x 1.25   = €{format(prijsHoorntjes, '.2f')}''')
    if aantalBakjes > 0:
        print(f'''Bakjes        {aantalBakjes} x 0.75   = €{format(prijsBakjes, '.2f')}''')
    print(f'''                         -------- +
Totaal                   = €{format(prijsTotaal, '.2f')}\n''')


# Main function layout.
def papiGelato():
    repeat = True
    # While repeat, in case the program is to be re-executed.
    while repeat:
        repeat = False
        vraagAantalBolletjes()
        vraagSmaken()
        vraagHoorntjeBakje()
        Bonnetje()
        vraagDoorgaanStoppen()
        if doorgaanStoppen == 'Y': # If Y, the main function will be repeated.
            repeat = True

# Main function execution.
clearScreen(0.5)
papiGelato()