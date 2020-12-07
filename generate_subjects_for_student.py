import random

subjects = ["English", "Maths", "Programming", "Physics", "Music"]
assignments = [["1", "2"], ["3", "4"], ["5"], ["6", "7", "8"], ["9"]]
print_subjects = []
all_assignments = []
for i in range(0, 200):
    nr_of_classes = random.randrange(1, len(subjects) + 1)
    student_classes = []
    student_assignments = []
    while len(student_classes) != nr_of_classes:

        random_subject = random.randrange(0, len(subjects))
        if subjects[random_subject] in student_classes:
            continue
        else:
            student_classes.append(subjects[random_subject])
            student_assignments.append(assignments[random_subject])

    all_assignments.append(student_assignments)
    #print(student_classes)
    

    
    # Izveido string, kas satures visus subjects
    all_classes = ""
    for k in range(0, len(student_classes)):

        all_classes = all_classes + student_classes[k]
        if k != len(student_classes) - 1:
            all_classes = all_classes + ":"
        else:
            all_classes = all_classes + "\n"
            
    print_subjects.append(all_classes)

print(all_assignments[1])
print(print_subjects[1])


with open('./grades.csv', 'w') as f:
    f.write("student_id,assignment_id,value\n")
    for i in range(0, 200):
        for assignment_list in all_assignments[i]:
            for assignment in assignment_list:
                wr = str(i + 1) + "," + assignment + "," + str(random.randrange(1, 11)) + "\n"
                f.write(wr)

    f.close()

with open('./student_subjects.csv', 'w') as f: 

    for c in print_subjects:
        f.write(c) 
    
    f.close()


        
