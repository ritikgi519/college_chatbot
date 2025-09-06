import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS college (topic TEXT, info TEXT)")

data = [
    ("courses", "We offer B.Tech, B.Sc, MBA, and MCA programs."),
    ("fees", "The average fee is ₹1,00,000 per year depending on the course."),
    ("admission", "Admissions start in June. Entrance exam + interview required."),
    ("faculty", "We have highly qualified faculty from IITs and NITs.")
]

cursor.executemany("INSERT INTO college VALUES (?, ?)", data)
conn.commit()
conn.close()
