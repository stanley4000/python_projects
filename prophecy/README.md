#############################################################################
This was completed as a practice problem for cs50, 2023: https://cs50.harvard.edu/x/2023/problems/7/prophecy/
############################################################################

The python script 'prophecy_script.py' refactors the database 'roster.db' to create three tables for: students, houses, and house_assignments. The file 'schema.sql' documents the code used to create the new tables.

This script assumes that roster.db already contains each of these tables and deletes them before proceeding with the refactoring.

It uses the information in students.csv to re-populate the new tables. 

It uses the SQL/sqlite functions found in Harvard's CS50 library.