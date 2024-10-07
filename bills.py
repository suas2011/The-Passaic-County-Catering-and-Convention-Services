#Bills

import sys
import math
import constants
import mealtypes
import halltypes
import random
import methods

##from currency_symbols import CurrencySymbols
##dollar=CurrencySymbols.get_symbol('USD')


#class Bills:

       
##    def billReports(self):
##        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
##        print('Caswell Catering and Convention Services')
##        constants.InvoiceNo=random.randint(100,999)
##        #print(constants.InvoiceNo)
##        print('       Final Bill | Invoice#:',constants.InvoiceNo)
##        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/\n')
##        print('Number of Adult:','{:5d}'.format(constants.adultsAttending))
##        print('Number of Children:','{:5d}'.format(constants.childrenAttending))
##        print('Gratuity: ',constants.GRATUITY_RATE,'%')
##        print('Weekend: ',constants.Weekend)

def StandardMealBill():

        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
        print('Caswell Catering and Convention Services')
        constants.InvoiceNo=random.randint(100,999)
        print('       Final Bill | Invoice#:',constants.InvoiceNo)
        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/\n')
        print('Number of Adult:%d','{:5d}'.format(constants.adultsAttending,'>10.2f'))
        print('Number of Children:%d','{:5d}'.format(constants.childrenAttending,'>10.2f'))
        print('Gratuity:%d ',constants.GRATUITY_RATE,'%')
        print('Weekend:%s ',constants.Weekend)
        print('Cost per standard meal for adult:%d ',"${:}".format(constants.STANDARD_MEAL))
        print('Cost per standard meal for child:%d ',"${:}".format(round(constants.STANDARD_MEAL*50/100,2)))
        print('------------------------------------------')
        print('Total cost for adult meals:       ',"${:}".format(constants.standardCostAdults,'>10.2f'))
        print('Total cost for child meals:       ',"${:}".format(constants.childrenSMCost,'>10.2f'))
        print('\nTotal food cost:                ',"${:}".format(constants.standardCostAdults+constants.childrenSMCost,'>10.2f'))
        print('------------------------------------------')
        print('Gratuity:', constants.sgratuity)
        print('Hall Type Room Fee:',constants.HallTypes)
        constants.SweekendCharges=constants.standardCostAdults+constants.childrenSMCost
        print('Weekend Charges: ',round((constants.SweekendCharges*10)/100,2))
        print('Taxes: ')
        print('------------------------------------------')
        print('Subtotal: ')
        print('\nLess Deposit: ')
        print('Less Speedy Payment: ')
        print('\nBalance Due: ')
        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
        print('   Thank you for using Caswell Catering')



def DeluxeMealBill():
        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
        print('Caswell Catering and Convention Services')
        constants.InvoiceNo=random.randint(100,999)
        print('       Final Bill | Invoice#:',constants.InvoiceNo)
        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/\n')
        print('Number of Adult:','{:5d}'.format(constants.adultsAttending))
        print('Number of Children:','{:5d}'.format(constants.childrenAttending))
        print('Gratuity: ',constants.GRATUITY_RATE,'%')
        print('Weekend: ',constants.Weekend)
        print('Cost per deluxe meal for adult: ',"${:}".format(constants.DELUXE_MEAL))
        print('Cost per deluxe meal for child: ',"${:}".format(round(constants.DELUXE_MEAL*50/100,2)))
        print('------------------------------------------')
        print('Total cost for adult meals:       ',"${:}".format(constants.deluxeCostAdults))
        print('Total cost for child meals:       ',"${:}".format(constants.childrenDMCost))
        print('\nTotal food cost:                ',"${:}".format(constants.deluxeCostAdults+constants.childrenDMCost))
        print('------------------------------------------')
        print('Gratuity:', constants.dgratuity)
        print('Hall Type Room Fee:',constants.HallTypes)
        constants.DweekendCharges=constants.deluxeCostAdults+constants.childrenDMCost
        print('Weekend Charges: ',round((constants.DweekendCharges*10)/100),2)
        print('Taxes: ')
        print('------------------------------------------')
        print('Subtotal: ')
        print('\nLess Deposit: ')
        print('Less Speedy Payment: ')
        print('\nBalance Due: ')
        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
        print('   Thank you for using Caswell Catering')
        
        
