from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Daniel in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab_10_db_f8wj_user:0vBxKQt9dbeeF7ej1aZHAqZejc3QhSpp@dpg-d23e6lfdiees739hrpcg-a.oregon-postgres.render.com/lab_10_db_f8wj")
    conn.close()
    return "Database Connection Successful"

# @app.route('/db_create')
# def db_create():
#     conn = psycopg2.connect("postgresql://lab_10_db_f8wj_user:0vBxKQt9dbeeF7ej1aZHAqZejc3QhSpp@dpg-d23e6lfdiees739hrpcg-a/lab_10_db_f8wj")
#     cur = conn.cursor()
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS Basketball(
#             First varchar(255),
#             Last varchar(255),
#             City varchar(255),
#             Name varchar(255),
#             Number int
#             );
#     ''')
#     conn.commit()
#     conn.close()
#     return "Basketball table successfully created"
