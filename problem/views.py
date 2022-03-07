from rest_framework.decorators import api_view
from rest_framework.response import Response
import sqlite3


# adding topics to table
@api_view(['GET'])
def create(request):
    if request.method == "GET":
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM topic")
        tableContain = cur.fetchall()
        print(tableContain)
        return Response(data={'data': tableContain})
    else:
        req_data = request.data
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        toArray = [req_data['TopicID'], req_data['TopicName']]
        cur.execute("INSERT INTO topic VALUES (?,?)", toArray)
        conn.commit()
        conn.close()
        return Response(data={"data": toArray})


@api_view(['GET', 'PUT', 'DELETE'])
def get(request, topic_id):
    if request.method == 'GET':
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM topic WHERE TopicID = (?)", topic_id)
        tableContain = cur.fetchone()
        # print(tableContain)
        if tableContain is None:
            return Response(data={"data": " does not exist"})
        return Response(data={'data': tableContain})
    elif request.method == 'DELETE':
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM topic WHERE TopicID = (?)", topic_id)
        tableContain = cur.fetchone()
        if tableContain is None:
            return Response(data={"data": " does not exist"})
        else:
            cur.execute("SELECT * FROM problem")
            tableAllContain = cur.fetchall()
            if not tableAllContain:
                cur.execute('DELETE FROM topic WHERE TopicID = (?)', topic_id)
                conn.commit()
                conn.close()
                return Response(data={"data": "Data DELETE"})
            else:
                for i in range(len(tableAllContain)):
                    if tableAllContain[i][2] == int(topic_id):
                        return Response(data={"data": "content used in problem content can't delete"})
                    else:
                        cur.execute('DELETE FROM topic WHERE TopicID = (?)', topic_id)
                        conn.commit()
                        conn.close()
                        return Response(data={"data": "Data DELETE"})
    elif request.method == 'PUT':
        req_data = request.data
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM topic WHERE TopicID = (?)", topic_id)
        tableContain = cur.fetchone()
        # print (tableContain)
        if tableContain is None:
            return Response(data={"data": " does not exist"})
        else:
            toArray = [req_data['TopicName'], topic_id]
            cur.execute("UPDATE topic SET 'TopicName' = (?) WHERE TopicID = (?)", toArray)
            conn.commit()
            conn.close()
            return Response(data={"data": toArray})


# adding difficultyLevel to table
@api_view(['GET', 'POST'])
def create_difflevel(request):
    if request.method == "GET":
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM difficultyLevel")
        tableContain = cur.fetchall()
        print(tableContain)
        return Response(data={'data': tableContain})
    else:
        req_data = request.data
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        toArray = [req_data['DiffID'], req_data['DiffLevel']]
        cur.execute("INSERT INTO difficultyLevel VALUES (?,?)", toArray)
        conn.commit()
        conn.close()
        return Response(data={"data": toArray})


@api_view(['GET', 'PUT', 'DELETE'])
def get_difflevel(request, diff_id):
    if request.method == 'GET':
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM difficultyLevel WHERE DiffID = (?)", diff_id)
        tableContain = cur.fetchone()
        # print(tableContain)
        if tableContain is None:
            return Response(data={"data": "does not exist"})
        return Response(data={'data': tableContain})
    elif request.method == 'DELETE':
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM difficultyLevel WHERE DiffID = (?)", diff_id)
        tableContain = cur.fetchone()
        if tableContain is None:
            return Response(data={"data": " does not exist"})
        else:
            cur.execute("SELECT * FROM problem")
            tableAllContain = cur.fetchall()
            if not tableAllContain:
                cur.execute('DELETE FROM difficultyLevel WHERE DiffID = (?)', diff_id)
                conn.commit()
                conn.close()
                return Response(data={"data": "Data DELETE"})
            else:
                for i in range(len(tableAllContain)):
                    print(tableAllContain[i][3], diff_id)
                    if tableAllContain[i][3] == int(diff_id):
                        return Response(data={"data": "content used in problem content can't delete"})
                    else:
                        cur.execute('DELETE FROM difficultyLevel WHERE DiffID = (?)', diff_id)
                        conn.commit()
                        conn.close()
                        return Response(data={"data": "Data DELETE"})
    elif request.method == 'PUT':
        req_data = request.data
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM difficultyLevel WHERE DiffID = (?)", diff_id)
        tableContain = cur.fetchone()
        # print (tableContain)
        if tableContain is None:
            return Response(data={"data": "does not exist"})
        else:
            toArray = [req_data['DiffLevel'], diff_id]
            cur.execute("UPDATE difficultyLevel SET 'DiffLevel' = (?) WHERE DiffID = (?)", toArray)
            conn.commit()
            conn.close()
            return Response(data={"data": toArray})


# adding problems to table
@api_view(['GET', 'POST'])
def createproblem(request):
    if request.method == "GET":
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM problem")
        tableContain = cur.fetchall()
        return Response(data={'data': tableContain})
    else:
        req_data = request.data
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        toArray = [req_data['ProblemID'], req_data['Author'], req_data['TopicID'],
                   req_data['DiffID'], req_data['Title'], req_data['Que'], req_data['Ans']]
        cur.execute("INSERT INTO problem VALUES (?,?,?,?,?,?,?)", toArray)
        conn.commit()
        conn.close()
        return Response(data={"data": toArray})


@api_view(['GET', 'PUT', 'DELETE'])
def getproblem(request, problem_id):
    if request.method == 'GET':
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM problem WHERE ProblemID = (?)", problem_id)
        tableContain = cur.fetchone()
        # print(tableContain)
        if tableContain is None:
            return Response(data={"data": "content does not exist"})
        return Response(data={'data': tableContain})
    elif request.method == 'DELETE':
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM problem WHERE ProblemID = (?)", problem_id)
        tableContain = cur.fetchone()
        if tableContain is None:
            return Response(data={"data": "content does not exist"})
        else:
            cur.execute("SELECT * FROM companyProblem")
            tableAllContain = cur.fetchall()
            # print(tableAllContain)
            if not tableAllContain:
                cur.execute('DELETE FROM problem WHERE ProblemID = (?)', problem_id)
                conn.commit()
                conn.close()
                return Response(data={"data": "Data DELETE"})
            else:
                for i in range(len(tableAllContain)):
                    print(tableAllContain[i][2], problem_id)
                    if tableAllContain[i][2] == int(problem_id):
                        return Response(data={"data": "content used in companyProblem content can't delete"})
                    else:
                        cur.execute('DELETE FROM problem WHERE ProblemID = (?)', problem_id)
                        conn.commit()
                        conn.close()
                        return Response(data={"data": "Data DELETE"})
    elif request.method == 'PUT':
        req_data = request.data
        conn = sqlite3.connect('user.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM problem WHERE ProblemID = (?)", problem_id)
        tableContain = cur.fetchone()
        # print (tableContain)
        if tableContain is None:
            return Response(data={"data": "content does not exist"})
        else:
            toArray = [req_data['Author'], req_data['TopicID'],req_data['DiffID'],
                       req_data['Title'], req_data['Que'], req_data['Ans'], problem_id]
            print(toArray)
            cur.execute("""UPDATE problem SET 'Author' = (?), 'TopicID' = (?), 'DiffID' = (?), 'Title' = (?),
                            'Que' = (?), 'Ans' = (?) WHERE ProblemID = (?)""", toArray)
            conn.commit()
            conn.close()
            return Response(data={"data": toArray})
