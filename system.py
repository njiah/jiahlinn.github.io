from flask import Flask, render_template, session

'''
import mysql.connector
app = Flask(__name__)


def get_connection():
    conn = mysql.connector.connect( host = 'localhost',
                                    user = 'ngwe2linn',
                                    password = 'Ngwe2linN9+$++',
                                    database = 'ngwe2linn')
    return conn
'''

#initializing app with Flask
app = Flask(__name__)
#app.secret_key = 'CV Website'

@app.route('/')
def index():
    return render_template('main.html')