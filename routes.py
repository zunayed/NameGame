from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask.ext.sqlalchemy import SQLAlchemy 
from dataprep import DataPrep 

app = Flask(__name__)    
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zunayed@localhost/testdb'  
db = SQLAlchemy(app)

@app.route('/')
def home():
	ans = request.args.get('submission')
	if ans == None:
		data.getNewPeople()
		return render_template('home.html', people = data.current_random_people)
	else:
		return render_template('home.html', people = data.current_random_people, user_ans = ans)

@app.route('/stats')
def leaderboard():
	return render_template('stats.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/check', methods = ["POST"])
def check():
	ans = request.form
	correct = []
	for item in ans:
		if item == ans[item]:
			correct.append(True)
		else:
			correct.append(False)



	return jsonify(answers=correct)

data = DataPrep()
print data

if __name__ == '__main__':
  app.run(debug=True)