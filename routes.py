from flask import Flask, render_template, request, url_for, redirect, jsonify
from dataprep import DataPrep 

from flask.ext.sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine

from database import db 
from database import User

app = Flask(__name__)    

@app.route('/')
def home():
	data.getNewPeople()
	return render_template('home.html', people = data.current_random_people)

@app.route('/stats')
def stats():
	return render_template('stats.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/check', methods = ["POST"])
def check():
	#database stuff
	db.create_all()

	ans = request.form
	correct = []
	for item in ans:
		if item == ans[item]:
			modify_database(item, True)
			correct.append(True)
		else:
			modify_database(item, False)
			correct.append(False)

	return jsonify(answers=correct)

def modify_database(student, ans):
	student = User.query.filter_by(username=student).first()
	if ans == True:
		student.correct_picks += 1
	else:
		student.incorrect_picks += 1
	db.session.add(student)
	db.session.commit()


data = DataPrep()

if __name__ == '__main__':
  app.run(debug=True)