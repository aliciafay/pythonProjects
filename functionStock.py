#alicia leslie
#program 1 using functions

def load():
    #NAME=input("enter name of stock")
    NUM_SHARES=int(input("Enter number of shares:"))
    PURCHASE_PRICE=int(input("Enter purchase price:"))
    SELLING_PRICE=int(input("Enter selling price:"))
    COMMISSION_RATE=float(input("Enter Commission:"))
    return NUM_SHARES,PURCHASE_PRICE,SELLING_PRICE,COMMISSION_RATE

def calc(NUM_SHARES,PURCHASE_PRICE,SELLING_PRICE,COMMISSION_RATE):
    amountpaidforstock=0.0
    purchasecommission=0.0
    totalpaid=0.0
    stocksoldfor=0.0
    sellingcommission=0.0
    totalreceived=0.0
    profitorloss=0.0

    amountpaidforstock=NUM_SHARES*PURCHASE_PRICE
    purchasecommission=amountpaidforstock*COMMISSION_RATE
    totalpaid=amountpaidforstock+purchasecommission
    stocksoldfor=NUM_SHARES*SELLING_PRICE
    sellingcommission=COMMISSION_RATE*stocksoldfor
    totalreceived=stocksoldfor-sellingcommission
    profitorloss=totalreceived-totalpaid
    return amountpaidforstock,purchasecommission,stocksoldfor,sellingcommission,profitorloss


def output(NAME,amountpaidforstock,purchasecommission,\
           stocksoldfor,sellingcommission,profitorloss):
    print("\n\nStock Name:",NAME)
    print("Amount Paid for Stock: $",format(amountpaidforstock,'10,.2f'))
    print("Purchase Commission: $",format(purchasecommission,'10,.2f'))
    print("Amount Stock Sold for: $",format(stocksoldfor,'10,.2f'))
    print("Selling Commission: $",format(sellingcommission,'10,.2f'))
    print("Profit(or loss if negative): $",format(profitorloss,'10,.2f'))

def main():
    totprofit=0
    NAME=input("Enter name of stock or -999 to quit:")
    while NAME!="-999":
        NUM_SHARES,PURCHASE_PRICE,SELLING_PRICE,COMMISSION_RATE=load()

        (amountpaidforstock,purchasecommission,stocksoldfor,sellingcommission,\
        profitorloss)=calc(NUM_SHARES,PURCHASE_PRICE,SELLING_PRICE,COMMISSION_RATE)
        
        output(NAME,amountpaidforstock,purchasecommission,\
           stocksoldfor,sellingcommission,profitorloss)
        totprofit=totprofit+profitorloss
        print()
        NAME=input("Enter name or -999 to quit:")
        print()
    print("Total profit or loss:$",format(totprofit,'10,.2f'))

main()
