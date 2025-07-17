student=[{'student1':[50,60,70,80]},{'student2':[60,50,80,65]},{'student3':[25,45,65,75]},{'student4':[78,49,95,84]},{'student5':[76,43,44,67]}]
marks=[]

marks.append(student[0]['student1'])
print(marks)

for i in student:
    for j in i:
        print()
print()
