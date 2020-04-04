import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    TOP_DIR='/Users/alfredo/python'
    python_projects = [i for i in os.listdir(TOP_DIR)]
    return render_template('index.html', files=python_projects)
