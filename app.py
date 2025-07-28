from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Daniel in 3308'

@app.route('/db_test')
def db_test():
    conn = psychopg2.connect("postgresql://lab_10_db_f8wj_user:0vBxKQt9dbeeF7ej1aZHAqZejc3QhSpp@dpg-d23e6lfdiees739hrpcg-a/lab_10_db_f8wj")
    conn.close()
    return "Database Connection Successful"
