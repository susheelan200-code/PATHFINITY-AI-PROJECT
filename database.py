
import sqlite3
import json

def create_database():
    conn = sqlite3.connect("pathfinity.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            academic_year TEXT,
            stream TEXT,
            interests TEXT,
            skills TEXT,
            career_goal TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_student(name, year, stream, interests, skills, goal):
    conn = sqlite3.connect("pathfinity.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, academic_year, stream, interests, skills, career_goal)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        year,
        stream,
        json.dumps(interests),
        json.dumps(skills),
        goal
    ))

    conn.commit()
    conn.close()


create_database()
def load_student():
    conn = sqlite3.connect("pathfinity.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, academic_year, stream, interests, skills, career_goal
        FROM students
        ORDER BY id DESC
        LIMIT 1
    """)

    student = cursor.fetchone()
    conn.close()

    if student:
        return {
            "name": student[0],
            "year": student[1],
            "stream": student[2],
            "interests": json.loads(student[3]),
            "skills": json.loads(student[4]),
            "goal": student[5]
        }

    return None