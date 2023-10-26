students=[]
grades=[]
num1=0
while(True):
    temp_value=input()
    if temp_value=="Students":
        num1=1
    if num1==1:
        students.append(temp_value.split("~"))
    if temp_value=="Grades":
        num1=2
    if num1==2:
        grades.append(temp_value.split("~"))
    if temp_value=="EndOfInput":
        break
students=students[1:-1]
grades=grades[1:-1]
#print(students,grades,sep="\n")
dict1={"A":10,
"AB":9,
"B":8,
"BC":7,
"C":6,
"CD":5,
"D":4}
#print(students)
new_student_list=[]
for student in students:
    temporary=0
    count=0
    for grade in grades:
        if student[0]==grade[3]:
            count+=1
            temporary+=dict1[grade[4]]
    try:
        new_student_list.append([student[0],student[1],round((temporary/count),2)])
        #print([student[0],student[1],round((temporary/count),2)])
    except:
        new_student_list.append([student[0],student[1],0])
        #print([student[0],student[1],0])
new_student_list.sort(key=lambda x:x[0])
for i in new_student_list:
    a,b,c=i
    print(a,b,c,sep="~")
            
