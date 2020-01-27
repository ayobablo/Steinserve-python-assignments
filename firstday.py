students=[{'name':'vincent','gender':'m','score':70},
{'name':'mercy','gender':'f','score':71},
{'name':'ayo','gender':'f','score':75},
{'name':'pelumi','gender':'f','score':73}]

def total_gender(students):
    male=0
    female=0
    for gender in students:
        if gender['gender']=='m':
            male=male+1
        elif gender['gender']=='f':
            female=female+1
    return (male , female)
           
print(total_gender(students))

def total_score(students):
    total_score=0
    for student in students:
        total_score=total_score + student['score']
    return (total_score)
print (total_score(students))

def total(students):
    total=0
    for name in students:
        total=total + 1
    return (total)
print(total(students))

def average_score(students):
    n=len(students)
    avg=total_score(students)/n
    return (avg)
print(average_score(students))
