employees = [
    {"name": "Nani", "salary": 99000, "ratings": 5},
    {"name": "Swag", "salary": 48000, "ratings": 3},
    {"name": "Kapil", "salary": 20000, "ratings": 2}
]

def final_salary(employee):
    salary = employee["salary"]
    
    if employee["ratings"] >= 4:
        salary *= 1.10
    elif employee["ratings"] == 3:
        salary *= 1.05
    else:
        salary *= 0.97
    
    employee["salary"] = round(salary, 2)
    return employee

updated_employees = list(map(final_salary, employees))
print(updated_employees)



