**Table of Contents**
- [Introduction](#introduction)
    - [Challenge Details](#challenge-details) 
        - [Mandatory Features](#mandatory-features)
        - [Bonus](#bonus)
- [Installation (Pre-Requierements)](#installation)
    - [Python Libraries Requiered](#python-libraries-requiered)
- [Repository files and folders](#repository-files-and-folders)
    - [Folder](#folders)
    - [Files](#files)
- [Usage](#usage)

 
# Introduction
 This repository was created as a result of a Data Engineer interview challenge. The main goals was to use the AviationStack API with the basic plan to obtain historical flight data and perform basic flight data
processing and analysis. The assessment revolved around (my) ability to create robust products with attention to detail, standards and reusability.

 [AviationStack API Documentation](https://aviationstack.com/documentation)

## Challenge Details
>### Mandatory Features
- There must be an automated process to ingest and store the data. Use Python or another
programming language of your choice to develop a script or application that interacts with the
API.
- Write a function that makes a request to the API to obtain historical flight data for a specific
airline in a given date range.
- Process the received data and store it in a suitable format, such as a CSV file and a database
(SQL or NoSQL) .
- Implements functionality to filter and query the stored data. For example, it allows searching for
flights by origin, destination, airline, etc.
- Perform a basic analysis of the data obtained. You can calculate statistics such as total number
of flights, average flight duration, number of flights per airline.
- Generate visualizations using graphical libraries such as Matplotlib or Plotly to display the results
of the analysis in the form of graphs or charts.
- Document your solution, including installation and usage instructions, as well as an explanation
of the processes and decisions made during development.

> ### Bonus
- Containerize your solution.
- Sketch up how you would set up the application using any cloud provider (AWS, GCP, etc).



# Installation
- In order to run properly this project, your machine should have Python installed (version 3.9+), JupyterNotebook or Jupyter Lab (in order to open and run the ipynb files) and also the following python libraries:

## Python Libraries Requiered
- requests
- pandas
- json
- datetime
- sqlite3
- subprocess
- numpy
- plotly
- matplotlib

# Repository files and folders
## Folders
There are two folders in this repository, both hold the data ingested by the code.
- **csv-files**
    - Store the csv-files containing the data from each day and airline requested.
- **database**
    - Store the database containing all the data in tables.

## Files
There are three files, which are the main files. A brief description for each one:
- `source_to_landing.py`
    - Python script that holds a function resposible for taking the data from the API connection, and storing this data on .csv files.
- `landing_to_sql.py`
    - Python script that holds a function resposible for taking the data stored in .csv files, and populating it in the database.
- `Analysis.ipynb`
    - JupyterNotebook holding instructions for functions usage, database consulting and data analysis.

# Usage
- Clone the repository.
    - Open Git Bash.
    - Change the current working directory to the location where you want the cloned directory.
    - `git clone https://github.com/RenanGroot/aviation-stack-api-challenge.git`
- Open the Analysis.ipynb Jupyter Notebook.
    - Using Jupyter Notebook or Jupyter Lab.
- Follow the instructions inside the Notebook.
