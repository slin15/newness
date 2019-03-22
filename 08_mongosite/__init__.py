# Susan Lin
# SoftDev pd8
# K #08: Ay Mon, Go Git It From Yer Flask
# 2019-03-06

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = os.urandom(32)

from util import mongo as mong

DB_FILE = 'data/mongo.py'

#home root
@app.route('/', methods=["POST", "GET"])
def home():
    render_template('home.html')



if __name__ == "__main__":
    app.debug = True
    app.run()
