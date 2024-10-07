#Main Menu
import billmenu
import mealmenu
import hallmenu
import methods
import halltypes

class MainMenu:
    def mainMenu(self):
     #mychoices=bills.Bills()
     while True:
      try:
        print('\n=====================================================')
        print('|The Passaic County Catering and Convention Services|')
        print('=====================================================')
        print('1. The Number of Adults & Children Attending.')
        print('2. The number of children attending.')
        print('3. Choose Meal-type for Adults')
        print('4. Select Hall Type.')
        print('5. Produce Bill/Report.')
        print('6. Exit Program.')
        print('-----------------------------------------------------')
        
        choice=int(input('\nEnter your choice: '))

        if choice==1:
               methods.adultsAttending()

        elif choice==2:
               methods.childrenAttending()
               methods.WeekEnds()

        elif choice==3:
               mealmenu.mmenu()
            
        elif choice==4:
               hallmenu.Hmenu()

        elif choice==5:
               #mychoices.billReports()
            billmenu.billsMenu()
             
        elif choice==6:
               methods.quitProgram()
        else:
            print('invalid Choice entere! Enter Correct Number of Choice/s')

      except ValueError:
            print('\nOpps! You have not entered the correct digit range [1-6 only]\n')

    
