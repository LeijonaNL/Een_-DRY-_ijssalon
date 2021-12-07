# Papi Gelato

# Importing time from device operating system.
import time, os

# Assigning preset input values to prevent error.
aantalBolletjes = 0
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
    print("Welkom bij Papi Gelato, je mag alle smaken kiezen zo lang het maar vanille ijs is.")
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


#
def vraagSmaken():
    global smaakBol
    #
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



#
def vraagHoorntjeBakje(): # Main function 2
    global hoorntjeBakje # This variable is now globally usable.
    repeat = True
    #
    while repeat:
        repeat = False
        if 3 < aantalBolletjes:
            hoorntjeBakje = 'bakje'
        elif aantalBolletjes == 1:
            hoorntjeBakje = input(f"Wilt U dit bolletje in een A) een hoorntje of B) een bakje? ").upper()
            cancelProgramRequest()
            if hoorntjeBakje == 'A':
                clearScreen(1)
                hoorntjeBakje = 'hoorntje'
            elif hoorntjeBakje == 'B':
                clearScreen(1)
                hoorntjeBakje = 'bakje'
            else:
                print("Sorry, dat snap ik niet...")
                clearScreen(2)
                repeat = True
        elif 1 < aantalBolletjes <= 3:
            hoorntjeBakje = input(f"Wilt U deze {aantalBolletjes} bolletje(s) in A) een hoorntje of B) een bakje? ").upper()
            cancelProgramRequest()
            if hoorntjeBakje == 'A':
                clearScreen(1)
                hoorntjeBakje = 'hoorntje'
            elif hoorntjeBakje == 'B':
                clearScreen(1)
                hoorntjeBakje = 'bakje'
            else:
                print("Sorry, dat snap ik niet...")
                clearScreen(2)
                repeat = True


#
def vraagDoorgaanStoppen(): # Main function 3
    global doorgaanStoppen # This variable is now globally usable.
    repeat = True
    #
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


# Main function layout.
def papiGelato():
    repeat = True
    #
    while repeat:
        repeat = False
        vraagAantalBolletjes()
        vraagSmaken()
        vraagHoorntjeBakje()
        vraagDoorgaanStoppen()
        if doorgaanStoppen == 'Y': # If Y, the main function will be repeated.
            repeat = True

# Main function execution.
clearScreen(1)
papiGelato()