from cs50 import SQL
import csv

def add_house(house, head):
    for dict in houses:
        if house == dict['house']:
            return
    houses.append({'id' : len(houses) + 1, 'house' : house, 'head' : head})


def add_student(student, id):
    for dict in students:
        if student == dict['name']:
            return
    students.append({'id' : id, 'name' : student})


def add_assignment(id, house):
    house_id = 0
    for dict in assignments:
        if id == dict['student_id']:
            return
    for dict in houses:
        if house == dict['house']:
            house_id = dict['id']
    assignments.append({'student_id' : id, 'house_id' : house_id})
    

db = SQL('sqlite:///roster.db')

students = []
houses = []
heads = []
assignments = []

with open('students.csv', 'r') as read_file:
    source_dictionary = csv.DictReader(read_file)
    for row in source_dictionary:
        # print(row)
        id = int(row["id"])
        name = row["student_name"]
        house = row["house"]
        head = row["head"]
        # print(id)
        add_house(house, head)
        add_student(name, id)
        add_assignment(id, house)

db.execute('DROP TABLE students;')
db.execute('DROP TABLE houses;')
db.execute('DROP TABLE house_assignments;')
# Create three tables with correct columns (dpcumented in 'schema.SQL')
db.execute('CREATE TABLE students (id INTEGER, student_name TEXT, PRIMARY KEY(id));')
db.execute('CREATE TABLE houses (id INTEGER NOT NULL, house TEXT NOT NULL, head TEXT NOT NULL, PRIMARY KEY(id));')
db.execute('CREATE TABLE house_assignments (student_id INTEGER NOT NULL, house_id INTEGER NOT NULL, FOREIGN KEY(student_id) REFERENCES students(id), FOREIGN KEY(house_id) REFERENCES houses(id), PRIMARY KEY(student_id, house_id));')

# Populate students table
for student in students:
    db.execute('INSERT INTO students (id, student_name) VALUES (?, ?);', student["id"], student['name'])
# print(db.execute('SELECT * FROM students;'))

#Populate houses table
for house in houses:
    db.execute('INSERT INTO houses (id, house, head) VALUES (?, ?, ?);', house['id'], house['house'], house['head'])

# Populate house_assignments table
for assignment in assignments:
    db.execute('INSERT INTO house_assignments (student_id, house_id) VALUES(?, ?);', assignment['student_id'], assignment['house_id'])
