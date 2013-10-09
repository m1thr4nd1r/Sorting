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
	
	# If inside the result path, then do the sorting and render the template (with the data)
	if request.method == 'POST':
		
		elements = request.values.getlist('element') # Gets all values of tags named 'element'
		elements_bck = elements
		things = request.values.getlist('thing') # Same as before, for tags named 'thing'
		result = []

		selector = -1

		while len(elements) > 0:
			
			pos = random.randint(0,len(elements) - 1)
			selector = (selector + 1) % len(things)
			result.append(elements.pop(pos) + " -> " + things[selector])
		
		return str(result)

if __name__ == '__main__':
    app.run()