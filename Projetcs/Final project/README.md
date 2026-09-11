# Titanic Survival Analysis - Final Project

This project performs Exploratory Data Analysis (EDA) on the famous Titanic dataset using Python, Pandas, Matplotlib, and Seaborn to understand the factors that influenced passenger survival.

## Project Overview
The objective of this project is to analyze passenger data from the Titanic disaster to identify patterns and correlations between survival and various demographic or socio-economic factors such as gender, passenger class, and age.

## Dataset
* **Source:** Kaggle (Titanic Dataset - `train.csv`)
* **Description:** Contains data on 891 passengers, including whether they survived (`Survived`), passenger class (`Pclass`), sex (`Sex`), age (`Age`), sibling/spouse count (`SibSp`), parent/child count (`Parch`), fare paid (`Fare`), and port of embarkation (`Embarked`).

## Tools & Libraries Used
* **Python** (Programming Language)
* **Pandas & NumPy** (Data manipulation and handling missing values)
* **Matplotlib & Seaborn** (Data visualization and graphical analysis)

## Step-by-Step Analysis Workflow
1. **Data Loading & Inspection:** Loaded the dataset and inspected data types, shape, and missing values.
2. **Data Preprocessing & Cleaning:** Handled missing values in the `Age` and `Embarked` columns and removed irrelevant identifiers (`PassengerId`, `Name`, `Ticket`, `Cabin`).
3. **Exploratory Data Analysis & Visualization:**
   * Analyzed survival rates by **Gender** (females had a significantly higher survival rate).
   * Analyzed survival rates by **Passenger Class** (1st-class passengers had higher priority and survival probability).
   * Examined the **Age Distribution** of survivors versus non-survivors.

## How to Run the Project
1. Ensure you have Python installed along with the required libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`).
2. Download the `train.csv` file from Kaggle and place it in the project root directory.
3. Open the Jupyter Notebook (`.ipynb`) and run all cells sequentially.