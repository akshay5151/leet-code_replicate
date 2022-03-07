import sqlite3


def create_model():
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE "companyName" (
    "CompanyID" INTEGER NOT NULL UNIQUE,
    "CompanyName" NVARCHAR(255) NOT NULL,
    PRIMARY KEY("CompanyID" AUTOINCREMENT)
    )''')

    cur.execute('''CREATE TABLE "companyProblem" (
    "ID" INTEGER NOT NULL UNIQUE,
    "CompanyID" INTEGER NOT NULL,
    "ProblemID" INTEGER NOT NULL,
    FOREIGN KEY("ProblemID") REFERENCES "problem"("ProblemID"),
    FOREIGN KEY("CompanyID") REFERENCES "companyName"("CompanyID"),
    PRIMARY KEY("ID" AUTOINCREMENT)
    )''')

    conn.commit()
    conn.close()
