Employee File Management
Problem Statement

Develop a small Python application that maintains employee information. Employee details are stored in a file and later read to generate a simple report:

Store Employee ID, Name, Role and Salary in employees.txt
Read the employee information from the file
Display all employees
Show employees whose salary is greater than ₹50,000
Find the employee with the highest salary
Count how many employees belong to each role
Handle the case where the file does not exist
Approach / Logic Used
Create an Employee class with employee_id, name, role and salary, and a display_details() method to print them.
add_employee() appends one employee to employees.txt as a comma-separated line. Opening the file in append mode also creates it if it does not exist.
read_employees() opens the file, skips blank lines, splits each line on commas and creates an Employee object for it. If the file is missing, it catches FileNotFoundError and prints an error message instead of crashing.
Display every employee using display_details() in a for loop.
find_employees_above_salary() collects employees whose salary is above the threshold (₹50,000).
find_highest_salary() compares salaries in a loop and keeps the highest-paid employee.
find_employees_by_role() counts employees per role in a dictionary. The result is printed in alphabetical order of role.

All file operations use a context manager (with open()), so the file is closed automatically.

How to Run
Install Python 3.6 or later.
Open a terminal in the project folder.
Run:
bash
   python employee_manager.py

On Windows, if python is not recognised, use py employee_manager.py.

Make sure employees.txt is in the same folder as the script. If it is missing, the program prints an error and shows no records.

Sample Input

Contents of employees.txt (Employee ID, Name, Role, Salary):

101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000
Sample Output
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

If employees.txt does not exist when it is read:

Error: employees.txt was not found.