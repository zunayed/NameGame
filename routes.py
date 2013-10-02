from flask import Flask, render_template, request
from dataprep import DataPrep 

app = Flask(__name__)      
 
@app.route('/')
def home():
	#get pictures
	data = DataPrep()
	random_people = data.main() 
	return render_template('home.html', people = random_people)

@app.route('/leaderboard')
def leaderboard():
	return render_template('leaderboard.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/check', methods = ["POST"])
def check():
	ans = request.form
	correct = []
	for item in ans:
		if item == ans[item]:
			correct.append("correct")
		else:
			correct.append("incorrect")
	
	return str(correct)

if __name__ == '__main__':
  app.run(debug=True)