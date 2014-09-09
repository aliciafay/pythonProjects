#alicia
#4-10
#Program to calculate gross pay for each employee

num_employee=6

def main():
    #create a list to hold employee hours
    hours=[0]*num_employee
    for index in range(num_employee):
        print("Enter the hours worked by employee:",\
              index+1,":",sep='',end='')
        hours[index]=float(input())
    pay_rate=float(input("Enter the hourly pay rate:"))
    #display each employees gross pay
    for index in range(num_employee):
        gross_pay=hours[index]*pay_rate
        print("Gross pay for employee",index+1,":$",\
              format(gross_pay,',.2f'),sep='')
main()
