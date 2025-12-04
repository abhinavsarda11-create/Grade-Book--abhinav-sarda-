# Grade-Book--abhinav-sarda-
python assignment 2

📘 GradeBook Analyzer

A Python-based CLI tool to analyze student marks, compute statistics, assign grades, and generate a full grade report.

📌 Project Overview

Lecturers often spend time manually calculating class performance.
This project automates the process by:

Reading student marks (manual input or CSV)

Performing statistical analysis

Assigning grades (A–F)

Separating pass/fail students

Printing a clean formatted results table

Allowing repeated analysis via a CLI loop

This tool is part of the Programming for Problem Solving using Python course (Mini Project).

🎯 Learning Objectives

By completing this project, you will learn to:

Read and store student data using Python structures

Use CSV handling (csv module)

Implement statistical functions (mean, median, min, max)

Apply decision-making statements for grading

Use list comprehensions for filtering

Format table-like output

Build a menu-driven CLI loop

Practice modular programming

📂 Project Structure
gradebook_analyzer/
│
├── gradebook.py
├── README.md
└── students.csv        (optional, sample input file)

🚀 Features Implemented
✔ 1. Data Entry Options

Manual student entry

Load from CSV file (name,marks format)

✔ 2. Statistical Analysis

Average marks

Median marks

Highest score + student name

Lowest score + student name

✔ 3. Grade Assignment

Grade categories:

A → 90+
B → 80–89
C → 70–79
D → 60–69
F → below 60

✔ 4. Pass/Fail Using List Comprehension

Passed: marks ≥ 40

Failed: marks < 40

✔ 5. Results Table Output

Clean table:

Name        Marks    Grade
---------------------------
Alice       78       C
Bob         92       A

✔ 6. Menu-Based CLI Loop

Users can repeat analysis or exit the program.
