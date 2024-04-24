

# Hoops CLI

  This repository contains the necessary files to run HoopsCLI. It includes CSV files, a SQL file, and a Python script.

## Installation

To run the program, follow these steps:

1. **Install PostgreSQL**: If you haven't already, install PostgreSQL onto your machine. You can download it from the [official PostgreSQL website](https://www.postgresql.org/download/).

2. **Set Up Python Environment**: Make sure you have Python installed on your machine. Additionally, install the necessary packages by running:
   
   ```bash
   pip install psycopg2
   ```

## Usage

1. **Create Database**: Import the provided `.sql` file into your PostgreSQL database management tool (e.g., pgAdmin, psql) to create a new database with the required schema. You can do this by running the following command in your terminal:

   ```bash
   psql -U your_username -d your_database_name -a -f schema.sql
   ```

   Replace `your_username` with your PostgreSQL username and `your_database_name` with the name of the database you want to create.

2. **Run the Python Script**: Execute the provided `.py` file to populate the database with data from the CSV files. You can run the script using:

   ```bash
   python NBA.py
   ```
## Files & Folders

- `csv`: Contains the raw data.
- `schema.sql`: SQL file defining the database schema.
- `NBA.py`: Python script to import data from CSV files into the PostgreSQL database.

## Contributors

- Aaditya Pulastya

