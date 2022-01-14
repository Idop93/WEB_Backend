import mysql.connector
from flask import jsonify
import json
def interact_db (query, query_type: str):
    return_value = False
    connection = mysql.connector.connect ( host= 'localhost',
                                           user='root',
                                           passwd='308222728',
                                           database='my_flask_project_db')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


def query_json(query):
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='308222728',
                                         database='my_flask_project_db')

    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()

    connection.close()
    cursor.close()
    return result