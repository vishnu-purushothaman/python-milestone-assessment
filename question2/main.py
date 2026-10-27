import os

# Find employees.txt in the same folder as this script
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "employees.txt")
SALARY_THRESHOLD = 50000


class Employee:
    def __init__(self, employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = salary

    def display_details(self):
        print(f"{self.employee_id} - {self.name} - {self.role} - ₹{self.salary}")


def add_employee(employee):
    # "a" mode adds the new record at the end of the file
    with open(FILE_PATH, "a", encoding="utf-8") as file:
        file.write(f"{employee.employee_id},{employee.name},{employee.role},{employee.salary}\n")


def read_employees():
    employees = []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip() == "":
                    continue  # skip empty lines
                # Split each line into its four parts
                emp_id, name, role, salary = line.strip().split(",")
                employees.append(Employee(int(emp_id), name, role, int(salary)))
    except FileNotFoundError:
        print("Error: employees.txt was not found.")
    return employees


def find_employees_above_salary(employees, threshold):
    result = []
    for emp in employees:
        if emp.salary > threshold:
            result.append(emp)
    return result


def find_highest_salary(employees):
    highest = employees[0]
    for emp in employees:
        if emp.salary > highest.salary:
            highest = emp
    return highest


def find_employees_by_role(employees):
    role_count = {}
    for emp in employees:
        if emp.role in role_count:
            role_count[emp.role] += 1
        else:
            role_count[emp.role] = 1
    return role_count


def main():
    employees = read_employees()

    if len(employees) == 0:
        print("No employee records to display.")
        return

    print("===== Employee Details =====\n")
    for emp in employees:
        emp.display_details()

    print(f"\n===== Employees with Salary > {SALARY_THRESHOLD} =====\n")
    for emp in find_employees_above_salary(employees, SALARY_THRESHOLD):
        print(f"{emp.name} - ₹{emp.salary}")

    print("\nHighest Paid Employee:")
    top = find_highest_salary(employees)
    print(f"{top.name} - ₹{top.salary}")

    print("\nEmployee Count by Role:")
    role_counts = find_employees_by_role(employees)
    for role in sorted(role_counts):
        print(f"{role}: {role_counts[role]}")


main()