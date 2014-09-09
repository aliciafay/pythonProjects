#Alicia Leslie
#Using While Loop

numbershares=0.0
purchaseprice=0.0
sellingprice=0.0
commission=0.0
count=0

name=input("Enter your name:")
numbershares=float(input("Enter Number of Shares or -999 to quit:"))
while numbershares!=-999:
    purchaseprice=float(input("Enter Purchase Price:"))
    sellingprice=float(input("Enter Selling price:"))
    commission=float(input("Enter Commission:"))
    
    count=count+1

    amountpaid=numbershares*purchaseprice
    amountcommission=amountpaid*commission
    amountsold=numbershares*sellingprice
    amountcommissionsold=amountsold*commission
    profit=(amountsold-amountcommissionsold)-(amountpaid+amountcommission)

    
    print()
    print("The information for stock number",count)
    print("--------------------------------------")
    print("Amount paid for the stock:      $",format(amountpaid,'10,.2f'))
    print("Commission paid on the purchase:$",format(amountcommission,'10,.2f'))
    print("Amount the stock sold for:      $",format(amountsold,'10,.2f'))
    print("Commission paid on the sale:    $",format(amountcommissionsold,'10,.2f'))
    print("Profit(or loss if negative):    $",format(profit,'10,.2f'))

    numbershares=int(input("Enter Number of Shares or -999 to quit"))
