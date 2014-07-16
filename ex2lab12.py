#Lab 12, Test 2
#alicia leslie

num_stud=int(input("How many students?"))
num_scores=int(input("How many scores?"))

for student in range(num_stud):
    total=0
    print("Student number",student+1)
    print("............")
    for test_num in range(num_scores):
        print("Test number",test_num+1,end='')
        score=float(input())
        total=total+score
    avg=total/num_scores
    print("The average for student number",\
          student+1,"is:",format(avg,'.1f'))
