from dbConfig import *

@app.route('/connect_db', methods=['GET'])
@connect_sql()
def conection_mysql_test(cursor):
    return 'connect success'
#
# @app.route('/hello/<firstname>/<lastname>', methods=['GET'])
# @connect_sql()
# def hello(cursor, firstname, lastname):
#     sql = "SELECT * FROM test WHERE firstname=%s AND lastname=%s"
#     cursor.execute(sql,(firstname, lastname))
#     print(cursor.description)
#     printvar = str(cursor.fetchall())
#     columns = [column[0] for column in cursor.description]
#     result = toJson(cursor.fetchall(),columns)
#     return printvar

#
# @app.route('/getName2', methods=['POST'])
# def getName2():
#     data = request.json
#     connection = mysql.connect()
#     cursor = connection.cursor()
#     sql = "SELECT * FROM test WHERE firstname=%s AND lastname=%s And id=%s"
#     cursor.execute(sql,(data['firstname'], data['lastname'], data['id']))
#     columns = [column[0] for column in cursor.description]
#     result = toJson(cursor.fetchall(),columns)
#     connection.commit()
#     connection.close()
#     return jsonify(result)
#

# @app.route('/hello2', methods=['GET'])
# def hello2():
#     return jsonify(getData('hello'))
#
# @connect_sql()
# def getData(c, data):
#     # print data
#     c.execute("SELECT * FROM SpecialSkill")
#     columns = [column[0] for column in c.description]
#     result = toJson(c.fetchall(),columns)
#     return result

#todo checktoken
# @app.before_request
# def before_request_func():
#     print(request.headers['token'])
#     if(request.headers['token'] != 'token na ja'):
#         return "invalid token",status.HTTP_200_OK

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    # print(app.route)
    app.run(debug=True,host='0.0.0.0',threaded=True,port=5000)

    # print(request.headers)
    # print(request.headers['User-Agent'])

