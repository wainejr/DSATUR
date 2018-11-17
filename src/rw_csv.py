#   file for reading the .csv file 
#   that represents the graph

import csv

PATH_FILE_R = "data/grafo06.csv"
PATH_FILE_W = "data/grafo06_colors.csv"

def read_data():
	data = []	
	with open(PATH_FILE_R) as csvfile:
		f = csv.reader(csvfile, delimiter=',')
		for row in f:
			# print(row)
			data.append(list(map(int, row)))
	# print(data)
	csvfile.close()
	return data

def write_colors(coloring):
	with open(PATH_FILE_W, 'w') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow(coloring)
