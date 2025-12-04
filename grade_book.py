"""
GradeBook Analyzer
Name: <Your Name>
Date: <DD-MM-YYYY>
"""

import csv
import statistics

# --------------------------------------------
# TASK 3: STATISTICAL FUNCTIONS
# --------------------------------------------

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    name = max(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]

def find_min_score(marks_dict):
    name = min(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]

# --------------------------------------------
# TASK 4: GRADE ASSIGNMENT
# --------------------------------------------

def assign_grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

def assign_grades(marks_dict):
    return {name: assign_grade(score) for name, score in marks_dict.items()}

# --------------------------------------------
# TASK 2: INPUT METHODS
# --------------------------------------------

def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))
    
    for _ in range(n):
        name = input("Enter student name: ")
        score = int(input(f"Enter marks for {name}: "))
        marks[name] = score
    
    return marks

def read_csv():
    marks = {}
    filename = input("Enter CSV file path: ")
    
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                name, score = row
                marks[name] = int(score)
    except FileNotFoundError:
        print("File not found. Try again.")
    
    return marks

# --------------------------------------------
# TASK 5: PASS / FAIL FILTER
# --------------------------------------------

def pass_fail(marks_dict):
    passed = [name for name, score in marks_dict.items() if score >= 40]
    failed = [name for name, score in marks_dict.items() if score < 40]
    return passed, failed

# --------------------------------------------
# TASK 6: PRINT TABLE
# --------------------------------------------

def print_table(marks_dict, grade_dict):
    print("\nName\t\tMarks\tGrade")
    print("----------------------------------------")
    for name, score in marks_dict.items():
        print(f"{name:<15}{score:<10}{grade_dict[name]:<5}")

# --------------------------------------------
# MAIN MENU LOOP
# --------------------------------------------

def main():
    print("\n----- Welcome to GradeBook Analyzer -----")

    while True:
        print("\nChoose an option:")
        print("1. Manual Input")
        print("2. Load from CSV")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            marks = manual_input()
        elif choice == '2':
            marks = read_csv()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        # Task 3: Statistics
        avg = calculate_average(marks)
        med = calculate_median(marks)
        max_name, max_score = find_max_score(marks)
        min_name, min_score = find_min_score(marks)

        print("\n----- Statistical Summary -----")
        print(f"Average Marks: {avg:.2f}")
        print(f"Median Marks: {med}")
        print(f"Highest Score: {max_name} ({max_score})")
        print(f"Lowest Score:  {min_name} ({min_score})")

        # Task 4: Grades
        grades = assign_grades(marks)

        # Grade distribution
        grade_counts = {g: list(grades.values()).count(g) for g in "ABCDF"}
        print("\nGrade Distribution:")
        for grade, count in grade_counts.items():
            print(f"{grade}: {count}")

        # Task 5: Pass / Fail
        passed, failed = pass_fail(marks)
        print("\nPassed Students:", passed)
        print("Failed Students:", failed)

        # Task 6: Final Table
        print_table(marks, grades)

        print("\nDo you want to run again? (y/n)")
        if input().lower() != 'y':
            break

# Run program
if __name__ == "__main__":
    main()
