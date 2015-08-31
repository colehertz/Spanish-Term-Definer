csvFile = open('test.csv')

try:
    reader = csv.reader(csvFile)
    for row in reader:
        print row
finally:
    csvFile.close()