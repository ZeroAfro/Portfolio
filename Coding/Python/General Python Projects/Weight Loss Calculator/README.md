# Weight Loss Calculator

A command-line Python tool that collects weekly Total Daily Energy Expenditure (TDEE) inputs from the user, validates them, and calculates the average daily caloric intake required to lose **1 or 2 pounds per week**.

---

## Overview

This script prompts users to:

- Enter how many weeks of TDEE data they want to provide (minimum 2 weeks).  
- Choose a weight loss goal of **1 or 2 pounds per week**.  
- Input weekly TDEE values, which are validated for correctness.  

Based on the average TDEE and chosen goal, the program calculates and displays the recommended daily calorie intake to meet the weight loss target. It also supports quitting anytime by typing `q`.

The program includes input validation, debug logging, and messaging around safe calorie thresholds (e.g., below 1200 calories/day).

---

## Features

- 📅 Input multiple weeks of TDEE data (minimum 2 weeks)  
- 🎯 Choose a weight loss goal: 1 or 2 pounds per week  
- ✅ Validates inputs (no zero, negative, or non-integer values allowed)  
- 🧮 Calculates average TDEE and subtracts 500 or 1000 calories depending on goal  
- ⚠️ Warns user if the calculated calorie intake drops below 1200/day  
- 🔄 Type `q` at any prompt to quit the program immediately  
- 🧪 Debug logging included for tracing program flow and troubleshooting  

---

## How to Use

1. Run the script with Python 3.10 or higher.  
2. Enter the number of weeks to input TDEE data (minimum two).  
3. Choose your weight loss goal: 1 or 2 pounds per week.  
4. Input your weekly TDEE values one by one.  
5. Receive your recommended daily calorie intake to meet your weight loss goal.  
6. Press ENTER to exit after viewing the result.  

💡 You can type `q` at any point to quit.

---

## Technologies Used

- **Python 3.10+**  
- Built-in modules: `sys`, `logging`

---

## Notes

- The program currently subtracts a fixed daily deficit (500 or 1000 calories) based on the weight loss goal.  
- Input validation ensures realistic and meaningful data entries.  
- Debug logging can be enabled or disabled by commenting/uncommenting the `logging.disable()` line in the script.  


