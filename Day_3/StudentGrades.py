students = [("Goutham", [95, 100, 98, 92]),
            ("Swag", [60, 65, 70, 75]),
            ("Aashi", [40, 45, 50, 55]),
            ("valli", [85, 90, 78, 92])]

def Grade_Track(students):
    return {name: grades for name, grades in students}

def Avg(student_name, grade_dict):
    return sum(grade_dict[student_name]) / len(grade_dict[student_name])

def Topper(grade_dict):
    return max(grade_dict, key=lambda student: sum(grade_dict[student]) / len(grade_dict[student]))

def Pass_Students(grade_dict):
    return sum(1 for grades in grade_dict.values() if sum(grades) / len(grades) >= 50)

grade_tracker = Grade_Track(students)

print("Dictionary of students with grades:", grade_tracker)
print("\nAvg grade for Goutham:", Avg("Goutham", grade_tracker))
print("Highest Avg:", f"\"{Topper(grade_tracker)}\"")
print("Passed students: ", Pass_Students(grade_tracker))
