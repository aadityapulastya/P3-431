

# Hoops CLI

  This repository contains the necessary files to run the HoopsCLI. It includes CSV files, a SQL file, and a Python script.

## Installation

To run the program, follow these steps:

1. **Install PostgreSQL**

2. **Set Up Python Environment**: Make sure you have psycopg2 installed. If not, execute this command in your terminal. This will install the program into your Python enviornment. 
   
   ```bash
   pip install psycopg2
   ```

## Usage

1. **Create Database**: Import `NBA.sql` into your Postgres Server by executing this command in the terminal:
   ```bash
   psql -U username -d database -f NBA.sql
   ```

   Replace `username` with your PostgreSQL username and `database` with the name of the database you want to create.

2. **Run the Python Script**: Execute `NBA.py` to connect with the DB and create a CLI interface for the user:

   ```bash
   python NBA.py
   ```
## Files & Folders

- `csv`: Contains raw CSVs.
- `NBA.sql`: SQL file defining the database schema and populating the data.
- `NBA.py`: Python script to create CLI to interact with DB.

## Contributors

- Aaditya Pulastya

