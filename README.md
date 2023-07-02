# Udacity Project: Data Modeling with PostgresSQL

## Introduction

A startup called Sparkify has hired me as a data engineer to create a database using PostresSQL to help them optimize queries for their song play analysis. I have been tasked with creating a Star database schema and developing ETL pipelines to create the tables, populate them with data and query for results. Data has been provided in JSON files for song_data and log_data from which I'm to extract the information and push into the database for analysis.

## Description


## Requirements

Project was created in Visual Studio Code (v1.79.2) using an Anaconda virtual environment. An installation of Postgres (v7.2) is available on the localhost.
Please refer to the requirements.txt file for all Python library versions used in this project.

## Database Design

Temporary dataframes were utilized to import sample data from the JSON files in order to visualize the data structures. From this analysis, tables were designed and created using SQL queries located in the sql_queryies.py file. Execution of the code in the create_tables.py file will drop the sparkifydb (if exists) and create the required tables.

To create the ETL process, the etl.ipynb (Jupyter Notebook) was written and tested so results could be visualized. When all test code had been executed, the test.ipynb notebook was ran to validate that all tables had data. Finally, dode in the etl.py file is executed to populate the tables from the data contained in the JSON files.

The below Entity Relationship Diagram was generated in pgAdmin4 and is included in the sparkifydb_erd.png file.
<img src="sparkifydb_erd.png" alt="ERD Diagram"/>

## ETL Pipeline

## Query Examples
