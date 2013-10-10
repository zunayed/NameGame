from bs4 import BeautifulSoup
from database import db
from database import User

def getPeople():
	soup = BeautifulSoup(open('students.html'))
	people = {}

	for batch in soup.find_all('ul', id = 'batch9'):
		for person in batch.find_all(class_='person'):
			for link in person.find_all(class_= 'profile-image'):
				people[person.div.get_text()] = link.get('src')
				student = User(person.div.get_text(), link.get('src').split('/')[-1])
				db.session.add(student)
				db.session.commit()

	return people

people_dictionary = getPeople()


