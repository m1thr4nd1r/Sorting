import os
import random
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
	# If on the root of the app, render the index screen
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
	return "chego"