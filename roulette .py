#Made By: Francisco Pedrosa (N0883131)
import random
import time
import os
import getpass
import hashlib

loggedName = ""
numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

#Main Image
def mainImage():
    print("\n\t\t\t\t******  ******* *     * *       ******* ******* ******* ******* ")
    print("\t\t\t\t*     * *     * *     * *       *          *       *    *       ")
    print("\t\t\t\t*     * *     * *     * *       *          *       *    *       ")
    print("\t\t\t\t******  *     * *     * *       *****      *       *    *****   ")
    print("\t\t\t\t*   *   *     * *     * *       *          *       *    *       ")
    print("\t\t\t\t*    *  *     * *     * *       *          *       *    *       ") 
    print("\t\t\t\t*     * *******  *****  ******* *******    *       *    ******* ")

#Menu
def menu():
    os.system("cls")
    os.system("color 06")
    mainImage()
    time.sleep(0.3)
    print("\n\n\t\t\t\t\t\t\t1 - Play")
    time.sleep(0.3)
    print("\t\t\t\t\t\t\t2 - Account")
    time.sleep(0.3)
    print("\t\t\t\t\t\t\t3 - About")
    time.sleep(0.3)
    print("\t\t\t\t\t\t\t4 - Exit")

    menuOption = int(input("\n\n\t\t\t\tOption => "))
    if menuOption == 1:
        if loggedName == "":
            os.system("cls")
            os.system("color 04")
            mainImage()
            print("\n\n\t\t\t\t\t\tFirst you need to SIGN IN!")
            input()
            menu()
        else:
            getMoney()
            if cash == 0:
                os.system("cls")
                os.system("color 04")
                mainImage()
                print("\n\n\t\t\t\t\t\tYou DON'T have money to PLAY!")
                input()
                menu()
            else:
                game()

    elif menuOption == 2:
        if loggedName != "":
            loggedAccount()
        else:
            notLoggedAccount()
    elif menuOption == 3:
        about()
    elif menuOption == 4:
        exitGame()
    else:
        menu()

#Game
def game():
    playAgain = 1

    while playAgain == 1:
        os.system("cls")
        os.system("color 06")
        getMoney()
        print("\n\t\t\t\tUsername: " + loggedName + "\t\t\t\tMoney: " + str(cash) + "£")
        rouletteImage()
        betType = int(input("\n\t\t Where to BET (0|1|2) => "))
        if betType != 0 and betType != 1 and betType != 2:
            os.system("color 04")
            print("\n\t\t You can ONLY use the numbers 0, 1 or 2!")
            input()
            game()
        else:
            betCash = int(input("\t\t How mutch to BET (£) => "))
            if betCash > cash:
                os.system("color 04")
                print("\n\t\t You CANNOT bet more than what you have!")
                input()
                game()
            elif betCash == 0:
                os.system("color 04")
                print("\n\t\t You CANNOT bet 0 Money!")
                input()
                game()
            else:
                cashUpdate = cash - betCash
                updateMoney(cashUpdate)
                 
                animation(betCash)
                stopRolling(betType,betCash)

                if cash != 0:
                    print("\t\t Play Again?")
                    playAgainQuestion = input("\t\t Yes or No -> ")
                    if playAgainQuestion != "Yes" and playAgainQuestion != "YES" and playAgainQuestion != "yes" and playAgainQuestion != "y" and playAgainQuestion != "Y":
                        playAgain = 0
                        break
                else:
                    break 
   
    
#Roulette Image
def rouletteImage():    
    print("\t\t/------------------------------------------------------------------------------------\\")
    print("\t\t|                                                                                    |")
    print("\t\t|                                         ||                                         |")
    print("\t\t|                                         ||                                         |")
    print("\t\t|                                         \\/                                         |")
    print("\t\t|    ----------------------------------------------------------------------------    |")
    print("\t\t|    | "+str(format('%02.0F' % numbers[0]))+" | "+str(format('%02.0F' % numbers[1]))+" | "+str(format('%02.0F' % numbers[2]))+" | "+str(format('%02.0F' % numbers[3]))+" | "+str(format('%02.0F' % numbers[4]))+" | "+str(format('%02.0F' % numbers[5]))+" | "+str(format('%02.0F' % numbers[6]))+" | "+str(format('%02.0F' % numbers[7]))+" | "+str(format('%02.0F' % numbers[8]))+" | "+str(format('%02.0F' % numbers[9]))+" | "+str(format('%02.0F' % numbers[10]))+" | "+str(format('%02.0F' % numbers[11]))+" | "+str(format('%02.0F' % numbers[12]))+" | "+str(format('%02.0F' % numbers[13]))+" | "+str(format('%02.0F' % numbers[14]))+" |    |")
    print("\t\t|    ----------------------------------------------------------------------------    |")
    print("\t\t|                                         /\\                                         |")
    print("\t\t|                                         ||                                         |")
    print("\t\t|                                         ||                                         |")
    print("\t\t|                                                                                    |")
    print("\t\t|                /-------------------------------------------------\\                 |")
    print("\t\t|                |    ODD(x2)    |    ZERO(x15)    |    EVEN(x2)   |                 |")
    print("\t\t|                |      (1)      |      (0)        |      (2)      |                 |")
    print("\t\t|                \\-------------------------------------------------/                 |")
    print("\t\t|                                                                                    |")
    print("\t\t\\------------------------------------------------------------------------------------/")

#Roulette Animation
def animation(bet):
    os.system("cls")
    os.system("color 06")         
    counter = 0
    numberOfSpins = random.randint(30,40)

    getMoney()
     
    while counter <= numberOfSpins:
        os.system("cls")
        print("\n\t\t\t\tUsername: " + loggedName + "\t\tBet: " + str(bet)+ "£\tMoney: " + str(cash) + "£") 
        print("\t\t/------------------------------------------------------------------------------------\\")
        print("\t\t|                                                                                    |")
        print("\t\t|                                         ||                                         |")
        print("\t\t|                                         ||                                         |")
        print("\t\t|                                         \\/                                         |")
        print("\t\t|    ----------------------------------------------------------------------------    |")
        print("\t\t|    | "+str(format('%02.0F' % numbers[0]))+" | "+str(format('%02.0F' % numbers[1]))+" | "+str(format('%02.0F' % numbers[2]))+" | "+str(format('%02.0F' % numbers[3]))+" | "+str(format('%02.0F' % numbers[4]))+" | "+str(format('%02.0F' % numbers[5]))+" | "+str(format('%02.0F' % numbers[6]))+" | "+str(format('%02.0F' % numbers[7]))+" | "+str(format('%02.0F' % numbers[8]))+" | "+str(format('%02.0F' % numbers[9]))+" | "+str(format('%02.0F' % numbers[10]))+" | "+str(format('%02.0F' % numbers[11]))+" | "+str(format('%02.0F' % numbers[12]))+" | "+str(format('%02.0F' % numbers[13]))+" | "+str(format('%02.0F' % numbers[14]))+" |    |")
        print("\t\t|    ----------------------------------------------------------------------------    |")
        print("\t\t|                                         /\\                                         |")
        print("\t\t|                                         ||                                         |")
        print("\t\t|                                         ||                                         |")
        print("\t\t|                                                                                    |")
        print("\t\t|                /-------------------------------------------------\\                 |")
        print("\t\t|                |    ODD(x2)    |    ZERO(x15)    |    EVEN(x2)   |                 |")
        print("\t\t|                |      (1)      |      (0)        |      (2)      |                 |")
        print("\t\t|                \\-------------------------------------------------/                 |")
        print("\t\t|                                                                                    |")
        print("\t\t\\------------------------------------------------------------------------------------/")

        #To equal the number 0 to number 14
        aux = numbers[0]
    
        numbers[0] = numbers[1]
        numbers[1] = numbers[2]
        numbers[2] = numbers[3]
        numbers[3] = numbers[4]
        numbers[4] = numbers[5]
        numbers[5] = numbers[6]
        numbers[6] = numbers[7]
        numbers[7] = numbers[8]
        numbers[8] = numbers[9]
        numbers[9] = numbers[10]
        numbers[10] = numbers[11]
        numbers[11] = numbers[12]
        numbers[12] = numbers[13]
        numbers[13] = numbers[14]
        numbers[14] = aux

        time.sleep(0.1)
        counter = counter + 1

def stopRolling(betType,bet):
    rolledNumber = random.randint(0,14)
    counter = 0
    
    while numbers[6] != rolledNumber:
        os.system("cls")
        
        print("\n\t\t\t\tUsername: " + loggedName + "\t\tBet: " + str(bet)+ "£\tMoney: " + str(cash) + "£") 
        print("\t\t/------------------------------------------------------------------------------------\\")
        print("\t\t|                                                                                    |")
        print("\t\t|                                         ||                                         |")
        print("\t\t|                                         ||                                         |")
        print("\t\t|                                         \\/                                         |")
        print("\t\t|    ----------------------------------------------------------------------------    |")
        print("\t\t|    | "+str(format('%02.0F' % numbers[0]))+" | "+str(format('%02.0F' % numbers[1]))+" | "+str(format('%02.0F' % numbers[2]))+" | "+str(format('%02.0F' % numbers[3]))+" | "+str(format('%02.0F' % numbers[4]))+" | "+str(format('%02.0F' % numbers[5]))+" | "+str(format('%02.0F' % numbers[6]))+" | "+str(format('%02.0F' % numbers[7]))+" | "+str(format('%02.0F' % numbers[8]))+" | "+str(format('%02.0F' % numbers[9]))+" | "+str(format('%02.0F' % numbers[10]))+" | "+str(format('%02.0F' % numbers[11]))+" | "+str(format('%02.0F' % numbers[12]))+" | "+str(format('%02.0F' % numbers[13]))+" | "+str(format('%02.0F' % numbers[14]))+" |    |")
        print("\t\t|    ----------------------------------------------------------------------------    |")
        print("\t\t|                                         /\\                                         |")
        print("\t\t|                                         ||                                         |")
        print("\t\t|                                         ||                                         |")
        print("\t\t|                                                                                    |")
        print("\t\t|                /-------------------------------------------------\\                 |")
        print("\t\t|                |    ODD(x2)    |    ZERO(x15)    |    EVEN(x2)   |                 |")
        print("\t\t|                |      (1)      |      (0)        |      (2)      |                 |")
        print("\t\t|                \\-------------------------------------------------/                 |")
        print("\t\t|                                                                                    |")
        print("\t\t\\------------------------------------------------------------------------------------/")

        #To equal the number 0 to number 14
        aux = numbers[0]
    
        numbers[0] = numbers[1]
        numbers[1] = numbers[2]
        numbers[2] = numbers[3]
        numbers[3] = numbers[4]
        numbers[4] = numbers[5]
        numbers[5] = numbers[6]
        numbers[6] = numbers[7]
        numbers[7] = numbers[8]
        numbers[8] = numbers[9]
        numbers[9] = numbers[10]
        numbers[10] = numbers[11]
        numbers[11] = numbers[12]
        numbers[12] = numbers[13]
        numbers[13] = numbers[14]
        numbers[14] = aux

        time.sleep(0.25)
        counter = counter + 1

    if betType == 0:
        if rolledNumber == 0:
            os.system("color 02")
            cashWon = bet * 15 
            print("\n\t\t You WON -> " + str(cashWon) + "£!")
            
        else:
            os.system("color 04")
            cashWon = 0
            print("\n\t\t You LOST -> "+ str(bet) +"£!")
            
    elif betType == 1:
        if (rolledNumber % 2) != 0:
            os.system("color 02")
            cashWon = bet * 2 
            print("\n\t\t You WON -> " + str(cashWon) + "£!")
            
        else:
            os.system("color 04")
            cashWon = 0
            print("\n\t\t You LOST -> "+ str(bet) +"£!")
            
    elif betType == 2:
        if (rolledNumber % 2) == 0:
            os.system("color 02")
            cashWon = bet * 2 
            print("\n\t\t You WON -> " + str(cashWon) + "£!")
            
        else:
            os.system("color 04")
            cashWon = 0
            print("\n\t\t You LOST -> "+ str(bet) +"£!")

    cashUpdate = cash + cashWon
    updateMoney(cashUpdate)
    input()

#Account Menu when not Logged
def notLoggedAccount():
    os.system("cls")
    os.system("color 06")
    mainImage()
    time.sleep(0.3)
    print("\n\n\t\t\t\t\t\t\t1 - Log In")
    time.sleep(0.3)
    print("\t\t\t\t\t\t\t2 - Register")
    time.sleep(0.3)
    print("\t\t\t\t\t\t\t3 - Back To Menu")

    accountOption = int(input("\n\n\t\t\t\tOption => "))
    if accountOption == 1:
        logIn("")
    elif accountOption == 2:
        register("")
    elif accountOption == 3:
        menu()
    else:
        notLoggedAccount()

#Account Menu when Logged
def loggedAccount():
    global loggedName
    
    os.system("cls")
    os.system("color 06")
    mainImage()
    time.sleep(0.3)
    print("\n\n\t\t\t\t\t\t\t1 - Change Username")
    time.sleep(0.3)
    print("\t\t\t\t\t\t\t2 - Change Password")
    time.sleep(0.3)
    print("\t\t\t\t\t\t\t3 - Log Out")
    time.sleep(0.3)
    print("\t\t\t\t\t\t\t4 - Back To Menu")

    accountOption = int(input("\n\n\t\t\t\tOption => "))
    if accountOption == 1:
        changeUsername()
    elif accountOption == 2:
        changePassword("")
    elif accountOption == 3:
        loggedName = ""
        os.system("cls")
        os.system("color 02")
        mainImage()
        print("\n\n\t\t\t\t\t\t\tSuccessful Logout!")
        input()
        menu()
    elif accountOption == 4:
        menu()
    else:
        loggedAccount()    

#Register
def register(name):
    os.system("cls")
    os.system("color 06")
    mainImage()
    
    if name == "":
        username = input("\n\n\t\t\t\t\t\tUsername => ")
        file = open("accounts.txt", "a")
        file.close()

        f = open("accounts.txt","r")
        fLength = len(f.readlines())
        f.close()
        
        f = open("accounts.txt","r")
        fLine = f.readlines()
        f.close()
        
        usernameFound = 0
    
        for counter in range(0,fLength,2):
            #Get the names from the file
            storedName = fLine[counter].split(" PSWD: ")

            #Searching for the Username
            if storedName[0] == username:
                usernameFound = 1
                break

        if usernameFound == 1:
            os.system("color 04")
            print("\n\t\t\t\t\t\tUsername Already in Use!")
            input()
            register("")
    else:
        print("\n\n\t\t\t\t\t\tUsername => " + name)
        username = name
        
    password = getpass.getpass("\t\t\t\t\t\tPassword => ")
    confirmPassword = getpass.getpass("\t\t\t\t\t\tConfirm Password => ")
    
    if password == confirmPassword:
        #ENCRYPTING PASSWORD
        encryptingPassword = hashlib.md5(password.encode()) 
        encryptedPassword = encryptingPassword.hexdigest()
            
        addAccount(username,encryptedPassword)
        notLoggedAccount()
    else:
        os.system("color 04")
        print("\n\t\t\t\t\t\tPasswords do not Match!")
        input()
        register(username)

#Add Account
def addAccount(usrname,passwrd):
    file = open("accounts.txt", "a")
    file.write(usrname + " PSWD: " + passwrd + " MONEY: 800\n\n")
    file.close()

#Log In
def logIn(name):
    os.system("cls")
    os.system("color 06")
    mainImage()

    if name == "":
        logUsername = input("\n\n\t\t\t\t\t\tUsername => ")
    else:
        print("\n\n\t\t\t\t\t\tUsername => " + name)
        logUsername = name
        
    logPassword = getpass.getpass("\t\t\t\t\t\tPassword => ")
        
    #ENCRYPTING PASSWORD
    encryptingLogPassword = hashlib.md5(logPassword.encode()) 
    encryptedLogPassword = encryptingLogPassword.hexdigest()
        
    processLogIn(logUsername,encryptedLogPassword)
    menu()

#Process Log In
def processLogIn(usrname,passwrd):
    global loggedName
    global userLine
    
    file = open("accounts.txt", "a")
    file.close()
    
    f = open("accounts.txt","r")
    fLength = len(f.readlines())
    f.close()

    f = open("accounts.txt","r")
    fLine = f.readlines()
    f.close()

    usernameFound = 0
    
    for counter in range(0,fLength,2):
        #Get the names from the file
        storedName = fLine[counter].split(" PSWD: ")

        #Searching for the Username
        if storedName[0] == usrname:
            usernameFound = 1
            break

    if usernameFound == 1:       
        #Get the Password
        storedPassword = storedName[1].split(" MONEY: ")
        if storedPassword[0] == passwrd:
            os.system("color 02")
            loggedName = usrname
            userLine = counter
            print("\n\t\t\t\t\t\tSuccessful Login!")
            input()
            menu()
        else:
            os.system("color 04")
            print("\n\t\t\t\t\t\tPassword is Not Correct!")
            input()
            logIn(usrname)
    else:
        os.system("color 04")
        print("\n\t\t\t\t\t\tUsername not Registered!")
        input()
        notLoggedAccount()    

#Change User Name
def changeUsername():
    global loggedName
    os.system("cls")
    os.system("color 06")
    mainImage()

    print("\n\n\t\t\t\t\t\tCurrent Username => " + loggedName)
    newUsername = input("\t\t\t\t\t\tNew Username => ")

    f = open("accounts.txt","r")
    fLength = len(f.readlines())
    f.close()
        
    f = open("accounts.txt","r")
    fLine = f.readlines()
    f.close()
        
    usernameFound = 0
    
    for counter in range(0,fLength,2):
        #Get the names from the file
        storedName = fLine[counter].split(" PSWD: ")

        #Searching for the Username
        if storedName[0] == newUsername:
            usernameFound = 1
            break

    if usernameFound == 1:
        os.system("color 04")
        print("\n\t\t\t\t\t\tUsername Already in Use!")
        input()
        changeUsername()
    else:
        oldUsername = fLine[userLine].split(" PSWD: ")
        oldUsername[0] = newUsername
        change = oldUsername[0] + " PSWD: " + oldUsername[1]

        file = open("accounts.txt", "w")
        file.close()
        file = open("accounts.txt", "a")
        
        for counter in range(0,fLength,2):
            if counter == userLine:
                file.write(change)
            else:
                file.write(fLine[counter])
            file.write("\n") 

        file.close()
        os.system("color 02")
        loggedName = newUsername
        print("\n\t\t\t\t\t\tSuccessful Username Change!")
        input()
        menu()

#Change Password
def changePassword(passCorrect):
    os.system("cls")
    os.system("color 06")
    mainImage()

    if passCorrect == "":
        currentPassword = getpass.getpass("\n\n\t\t\t\t\t\tCurrent Password => ")

        #ENCRYPTING PASSWORD
        encryptingCurrentPassword = hashlib.md5(currentPassword.encode()) 
        encryptedCurrentPassword = encryptingCurrentPassword.hexdigest()
    else:
        print("\n\n\t\t\t\t\t\tCurrent Password => ")
        encryptedCurrentPassword = passCorrect

    #Get the Password
    f = open("accounts.txt","r")
    fLength = len(f.readlines())
    f.close()
        
    f = open("accounts.txt","r")
    fLine = f.readlines()
    f.close()

    username = fLine[userLine].split(" PSWD: ")
    storedPassword = username[1].split(" MONEY: ")
    
    if storedPassword[0] == encryptedCurrentPassword:
        newPassword = getpass.getpass("\t\t\t\t\t\tNew Password => ")
        confirmNewPassword = getpass.getpass("\t\t\t\t\t\tConfirm New Password => ")
        
        if newPassword == confirmNewPassword:
            #ENCRYPTING PASSWORD
            encryptingNewPassword = hashlib.md5(newPassword.encode()) 
            encryptedNewPassword = encryptingNewPassword.hexdigest()

            storedPassword[0] = encryptedNewPassword
            change = loggedName + " PSWD: " + storedPassword[0] + " MONEY: " + storedPassword[1]

            file = open("accounts.txt", "w")
            file.close()
            file = open("accounts.txt", "a")
        
            for counter in range(0,fLength,2):
                if counter == userLine:
                    file.write(change)
                else:
                    file.write(fLine[counter])
                file.write("\n") 

            file.close()
            os.system("color 02")
            print("\n\t\t\t\t\t\tSuccessful Password Change!")
            input()
            menu()
        else:
            os.system("color 04")
            print("\n\t\t\t\t\t\tPasswords do not Match!")
            input()
            changePassword(encryptedCurrentPassword)
    else:
        os.system("color 04")
        print("\n\t\t\t\t\t\tPassword is Not Correct!")
        input()
        changePassword("")

#Money Update in file
def updateMoney(moneyUpdated):
    f = open("accounts.txt","r")
    fLength = len(f.readlines())
    f.close()
        
    f = open("accounts.txt","r")
    fLine = f.readlines()
    f.close()

    money = fLine[userLine].split(" MONEY: ")
    money[1] = str(moneyUpdated)
    change = money[0] + " MONEY: " + money[1]
    
    file = open("accounts.txt", "w")
    file.close()
    
    file = open("accounts.txt", "a")
    
    for counter in range(0,fLength,2):
        if counter == userLine:
            file.write(change)
            file.write("\n\n")
        else:
            file.write(fLine[counter])
            file.write("\n")         
        
    file.close()

#Get money
def getMoney():
    global cash
    
    f = open("accounts.txt","r")
    fLength = len(f.readlines())
    f.close()
        
    f = open("accounts.txt","r")
    fLine = f.readlines()
    f.close()

    money = fLine[userLine].split(" MONEY: ")

    convertInt = int(money[1])
    cash = convertInt
    
#Instructions
def about():
    os.system("cls")
    mainImage()
    print("\n\n\t\t\tThe roulette game is a game of luck!")
    print("\t\t\tFirst the player needs to Log In on an account or if don't have one, needs to Create one.")
    print("\t\t\tWhen the player creates an account, it starts with 800£.")
    print("\t\t\tThe player can change the username or the password.")    
    print("\t\t\tWhen the player bets on even or odd numbers, (if he wins) earns double of what he betted!")
    print("\t\t\tWhen the player bets on the number zero, (if he wins) earns fifteen  times of what he betted!")
    input("\n\n\t\t\tPress Enter key to exit...")
    menu()

#Exit
def exitGame():
    os.system("cls")
    print("\n\n\t\t\t\t\t\t******  *     * *******    ***")
    time.sleep(0.01)
    os.system("cls")
    print("\n\n\t\t\t\t\t\t******  *     * *******    ***")
    print("\t\t\t\t\t\t*     *  *   *  *          ***")
    time.sleep(0.01)
    os.system("cls")
    print("\n\n\t\t\t\t\t\t******  *     * *******    ***")
    print("\t\t\t\t\t\t*     *  *   *  *          ***")
    print("\t\t\t\t\t\t*     *   * *   *          *** ")
    time.sleep(0.01)
    os.system("cls")
    print("\n\n\t\t\t\t\t\t******  *     * *******    ***")
    print("\t\t\t\t\t\t*     *  *   *  *          ***")
    print("\t\t\t\t\t\t*     *   * *   *          *** ")
    print("\t\t\t\t\t\t******     *    *****      ***")
    time.sleep(0.01)
    os.system("cls")
    print("\n\n\t\t\t\t\t\t******  *     * *******    ***")
    print("\t\t\t\t\t\t*     *  *   *  *          ***")
    print("\t\t\t\t\t\t*     *   * *   *          *** ")
    print("\t\t\t\t\t\t******     *    *****      ***")
    print("\t\t\t\t\t\t*     *    *    *")
    time.sleep(0.01)
    os.system("cls")
    print("\n\n\t\t\t\t\t\t******  *     * *******    ***")
    print("\t\t\t\t\t\t*     *  *   *  *          ***")
    print("\t\t\t\t\t\t*     *   * *   *          *** ")
    print("\t\t\t\t\t\t******     *    *****      ***")
    print("\t\t\t\t\t\t*     *    *    *")
    print("\t\t\t\t\t\t*     *    *    *          ***")
    time.sleep(0.01)
    os.system("cls")
    print("\n\n\t\t\t\t\t\t******  *     * *******    ***")
    print("\t\t\t\t\t\t*     *  *   *  *          ***")
    print("\t\t\t\t\t\t*     *   * *   *          *** ")
    print("\t\t\t\t\t\t******     *    *****      ***")
    print("\t\t\t\t\t\t*     *    *    *")
    print("\t\t\t\t\t\t*     *    *    *          ***")
    print("\t\t\t\t\t\t******     *    *******    ***")

    print("\n\t\t\t\t\t\tThank you for Playing...")
    exit
    
#Main
def main():   
    os.system("color 06")
    menu()
    input()

main()
    
