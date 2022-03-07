import sqlite3


def create_model():
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE "topic" (
    "TopicID"	INTEGER NOT NULL UNIQUE,
    "TopicName"	NVARCHAR(255) NOT NULL,
    PRIMARY KEY("TopicID" AUTOINCREMENT)
    )''')

    cur.execute('''CREATE TABLE "difficultyLevel" (
    "DiffID"	INTEGER NOT NULL UNIQUE,
    "DiffLevel"	NVARCHAR(255) NOT NULL,
    PRIMARY KEY("DiffID" AUTOINCREMENT)
    )''')

    cur.execute('''CREATE TABLE "problem" (
    "ProblemID" INTEGER NOT NULL UNIQUE,
    "Author" INTEGER NOT NULL,
    "TopicID" INTEGER NOT NULL,
    "DiffID" INTEGER NOT NULL,
    "Title" NVARCHAR(255) NOT NULL,
    "Que" NTEXT NOT NULL,
    "Ans" NTEXT NOT NULL,
    FOREIGN KEY("TopicID") REFERENCES "topic"("TopicID"),
    FOREIGN KEY("DiffID") REFERENCES "difficultyLevel"("DiffID"),
    FOREIGN KEY("Author") REFERENCES "userLogin"("UserID"),
    PRIMARY KEY("ProblemID" AUTOINCREMENT)
    )''')

    conn.commit()
    conn.close()
