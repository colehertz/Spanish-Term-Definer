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
def defineDoc(filename):

    f = open('./app/test2.csv', 'rb')

    definitions = []

    wordList = list(csv.DictReader(f))
    for word in wordList:
    	termDef = translate(word["Word"])
    	definitions.append(termDef)

    print(definitions)

    return "got it"

	#s = translate('el perro')
	#return s


