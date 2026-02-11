Finance Reporting Automation & Data Validation Tool
Project Overview

This project demonstrates a Python and PostgreSQL based ETL automation pipeline designed to simulate finance reporting and regulatory validation workflows used in multinational organizations.

The system extracts transactional data from a relational database, applies finance-specific transformation and validation rules, identifies anomalies, and generates automated summary and exception reports.

The objective is to reduce manual reporting effort while ensuring data accuracy, control, and compliance readiness.

Problem Statement

Finance teams handle large volumes of transactional data that must be:

Accurate

Consistent

Auditable

Manual reporting increases the risk of errors and compliance issues.
This project automates the extraction, validation, and reporting process using Python and SQL.

High-Level Architecture

PostgreSQL stores transactional data

Python ETL pipeline:

Extracts data using SQL

Transforms data using pandas

Validates records using finance rules

Automated reports are generated as CSV files

Technology Stack

Programming Language: Python

Database: PostgreSQL

Libraries: pandas, psycopg2

Concepts: ETL, SDLC, data validation, automation

Reporting Output: CSV files

Database Schema

Table: transactions

Column	Description
transaction_id	Unique transaction identifier
account_id	Account reference
transaction_date	Date of transaction
debit	Debit amount
credit	Credit amount
balance	Account balance
created_at	Audit timestamp

This schema reflects real-world finance transaction systems.

ETL Workflow
1. Extract

Connected Python to PostgreSQL using psycopg2

Retrieved transactional data using SQL

Loaded data into pandas DataFrame

2. Transform

Ensured numeric consistency for debit and credit

Derived a net_amount column (credit − debit)

Prepared data for validation and reporting

3. Validate (Finance Rules)

Applied rule-based validation to identify anomalies:

Debit and credit both zero → invalid

Debit and credit both non-zero → invalid

Negative balance → invalid

Valid and invalid records are separated to simulate regulatory exception handling.

4. Report

Automatically generated:

Finance summary report

Exception report for invalid records

Output Files

Generated automatically in the output/ folder:

finance_summary.csv

Total transactions

Valid vs invalid counts

Total debit and credit amounts

exception_report.csv

Records violating finance rules

Project Structure
finance-reporting-automation/
│
├── data/
│   └── insert_transactions.sql
│
├── src/
│   ├── db_connection.py
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── report.py
│   └── main.py
│
├── output/
│   ├── finance_summary.csv
│   └── exception_report.csv
│
├── requirements.txt
└── README.md
How to Run the Project
1. Install dependencies
pip install -r requirements.txt
2. Run the ETL pipeline
python -m src.main
3. View outputs

Check the output/ directory for generated reports.

Key Learning Outcomes

Built an end-to-end ETL pipeline using Python and SQL

Applied finance-specific validation rules

Implemented anomaly detection and exception reporting

Automated reporting workflows

Practiced clean code structure and SDLC principles