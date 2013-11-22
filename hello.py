import os
import random
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

app = Flask(__name__)
app.debug = True  # Activating Debug of the App
app.secret_key = 'Candy_land'

@app.route('/')
def hello():
	# If on the root of the app, render the index screen
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
	# If inside the result path, then do the sorting and render the template (with the data)
	if request.method == 'POST':
		
		elements = request.values.getlist('element') # Gets all values of tags named 'element'
		groups = request.values.getlist('group') # Same as before, for tags named 'thing'
	 	
	 	# If there isn't any groups or elements then return to index, otherwise keep going
 	 	if len(groups) == 0:
	 		flash("No groups added")
	 		return redirect(url_for('hello')) 
	 	elif len(elements) == 0:
	 		flash("No elements added")
 			return redirect(url_for('hello'))			
	 	else:
			# removing white spaces at the beginning and the end of both lists
	 		g = map(str.strip, map(str, groups))
	 		e = map(str.strip, map(str, elements))

	 		# if there is any empty element on any of the lists go to the index, otherwise keep going
 			if '' in g:
	 			flash("Empty Group")
	 			return redirect(url_for('hello'))
	 		elif '' in e:
	 			flash("Empty Element")
 				return redirect(url_for('hello'))
	 		else:
	 			# initialize the variables
	 		 	result = [[] for i in range(0,len(groups))]
			 	sort = []

				selector = -1
				
				while len(elements) > 0:
					pos = random.randint(0,len(elements) - 1)
					selector = (selector + 1) % len(groups)
					result[selector].append(elements.pop(pos))
				
				return render_template('results.html', results = result, groups = groups)
	else:
		return render_template('404.html')
	
	#Como salvar no banco:
	# Elemento | Grupo | Data/Hora que o sorteio foi realizado