#Meal Menu

import mealtypes
import mainmenu
import constants

def mmenu():
    while True:
     print('\n=====================')
     print('|  Adult Meal Type  |')
     print('=====================')
     print('D-Deluxe Meal  : $25.95')
     print('S-Standard Meal: $21.75')
     print('E-Exit Menu')

     constants.mealType=str(input('Enter Meal Type - Deluxe=D|Standard=S:'))
                                 
     if constants.mealType=='s' or constants.mealType=='S':
        constants.MTStandard='S'
        mealtypes.Standard()
           
     elif constants.mealType=='d' or constants.mealType=='D':
          constants.MTDeluxe='D'
          mealtypes.Deluxe()

     elif constants.mealType=='e' or constants.mealType=='E':
          menu=mainmenu.MainMenu()
          menu.mainMenu()
            
     else:
       print('Invalid Meal Type Selected [D-Deluxe | S-Standard]')



    
    
