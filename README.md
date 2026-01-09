# Teaching Assistant Submission Tester

This project is a simple automated grading tool designed to help Teaching Assistants compile and test student C submissions consistently and efficiently. 
The script compiles a C program, runs it with a predefined input file, and compares the program’s output against an expected result.

---

## Project Files

Your folder **must contain exactly these three files**:

- `lab5.c` – Student C program to be compiled and tested  
- `customer_data.txt` – Input data file passed to the program  
- `grading.py` – Python script that compiles and tests the C program  

---

## Requirements

- Python 3  
- GCC (C compiler)  
- Terminal / PowerShell  

Ensure both `python3` and `gcc` are available in your system PATH.

---

## How to Run

1. Open a terminal (PowerShell).
2. Navigate to the folder containing all three files.
3. Run the grading script:

```bash
python3 grading.py

