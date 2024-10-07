#Methods Standard and Deluxe

import constants

def Deluxe():
        print('You selected Deluxe Meal!')
        print('Your Meal Charges - $25.95\n')
        constants.deluxeCostAdults=constants.DELUXE_MEAL * constants.adultsAttending
        constants.dgratuity=(constants.deluxeCostAdults *  constants.GRATUITY_RATE)/100
        constants.childrenDMCost=(constants.deluxeCostAdults * 50)/100.
        print('\nDeluxe Adults Meal Cost            : ',"${:,.2f}".format(constants.deluxeCostAdults))
        print('Children Cost to be Paid           : ',"${:,.2f}".format(constants.childrenDMCost))
        print('Total Payable Cost for Deluxe Meal : ',"${:,.2f}".format(constants.deluxeCostAdults+constants.childrenDMCost))
        print('\nGratuity Generated on Cost of Food : ',"${:,.2f}".format(constants.dgratuity))
             
        #Deluxe Hall Types defined here'''

        print('\n===================')
        print('|Hall - A $1000.00|')
        print('|Hall - B $ 850.00|')
        print('|Hall - C $ 750.00|')
        print('|Hall - H $   0.00|') #is home
        print('===================\n')
        
        hallType_d=input('Enter Hall Type A|B|C|H :')
                         
        if hallType_d == 'a' or hallType_d == 'A':
           print('You selected Hall Type A!')
           print('Your Hall-A Charges - $1000.00')
           constants.DeluxeHall_A_Cost = constants.HALL_A+constants.deluxeCostAdults + constants.childrenDMCost
           print('\nTotal Deluxe Cost with Hall-A: ',"${:,.2f}".format(constants.DeluxeHall_A_Cost))

        elif hallType_d=='b' or hallType_d=='B':
           print('You selected Hall Type B!')
           print('Your Hall-B Charges - $850.00')
           constants.DeluxeHall_B_Cost = constants.HALL_B + constants.deluxeCostAdults + constants.childrenDMCost
           print('\nTotal Deluxe Cost with Hall-A: ',"${:,.2f}".format(constants.DeluxeHall_B_Cost))

        elif hallType_d=='c' or hallType_d=='C':
           print('You selected Hall Type C!')
           print('Your Hall-C Charges - $750.00')
           constants.DeluxeHall_C_Cost = constants.HALL_C + constants.deluxeCostAdults + constants.childrenDMCost
           print('\nTotal Deluxe Cost with Hall-A: ',"${:,.2f}".format(constants.DeluxeHall_C_Cost))

        elif hallType_d=='h' or hallType_d=='H':
           print('You selected Hall Type H!')
           print('Your Hall-H is a Home, Charges - $0.00!')
           constants.DeluxeHall_H_Cost = constants.HALL_H + constants.deluxeCostAdults + constants.childrenDMCost
           print('\nTotal Deluxe Cost with Hall-A: ',"${:,.2f}".format(constants.DeluxeHall_H_Cost))

        else:
           print('Invalid Hall Types Entered! Please Enter the correct letters for Hall Types.')



def Standard():
        print('You selected Standard Meal!')
        print('Your Meal Charges - $21.75')
        constants.standardCostAdults=constants.STANDARD_MEAL * constants.adultsAttending
        constants.sgratuity= (constants.standardCostAdults * constants.GRATUITY_RATE)/100
        constants.childrenSMCost=constants.standardCostAdults * 50 /100.
        print('\nStandard Adults Meal Cost            : ',"${:,.2f}".format(constants.standardCostAdults))
        print('Children Cost to be Paid             : ',"${:,.2f}".format(constants.childrenSMCost))
        print('Total Payable Cost for Standard Meal : ',"${:,.2f}".format(constants.standardCostAdults+constants.childrenSMCost))
        print('\nGratuity Generated on Cost of Food   : ',"${:,.2f}".format(constants.sgratuity))

        ''' Standard Hall Types defined here'''

        print('\n===================')         
        print('|Hall - A $1000.00|')
        print('|Hall - B $ 850.00|')
        print('|Hall - C $ 750.00|')
        print('|Hall - H $   0.00|') #is home
        print('===================\n')
        
        hallType_s=input('Enter Hall Type A|B|C|H :')
                         
        if hallType_s == 'a' or hallType_s == 'A':
           print('You selected Hall Type A!')
           print('Your Hall-A Charges - $1000.00')
           constants.StandardHall_A_Cost = constants.HALL_A+constants.standardCostAdults + constants.childrenSMCost
           print('\nTotal Deluxe Cost with Hall-A: ',"${:,.2f}".format(constants.StandardHall_A_Cost))

        elif hallType_s=='b' or hallType_s=='B':
           print('You selected Hall Type B!')
           print('Your Hall-B Charges - $850.00')
           constants.StandardHall_B_Cost = constants.HALL_B + constants.standardCostAdults + constants.childrenSMCost
           print('\nTotal Deluxe Cost with Hall-A: ',"${:,.2f}".format(constants.StandardHall_B_Cost))

        elif hallType_s=='c' or hallType_s=='C':
           print('You selected Hall Type C!')
           print('Your Hall-C Charges - $750.00')
           constants.StandardHall_C_Cost = constants.HALL_C + constants.standardCostAdults + constants.childrenSMCost
           print('\nTotal Deluxe Cost with Hall-A: ',"${:,.2f}".format(constants.StandardHall_C_Cost))

        elif hallType_s=='h' or hallType_s=='H':
           print('You selected Hall Type H!')
           print('Your Hall-H is a Home, Charges - $0.00!')
           constants.StandardHall_H_Cost = constants.HALL_H + constants.standardCostAdults + constants.childrenSMCost
           print('\nTotal Deluxe Cost with Hall-A: ',"${:,.2f}".format(constants.StandardHall_H_Cost))

        else:
           print('Invalid Hall Types Entered! Please Enter the correct letters for Hall Types.')


def GenerateInvoice():
           randInvoice=random.randint(100,999)
           print('Your Invoice #: ', randInvoice)
