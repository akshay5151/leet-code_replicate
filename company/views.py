from rest_framework.decorators import api_view
from rest_framework.response import Response
import sqlite3


@api_view(['GET', 'POST'])
def create(request):
    if request.method == "GET":
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM companyName")
        tableContain = cur.fetchall()
        print(tableContain)
        return Response(data={'data': tableContain})
    else:

        req_data = request.data
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        toArray = [req_data['CompanyID'], req_data['CompanyName']]
        print(toArray)
        cur.execute("INSERT INTO companyName VALUES (?,?)", toArray)
        conn.commit()
        conn.close()
        return Response(data={"data": toArray})


@api_view(['GET', 'PUT', 'DELETE'])
def get(request, company_id):
    if request.method == 'GET':
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM companyName WHERE CompanyID = (?)", company_id)
        tableContain = cur.fetchone()
        # print(tableContain)
        if tableContain is None:
            return Response(data={"data": "content does not exist"})
        return Response(data={'data': tableContain})
    elif request.method == 'DELETE':
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM companyName WHERE CompanyID = (?)", company_id)
        tableContain = cur.fetchone()
        if tableContain is None:
            return Response(data={"data": "content does not exist"})
        else:
            cur.execute("SELECT * FROM companyProblem")
            tableAllContain = cur.fetchall()
            if not tableAllContain:
                cur.execute('DELETE FROM companyName WHERE CompanyID = (?)', company_id)
                conn.commit()
                conn.close()
                return Response(data={"data": "Data DELETE"})
            else:
                for i in range(len(tableAllContain)):
                    if tableAllContain[i][1] == int(company_id):
                        return Response(data={"data": "content used in problem content can't delete"})
                    else:
                        cur.execute('DELETE FROM companyName WHERE CompanyID = (?)', company_id)
                        conn.commit()
                        conn.close()
                        return Response(data={"data": "Data DELETE"})
    elif request.method == 'PUT':
        req_data = request.data
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM companyName WHERE CompanyID = (?)", company_id)
        tableContain = cur.fetchone()
        # print (tableContain)
        if tableContain is None:
            return Response(data={"data": "content does not exist"})
        else:
            toArray = [req_data['CompanyName'], company_id]
            cur.execute("UPDATE companyName SET 'CompanyName' = (?) WHERE CompanyID = (?)", toArray)
            conn.commit()
            conn.close()
            return Response(data={"data": toArray})


@api_view(['GET', 'POST'])
def create_comProblem(request):
    if request.method == "GET":
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM companyProblem")
        tableContain = cur.fetchall()
        # print(tableContain)
        return Response(data={'data': tableContain})
    else:
        req_data = request.data
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        toArray = [req_data['ID'], req_data['CompanyID'], req_data['ProblemID']]
        # print(toArray)
        cur.execute("INSERT INTO companyProblem VALUES (?,?,?)", toArray)
        conn.commit()
        conn.close()
        return Response(data={"data": toArray})


@api_view(['GET', 'PUT', 'DELETE'])
def get_comProblem(request, id):
    if request.method == 'GET':
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM companyProblem WHERE ID = (?)", id)
        tableContain = cur.fetchone()
        # print(tableContain)
        if tableContain is None:
            return Response(data={"data": "content does not exist"})
        return Response(data={'data': tableContain})
    elif request.method == 'DELETE':
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM companyProblem WHERE ID = (?)", id)
        tableContain = cur.fetchone()
        if tableContain is None:
            return Response(data={"data": "content does not exist"})
        else:
            cur.execute('DELETE FROM companyProblem WHERE ID = (?)', id)
            conn.commit()
            conn.close()
            return Response(data={"data": "Data DELETE"})
    elif request.method == 'PUT':
        req_data = request.data
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM companyProblem WHERE ID = (?)", id)
        tableContain = cur.fetchone()
        # print (tableContain)
        if tableContain is None:
            return Response(data={"data": "content does not exist"})
        else:
            toArray = [req_data['CompanyID'], req_data['ProblemID'], id]
            cur.execute("UPDATE companyProblem SET 'CompanyID' = (?), 'ProblemID' =(?) WHERE CompanyID = (?)", toArray)
            conn.commit()
            conn.close()
            return Response(data={"data": toArray})
