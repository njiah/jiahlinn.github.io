import mysql.connector
from flask import Flask, render_template, session

app = Flask(__name__)


def get_connection():
    conn = mysql.connector.connect( host = 'localhost',
                                    user = 'ngwe2linn',
                                    password = 'Ngwe2linN9+$++',
                                    database = 'ngwe2linn')
    return conn

@app.route('/index')
def index():
    return render_template('main.html')