#Alicia Leslie

numbershares=0.0
purchaseprice=0.0
sellingprice=0.0
commission=0.0

name=input("Enter your name:")
numbershares=float(input("Enter Number of shares:"))
purchaseprice=float(input("Enter Purchase Price:"))
sellingprice=float(input("Enter Selling price:"))
commission=float(input("Enter Commission:"))

amountpaid=numbershares*purchaseprice
amountcommission=amountpaid*commission
amountsold=numbershares*sellingprice
amountcommissionsold=amountsold*commission
profit=(amountsold-amountcommissionsold)-(amountpaid+amountcommission)

print("Amount paid for the stock:$",format(amountpaid,'10,.2f'))
print("Commission paid on the purchase:$",format(amountcommission,'10,.2f'))
print("Amount the stock sold for:$",format(amountsold,'10,.2f'))
print("Commission paid on the sale:$",format(amountcommissionsold,'10,.2f'))
print("Profit(or loss if negative):$",format(profit,'10,.2f'))


