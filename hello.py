import os
import random
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.debug = True  # Activating Debug of the App

@app.route('/')
def hello():
	# If on the root of the app, render the index screen
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
	result = []
	
	# If inside the result path, then do the sorting and render the template (with the data)
	if request.method == 'POST':
		
		elements = request.values.getlist('element') # Gets all values of tags named 'element'
		elements_bck = elements
		groups = request.values.getlist('group') # Same as before, for tags named 'thing'
	 	
	 	sort = []

		selector = -1

		while len(elements) > 0:
			
			pos = random.randint(0,len(elements) - 1)
			selector = (selector + 1) % len(groups)
			sort = [selector, pos]
			result.append([selector, pos)
			#result.append(elements.pop(pos) + " -> " + groups[selector])
	
	return str(result)
	#return render_template('results.html', results = result, elements = elements_bck, groups = groups)