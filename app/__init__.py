import requests
import csv
from bs4 import BeautifulSoup
from flask import Flask


app = Flask(__name__)

@app.route('/translate/<term>')
def translate(term):
	
	page = requests.get('http://www.spanishdict.com/translate/'+term)
	
	parsedHtml = BeautifulSoup(page.content)

	results = parsedHtml.find_all("span", class_="dictionary-neodict-translation-translation click-to-translate-section")


	for result in results:
		return ''.join(result.findAll(text=True))

	return "TERM NOT FOUND"


@app.route('/conjugate/<verb>/present')
def conjugatePresent(verb):

	page = requests.get('http://www.spanishdict.com/translate/' + verb)

	soup = BeautifulSoup(page.content)

	results = soup.find_all("")

@app.route('/define/document/<filename>')
def writeDefinitions(filename):
	try:
		tabReader = csv.reader( open("./app/test2.csv", "rb"), delimiter='\t')
		fd = open('./app/list.csv', 'wb+')
		tabWriter = csv.writer(fd, delimiter='\t', quoting=csv.QUOTE_NONE)
		tabWriter.writerow(["Term", "Definition"])
		if tabReader != None :
		    for index, term in enumerate(tabReader):

		    	if (index > 0):
		    		print term[0]
		    		print translate(term[0])
		    		translation = translate(term[0])
		    		tabWriter.writerow([term[0], translation])

		        #term.append("new_thing")
		        #tabWriter.writerow(term)
		fd.close()
		return "SUCCESS"

	except Exception,e :
		return "Exception : " + str(e)



