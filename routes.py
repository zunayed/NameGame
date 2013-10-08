from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask.ext.sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine

import pdb
import random
from database import db, User 
from dataprep import DataPrep 

app = Flask(__name__)    

@app.route('/')
def home():
	data.getNewPeople()
	shuffled = []
	for item in data.current_random_people:
		shuffled.append(item)

	random.shuffle(shuffled)

	return render_template('home.html', people = data.current_random_people, shuffled_names = shuffled)

@app.route('/stats')
def stats():
	students = User.query.all()
	student_stats = {}
	for student in students:
		total_plays = student.incorrect_picks + student.correct_picks + 1 
		percentage = (float(student.correct_picks) / total_plays) * 100
		student_stats[student.username] = round(percentage, 0)

	return render_template('stats.html', stats = student_stats)

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
			modifyDatabase(item, True)
			correct.append(True)
		else:
			modifyDatabase(item, False)
			correct.append(False)

	return jsonify(answers=correct)

def modifyDatabase(student, ans):
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