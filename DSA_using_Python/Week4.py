    

def histogram(l):
    list1=l[0:]
    final_list=[]
    set1=set(list1)
    set1=sorted(set1)
    for i in set1:
        count=list1.count(i)
        final_list.append(tuple([i,count]))
    final_list=sorted(final_list,key=lambda x:x[1])

    return final_list
    
#################################################################################

def transcript(coursedetails, studentdetails, grades):
    course_map = {code: name for code, name in coursedetails}
    student_map = {roll: name for roll, name in studentdetails}
    student_grades = {}
    for roll, code, grade in grades:
        if roll not in student_grades:
            student_grades[roll] = []
        student_grades[roll].append((code, course_map[code], grade))
    transcript_list = []
    for roll in sorted(student_grades.keys()):
        name = student_map[roll]
        sorted_grades = sorted(student_grades[roll], key=lambda x: x[0]) 
        transcript_list.append((roll, name, sorted_grades))
    
    return transcript_list

