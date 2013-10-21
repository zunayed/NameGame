from flask import Flask, render_template, request, url_for, redirect, jsonify, flash
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

import random
from database import db, User
from dataprep import DataPrep
from form import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'
data = DataPrep()

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

@app.route('/about', methods = ('GET', 'POST'))
def about():
	form = ContactForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash('All Fields are Required')
			return render_template('about.html', form = form)
		else:
			return 'Form posted.'
	elif request.method == 'GET':
		return render_template('about.html', form = form)


@app.route('/check', methods = ['POST'])
def check():
	#database stuff
	db.create_all()

	ans = request.form
	ans_graded = []
	for item in ans:
		if item == ans[item]:
			modifyDatabase(item, True)
			ans_graded.append(True)
		else:
			modifyDatabase(item, False)
			ans_graded.append(False)

	return jsonify(answers = ans_graded)

def modifyDatabase(student, ans):
	student = User.query.filter_by(username = student).first()
	if ans == True:
		student.correct_picks += 1
	else:
		student.incorrect_picks += 1
	db.session.add(student)
	db.session.commit()

if __name__ == '__main__':
  app.run(debug=True)
