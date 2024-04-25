# HoopsCLI

This repository contains the necessary files to run the HoopsCLI. It includes the original CSV files, NBA.sql, NBA.py.

## Setting Up

To run the program, follow these steps:

1. **Install PostgreSQL**

2. **Set Up Python Environment**: Make sure you have psycopg2 installed. If not, execute this command in your terminal. This will install the program into your Python enviornment. 
   
   ```shell
   pip3 install psycopg2
   ```

## How to Use

1. **Create Database**: Import `NBA.sql` into your Postgres Server by executing this command in the terminal:
   ```shell
   psql -U username -d database -f NBA.sql
   ```

   Replace `username` with your PostgreSQL username and `database` with the name of the database you want to import to.
   
   **Note: You should create an empty DB to input the data into. The SQL script will not create a DB for you.**

3. **Run the Python Script**: Execute `NBA.py` to connect with the DB and create a CLI interface for the user:

   ```shell
   python NBA.py
   ```
