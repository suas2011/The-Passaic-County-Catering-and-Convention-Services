#Global Variables - constants
#Constants defined below:

#General Variables
deluxeCostAdults=0
adultsAttending=0
childrenAttending=0
childrenSMCost=0
dgratuity=0
InvoiceNo=0
childrenDMCost=0
standardCostAdults=0
sgratuity=0
HSMCost=0  #Half Standard Meal Cost $21.75*50/100
HDMCost=0  #Half Deluxe Meal Cost   $25.95*50/100

#used to store character value as 'S' and 'D'
MTStandard='S'
MTDeluxe='D'
HallTypes=['A','B','C','H']
DeluxeHall_A_Cost =0
DeluxeHall_B_Cost =0
DeluxeHall_C_Cost =0
DeluxeHall_H_Cost =0

StandardHall_A_Cost =0
StandardHall_B_Cost =0
StandardHall_C_Cost =0
StandardHall_H_Cost =0


#Meal Types:

DELUXE_MEAL=25.95       #$
STANDARD_MEAL=21.75     #$

#Children food cost 50% of Adult meal cost.
CHILDREN_FOOD_COST=50   #%

#Gratuity
GRATUITY_RATE=20

#Surcharge 10% on Food Cost, If the catering is on Weekend
SURCHARGE=10

#Sales Tax:
SALES_TAX=6.875

#HallTypes charges in $:
HALL_A=1000
HALL_B=850
HALL_C=750
HALL_H=0  # is home

#Weekends
Weekend=''
SweekendCharges=0
DweekendCharges=0
        
#Bill Speedy DiscountS if paid within 10 days
BILL_LESSTHAN1000discount=2     #%
BILL_LESSTHAN2000discount=4     #%
BILL_LESSTHAN5000discount=5     #%
BILL_GREATERTHAN5000discount=7  #%

#Order Deposit
DEPOSIT=0

#Speedy Payment
SpeedyPayment=' ' #'Yes'| 'No', y/n



    

