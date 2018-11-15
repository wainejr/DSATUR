#   file for reading the .csv file 
#   that represents the graph

import csv

PATH_FILE = "data/grafo06.csv"

def read_data():	
	data = []	
	with open(PATH_FILE) as f:
		f = csv.reader(f, delimiter=',')
		for row in f:
			# print(row)
			data.append(list(map(int, row)))
	# print(data)
	return data
'''
	f = open(PATH_FILE, "r")
	content = f.read()
	print("Aqui")
	print (content)
	f.close()
'''
