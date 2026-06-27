# Python Mini Projects

A collection of 20 Python mini projects completed as part of a summer internship program. The projects are organized into five sections, each focused on a specific set of Python concepts and tools. All projects are written in Python and follow a clean, readable coding style.

---

## Table of Contents

- [Section 1 - Python Basics](#section-1---python-basics)
- [Section 2 - Data Structures](#section-2---data-structures)
- [Section 3 - Functions and File Handling](#section-3---functions-and-file-handling)
- [Section 4 - OOP and Advanced Python](#section-4---oop-and-advanced-python)
- [Section 5 - Python for Data and Automation](#section-5---python-for-data-and-automation)
- [How to Run](#how-to-run)
- [Requirements](#requirements)

---

## Section 1 - Python Basics

**Concepts:** Variables, loops, conditionals, strings, random module

| Project | Description |
|---|---|
| Number Guessing Game | Computer picks a random number and the user guesses with hints like too high or too low. Tracks number of attempts. |
| Simple ATM Machine | User enters a PIN and can check balance, deposit, or withdraw. Uses conditionals and loops for menu navigation. |
| Basic Calculator | Performs addition, subtraction, multiplication and division with input validation and division by zero handling. |
| Word Counter and Analyzer | Takes a paragraph as input, counts words, finds the longest word, counts vowels and tracks most common starting letter. |

---

## Section 2 - Data Structures

**Concepts:** Lists, tuples, dictionaries, sets, list comprehensions

| Project | Description |
|---|---|
| Student Result Management System | Stores student names and marks in a dictionary, computes average, finds the topper and displays grades using list comprehensions. |
| Contact Book | Add, search, update and delete contacts stored in a dictionary. Uses a set to detect duplicate phone numbers. |
| Shopping Cart System | Add and remove items using a list, track unique categories using a set and store item prices in a dictionary with total bill calculation. |

---

## Section 3 - Functions and File Handling

**Concepts:** Functions, modules, file I/O, exception handling, CSV handling

| Project | Description |
|---|---|
| Library Book Management System | Add, remove and search books stored in a CSV file using file handling with try-except for error management. |
| Expense Tracker | Log daily expenses to a text file and summarize by category using functions with exception handling for invalid input. |
| Student Grade File Manager | Reads student data from a CSV, computes grades using functions and writes updated results to a new CSV file. |
| Password Generator and Validator | Generates strong passwords using the random and string modules and validates passwords using a custom exception class. |

---

## Section 4 - OOP and Advanced Python

**Concepts:** Classes, inheritance, polymorphism, encapsulation, decorators, regex, generators, dunder methods

| Project | Description |
|---|---|
| OOP Grade Management System | Classes for Student, Teacher and Course with inheritance from a base Person class. Records are saved and retrieved from a file using the __str__ dunder method. |
| Bank Account System | Base class Account with child classes SavingsAccount and CurrentAccount. Each overrides the withdraw method differently. Balance is encapsulated and account numbers are validated using regex. |
| Employee Payroll System | Employee base class with FullTimeEmployee and PartTimeEmployee subclasses. Uses polymorphic calculate_salary method and a decorator to log every salary computation to a file. |
| Log File Analyzer | Reads a server log file, uses regex to extract error codes, timestamps and IP addresses. Uses a generator to process lines one at a time and saves a summary report to an output file. |

---

## Section 5 - Python for Data and Automation

**Concepts:** NumPy, Pandas, web scraping, requests, BeautifulSoup, CSV export

| Project | Description |
|---|---|
| Automated Data Collector | Scrapes book titles, prices and ratings from books.toscrape.com using requests and BeautifulSoup and stores the data in a CSV file using Pandas. |
| IPL Dataset Analyzer | Loads a real IPL matches CSV dataset, cleans missing values and answers 10 business questions using Pandas groupby, value_counts and aggregation functions. |
| NumPy Statistics Dashboard | Takes a dataset as input either manually or from a file, computes mean, median, standard deviation, min and max using NumPy and displays a text based summary report. |
| Student Marks Analyzer | Reads student marks from a CSV, filters pass and fail, sorts by score, adds a grade column using apply() and exports the cleaned data to a new CSV file. |

---

## How to Run

1. Clone the repository

```
git clone https://github.com/Ajeet22222/python-mini-projects.git
```

2. Navigate into the project folder

```
cd python-mini-projects
```

3. Install required libraries for Section 5 projects

```
pip install requests beautifulsoup4 pandas numpy
```

4. Navigate into any section folder and run the desired project

```
cd section1_basics
python number_guessing_game.py
```

---

## Requirements

- Python 3.x
- pandas
- numpy
- requests
- beautifulsoup4

All standard library modules such as random, string, csv, os, re and datetime are included with Python and do not require separate installation.

---

## Project Structure

```
python_mini_projects/
|
|-- section1_basics/
|   |-- number_guessing_game.py
|   |-- atm_machine.py
|   |-- basic_calculator.py
|   |-- word_counter_analyzer.py
|
|-- section2_data_structures/
|   |-- student_result_management.py
|   |-- contact_book.py
|   |-- shopping_cart.py
|
|-- section3_functions_file_handling/
|   |-- library_management.py
|   |-- expense_tracker.py
|   |-- student_grade_file_manager.py
|   |-- password_generator_validator.py
|
|-- section4_oop_advanced/
|   |-- oop_grade_management.py
|   |-- bank_account_system.py
|   |-- employee_payroll.py
|   |-- log_file_analyzer.py
|
|-- section5_data_automation/
|   |-- automated_data_collector.py
|   |-- ipl_dataset_analyzer.py
|   |-- numpy_statistics_dashboard.py
|   |-- student_marks_analyzer.py
|
|-- README.md
```

---

## Author
Ajeet
Developed as part of internship Python programming module.
