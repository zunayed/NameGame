from bs4 import BeautifulSoup

class DataPrep(object):
	"""docstring for DataPrep"""
	def __init__(self):
		pass
		
	def getPeople(self):
		soup = BeautifulSoup(open('students.html'))
		people = {}

		for batch in soup.find_all('ul', id = 'batch9'):
			for person in batch.find_all(class_='person'):
				for link in person.find_all(class_= 'profile-image'):
					people[person.div.get_text()] = link.get('src')

		return people

	def random_element(self, dictionary):
	    import random as r
	    return dictionary[r.choice(dictionary.keys())]

	def choose_random_elements(self, dictionary, n, choices=None):
	    if choices == None:
	        return self.choose_random_elements(dictionary, n, [])
	    elif len(choices) == n:
	        return choices
	    else:
	        element = self.random_element(dictionary)
	        if element not in choices:
	            choices.append(element)
	        return self.choose_random_elements(dictionary, n, choices)

	def output_html(self, dictionary, list):
		random_people = {}
		for item in dictionary:
			for random in list:
				if dictionary[item] == random:
					#print item
					random_people[item] = random.split('/')[-1]
					print random_people[item]
					
		
		return random_people

	def main(self):
		people = self.getPeople()
		return self.output_html(people, self.choose_random_elements(people, 4))



