#Methods
#All functional Methods are declare and defined here

import sys
import constants
import mealtypes
import halltypes
import random

def adultsAttending():
    constants.adultsAttending=int(input('Total number of Adults Attending: '))
        
def childrenAttending():
    constants.childrenAttending=int(input('Total Number of Children attending: '))
                
def quitProgram():
    print('Thanks for using The Passaic County Catering and Convention Services!') 
    sys.exit(0)
    
def WeekEnds():
    constants.Weekend=str(input('Enter Weekend [Y/N]: '))

def genInvoiceNo():
    constants.InvoiceNo=random.randint(100,999)
    print(constants.InvoiceNo)
