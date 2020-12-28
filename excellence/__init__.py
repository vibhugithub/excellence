from flask import Flask, request
import os
import mysql.connector  # using pip3 install mysql.connector


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_PORT = "3306"
MYSQL_DATABASE = "excellence_tech"


def get_db_connection():
    db_connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        passwd=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        port=MYSQL_PORT,
    )
    return db_connection
