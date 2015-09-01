#!flask/bin/python
import cmd, os
import sys
import csv
import requests

class Translator(cmd.Cmd):

	"""Program to automatically define Spanish Vocab Terms in a CSV file."""

	intro = "="*55 + "\nSpanish Translator that defines a list of Vocab terms.\n" "-----\n" + "A Hersowitz Production \n" + "="*55
	prompt = '(--) '

	#class variables
	filePath = ""
	base_url = "http://127.0.0.1/"
	fileName = ""

	def do_greet(self, person):
		if person:
			print("hi, " + person)
		else:
			print("hi")

	def getFilePath():
		filePath = input("Specify the file path for the CSV containing your terms:")

	def do_setFileName(self, name):
		self.fileName = name

	def do_load(self, file):
		"""Load a CSV file containg Spanish Terms"""
		docName = "voabList.csv"
		try:
			tabReader = csv.reader( open(file, "rb"), delimiter='\t')

			if self.fileName != "":
				docName = self.fileName

			fd = open(docName, 'wb+')
			tabWriter = csv.writer(fd, delimiter='\t', quoting=csv.QUOTE_NONE)
			tabWriter.writerow(["Term", "Definition"])
			if tabReader != None :
			    for index, term in enumerate(tabReader):

			    	if (index > 0):
			    		response = requests.get(self.base_url+"translate/"+term[0])#translate(term[0])
			    		translation = response.content
			    		tabWriter.writerow([term[0], translation])
			    		print term[0] + "	-	" + translation

			fd.close()

		except IOError as e:
			print(e)

	def do_exit(self, line):
		return True

	def do_EOF(self, line):
		return True

if __name__ == '__main__':
	Translator().cmdloop()
