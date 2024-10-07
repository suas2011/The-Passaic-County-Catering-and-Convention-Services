#Hall Menu
import mainmenu
import halltypes

def Hmenu():
    while True:
     print('Hall Menu')
     print('---------')
     print('1-Hall Menu for Deluxe Meal')
     print('2-Hall Menu for Standard Meal')
     print('3-Exit Hall Menu')
     choisehm=int(input('\nEnter Hall Menu Type: '))
     if choisehm==1:
       halltypes.Halltypes_D()
     elif choisehm==2:
       halltypes.Halltypes_S()
     elif choisehm==3:
           menu=mainmenu.MainMenu()
           menu.mainMenu()
     else:
       print('Invalid Hall Menu Choice entered! Reenter Please!')
