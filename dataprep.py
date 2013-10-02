from bs4 import BeautifulSoup

class DataPrep(object):
	"""docstring for DataPrep"""
	def __init__(self):
		self.people_dictionary = self.getPeople()
		self.current_random_people = self.main()
		
	def getNewPeople(self):
		self.current_random_people = self.main()

	def getPeople(self):
		soup = BeautifulSoup(open('students.html'))
		people = {}

		for batch in soup.find_all('ul', id = 'batch9'):
			for person in batch.find_all(class_='person'):
				for link in person.find_all(class_= 'profile-image'):
					people[person.div.get_text()] = link.get('src')

		return people

	def random_element(self):
	    import random as r
	    return self.people_dictionary[r.choice(self.people_dictionary.keys())]

	def choose_random_elements(self, n, choices=None):
	    if choices == None:
	        return self.choose_random_elements(n, [])
	    elif len(choices) == n:
	        return choices
	    else:
	        element = self.random_element()
	        if element not in choices:
	            choices.append(element)
	        return self.choose_random_elements(n, choices)

	def output(self, list):
		random_people = {}
		for item in self.people_dictionary:
			for random in list:
				if self.people_dictionary[item] == random:
					#print item
					random_people[item] = random.split('/')[-1]
					#print random_people[item]
					
		return random_people

	def main(self):
		return self.output(self.choose_random_elements(4))