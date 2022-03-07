import sqlite3


def create_model():
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE "userLogin" (
    "UserID" INTEGER NOT NULL UNIQUE,
    "FirstName" NVARCHAR(255) NOT NULL,
    "LastName" NVARCHAR(255) NOT NULL,
    "Email" NVARCHAR(255) NOT NULL,
    "Password" NVARCHAR(255) NOT NULL,
    PRIMARY KEY("UserID" AUTOINCREMENT)
    )''')

    conn.commit()
    conn.close()
