#Meal Types

import constants

##from currency_symbols import CurrencySymbols
##dollar=CurrencySymbols.get_symbol('USD')
##

def Deluxe():
        print('You selected Deluxe Meal!')
        print('Your Meal Charges - $25.95\n')
        constants.deluxeCostAdults=constants.DELUXE_MEAL * constants.adultsAttending
        constants.childrenDMCost=(constants.childrenAttending*(constants.DELUXE_MEAL * 50)/100)
        constants.dgratuity=(constants.deluxeCostAdults + constants.childrenDMCost)*(constants.GRATUITY_RATE/100)
        print('\nDeluxe Adults Meal Cost            : ',"${:,.2f}".format(constants.deluxeCostAdults))
        print('Children Cost to be Paid           : ',"${:,.2f}".format(constants.childrenDMCost))
        print('Total Payable Cost for Deluxe Meal : ',"${:,.2f}".format(constants.deluxeCostAdults+constants.childrenDMCost))
        print('\nGratuity Generated on Cost of Food : ',"${:,.2f}".format(constants.dgratuity))
        
        

def Standard():
        print('You selected Standard Meal!')
        print('Your Meal Charges - $21.75')
        constants.standardCostAdults=constants.STANDARD_MEAL * constants.adultsAttending
        constants.childrenSMCost=(constants.childrenAttending*(constants.STANDARD_MEAL * 50)/100)
        #constants.sgratuity= (constants.standardCostAdults * constants.GRATUITY_RATE)/100
        constants.sgratuity=(constants.standardCostAdults + constants.childrenSMCost)*(constants.GRATUITY_RATE/100)
        
        print('\nStandard Adults Meal Cost            : ',"${:,.2f}".format(constants.standardCostAdults))
        print('Children Cost to be Paid             : ',"${:,.2f}".format(constants.childrenSMCost))
        print('Total Payable Cost for Standard Meal : ',"${:,.2f}".format(constants.standardCostAdults+constants.childrenSMCost))
        print('\nGratuity Generated on Cost of Food   : ',"${:,.2f}".format(constants.sgratuity))
        
