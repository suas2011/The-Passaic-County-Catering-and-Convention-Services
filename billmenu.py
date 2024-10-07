#Bill Menu
import bills
import mainmenu


def billsMenu():
   while True:
    print('\n1-Deluxe Bill')
    print('2-Standard Bill')
    print('3-Exit Bill Menu')
    billchoice=int(input('Enter Deluxe or Standard Bill Type: '))
    
    if billchoice==1:
        bills.DeluxeMealBill()
    elif billchoice==2:
        bills.StandardMealBill()
    elif billchoice==3:
        menu=mainmenu.MainMenu()
        menu.mainMenu()
    else:
        print('Invalid Bill Type entered!')
