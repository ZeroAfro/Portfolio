# Weekly TDEE Weight Loss Calculator

A command-line Python tool that collects weekly TDEE inputs from the user, validates them, and calculates the average daily calories required to lose 2 pounds per week.

---

## Overview

This script prompts users for their Total Daily Energy Expenditure (TDEE) over multiple weeks, then calculates a recommended daily caloric intake to achieve a weight loss of 2 pounds per week. The program includes input validation, logging, and runs until the calculation is completed or the user chooses to quit.

---

## Features

- 📅 Input your TDEE for multiple weeks  
- ✅ Validates inputs (non-integer, negative, or zero entries)  
- 🧮 Calculates average TDEE and subtracts 1000 for weight loss target  
- 🔄 Allows quitting at any point using `q`  
- 🧪 Debug logging available for tracing program execution  

---

## How to Use

1. Run the script using Python.
2. Enter how many weeks of TDEE data you want to input (must be 2 or more).
3. For each week, input a valid TDEE (positive integer).
4. After all entries, view the recommended daily calorie intake to lose 2 pounds/week.
5. You can exit at any point by typing `q`.

---

## Technologies Used

- **Python 3.10+**
- **Built-in Modules:** `sys`, `logging`
