#Alicia Leslie
#Declare Variables

purchase=0.0
StateTax=0.0
CountyTax=0.0
TotalTax=0.0
TotalSale=0.0
STATE_TAX_RATE=0.04
COUNTY_TAX_RATE=0.02

purchase=float(input("Enter the amount of purchase:"))

StateTax=purchase*STATE_TAX_RATE
CountyTax=purchase*COUNTY_TAX_RATE
TotalTax=StateTax+CountyTax
TotalSale=purchase+TotalTax

print("Purchase Amount:",format(purchase,'.2f'))
print("State Tax:",format(StateTax,'.2f'))
print("County Tax:",format(CountyTax,'.2f'))
print("Total Tax:",format(TotalTax,'.2f'))
print("The Total Sales:",format(TotalSale,'.2f'))
