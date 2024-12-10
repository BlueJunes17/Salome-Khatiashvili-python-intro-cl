import json
import os

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = int(salary)  

class Department:
    def __init__(self, name, description, employees):
        self.name = name
        self.description = description
        self.employees = employees

    def average(self):
        if not self.employees:
            return 0  #თუ თანამშრომლები არ არიან
        return sum(emp.salary for emp in self.employees) / len(self.employees)

    def max(self):
        if not self.employees:
            return 0
        return max(emp.salary for emp in self.employees)

    def min(self):
        if not self.employees:
            return 0
        return min(emp.salary for emp in self.employees)

    def positions(self):
        position_counts = {}
        for emp in self.employees:
            position_counts[emp.position] = position_counts.get(emp.position, 0) + 1
        return position_counts

def read_json_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file")
        return None


def main():
    file_path = 'data.json'
    data = read_json_file(file_path)
    if not data:
        return

    departments = []
    for dept_key, dept_data in data.items():
        employees = [Employee(emp['name'], emp['position'], emp['salary']) for emp in dept_data.get('employees', [])]
        department = Department(dept_data['name'], dept_data['description'], employees)
        departments.append(department)

    for dept in departments:
        print(f"Department: {dept.name}")
        print(f"Description: {dept.description}")
        print(f"Average salary: {dept.average():.2f}")
        print(f"Max salary: {dept.max()}")
        print(f"Min salary: {dept.min()}")
        print(f"Positions: {dept.positions()}")
        print("-" * 40)

if __name__ == '__main__':
    main()
