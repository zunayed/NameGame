from flask import Flask, render_template, request, url_for, redirect, Response
from dataprep import DataPrep 

app = Flask(__name__)      

@app.route('/')
def home():
	ans = request.args.get('submission')
	if ans == None:
		data.getNewPeople()
		return render_template('home.html', people = data.current_random_people)
	else:
		return render_template('home.html', people = data.current_random_people, user_ans = ans)

@app.route('/leaderboard')
def leaderboard():
	return render_template('leaderboard.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/check', methods = ["POST"])
def check():
	ans = request.form
	correct = ''
	for item in ans:
		if item == ans[item]:
			correct += 't'
		else:
			correct += 'f'

	return Response(correct)

data = DataPrep()
print data

if __name__ == '__main__':
  app.run(debug=True)