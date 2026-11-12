#fictional student dataset for CUL-CYB 371
students = [
    ['V01-STU001', 'Information Technology', 400, 89, 52],
    ['V01-STU002', 'Cyber Security', 300, 80, 71],
    ['V01-STU003', 'Software Engineering', 300, 93, 76],
    ['V01-STU004', 'Software Engineering', 300, 96, 79],
    ['V01-STU005', 'Cyber Security', 400, 81, 75],
    ['V01-STU006', 'Cyber Security', 300, 58, 58],
    ['V01-STU007', 'Software Engineering', 100, 83, 58],
    ['V01-STU008', 'Information Technology', 100, 93, 89],
    ['V01-STU009', 'Information Technology', 300, 62, 94],
    ['V01-STU010', 'Cyber Security', 300, 72, 53],
    ['V01-STU011', 'Cyber Security', 300, 83, 79],
    ['V01-STU012', 'Computer Science', 100, 67, 67],
    ['V01-STU013', 'Computer Science', 400, 60, 73],
    ['V01-STU014', 'Cyber Security', 200, 59, 57],
    ['V01-STU015', 'Computer Science', 300, 72, 66],
    ['V01-STU016', 'Computer Science', 100, 62, 59],
    ['V01-STU017', 'Software Engineering', 200, 87, 57],
    ['V01-STU018', 'Cyber Security', 300, 91, 66]
]

headings = ['Student ID', 'Department', 'Level', 'Attendance Percentage', 'Average Examination Score']

print("FICTIONAL STUDENT DATASET")
print("-" * 105)
print(f"{'Student ID':<14} {'Department':<25} {'Level':<8} {'Attendance':<14} {'Exam Score'}")

for student in students:
    print(f"{student[0]:<14} {student[1]:<25} {student[2]:<8} {str(student[3]) + '%':<14} {str(student[4]) + '%'}")

print("-" * 105)
print("Total students:", len(students))
print("Dataset successfully generated")
