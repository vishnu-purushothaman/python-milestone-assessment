# Employee File Management

## Problem Statement

Develop a small Python application that maintains employee information. Employee details are stored in a file and later read to generate a simple report.

### Requirements

- Store Employee ID, Name, Role, and Salary in `employees.txt`
- Read employee information from the file
- Display all employees
- Show employees whose salary is greater than ₹50,000
- Find the employee with the highest salary
- Count how many employees belong to each role
- Handle the case where the file does not exist

## Approach / Logic Used

- Create an `Employee` class with `employee_id`, `name`, `role`, and `salary` attributes.
- Add a `display_details()` method to print the employee information.
- Use `add_employee()` to append one employee record to `employees.txt` as a comma-separated line.
- Use `read_employees()` to open the file, skip blank lines, split each line on commas, and create an `Employee` object for each record.
- Catch `FileNotFoundError` and print a clear error message instead of crashing.
- Display every employee using `display_details()` in a loop.
- Use `find_employees_above_salary()` to collect employees whose salary exceeds the threshold.
- Use `find_highest_salary()` to compare salaries and keep the highest paid employee.
- Use `find_employees_by_role()` to count employees by role and print the results in alphabetical order.
- Use a context manager (`with open(...)`) so files are automatically closed.

## How to Run

1. Install Python 3.6 or later.
2. Open a terminal in the project folder.
3. Run the application:

```bash
python main.py
```

On Windows, if `python` is not recognized, use:

```bash
py main.py
```

> Make sure `employees.txt` is in the same folder as the script. If it is missing, the program prints an error and shows no records.

## Sample Input

Contents of `employees.txt`:

```text
101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000
```

## Sample Output

```text
===== Employee Details =====

101 - Rahul - Python Developer - ₹50000
102 - Anjali - Tester - ₹45000
103 - John - Developer - ₹60000
104 - Priya - Tester - ₹48000

===== Employees with Salary > 50000 =====

John - ₹60000

Highest Paid Employee:
John - ₹60000

Employee Count by Role:
Developer: 1
Python Developer: 1
Tester: 2
```

If `employees.txt` does not exist when it is read:

```text
Error: employees.txt was not found.
```