#alicia
#read the employees.txt

def main():
    emp_file=open('employees.txt','r')
    name=emp_file.readline()
    while name!='':
        name=emp_file.readline()
        id_num=emp_file.readline()
        dept=emp_file.readline()
        name=name.rstrip('\n')
        id_num=id_num.rstrip('\n')
        dept=dept.rstrip('\n')
        print('name:',name)
        print('id:',id_num)
        print('dept:',dept)
        print()
        name=emp_file.readline()
    emp_file.close()
main()
        
