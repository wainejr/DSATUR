#   for reading the .csv file that represents the graph and writing data

import csv
import statistics


PATH_FILE_R = "data/grafo06.csv"
PATH_FILE_WC = "data/grafo06_colors.csv"
PATH_FILE_WD = "data/grafo06_data.txt"


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
	with open(PATH_FILE_WC, 'w') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for i in range(0, len(coloring)):
			node_color = [i+1, coloring[i]]
			spamwriter.writerow(node_color)

def write_data(graph, n_colors, runtime):
	with open(PATH_FILE_WD, 'w') as file:
		n_nodes = len(graph)
		degrees = list()
		for node in graph:
			degrees.append(len(node)-1)
		n_edges = sum(degrees)
		min_degree = min(degrees)
		max_degree = max(degrees)
		mean_degrees = statistics.mean(degrees)
		std_dev_degrees = statistics.stdev(degrees)
		#header = ['No. nós', 'No. arestas', 'Min. grau', 'Max. grau', 'Média graus', 'Desvio padrão graus', 'No. cores', 'Run time (s)']
		#data = [n_nodes, n_edges, min_degree, max_degree, mean_degrees, std_dev_degrees, n_colors, runtime]
		#spamwriter = csv.writer(file, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		#spamwriter.writerow(header)
		#spamwriter.writerow(data)
		file.write("No. nos: \t\t" + str(n_nodes))
		file.write("\nNo. arestas: \t\t" + str(n_edges))
		file.write("\nMinimo (grau): \t\t" + str(min_degree))
		file.write("\nMaximo (grau): \t\t" + str(max_degree))
		file.write("\nMedia (grau): \t\t" + str(mean_degrees))
		file.write("\nDesvio padrao (grau): \t" + str(std_dev_degrees))
		file.write("\nNo. cores: \t\t" + str(n_colors))
		file.write("\nRun time (s): \t\t" + str(runtime))
