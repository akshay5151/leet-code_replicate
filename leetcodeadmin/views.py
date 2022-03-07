from rest_framework.decorators import api_view
from rest_framework.response import Response
import sqlite3


@api_view(['GET', 'POST'])
def admin_create(request):
    if request.method == "GET":
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM userLogin")
        tableContain = cur.fetchall()
        print(tableContain)
        return Response(data={'data': tableContain})
    else:
        req_data = request.data
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        toArray = [req_data['UserID'],req_data['FirstName'],req_data['LastName'],
                   req_data['Email'],req_data['Password']]
        cur.execute("INSERT INTO userLogin VALUES (?,?,?,?,?)", toArray)
        conn.commit()
        conn.close()
        return Response(data={"data": toArray})
