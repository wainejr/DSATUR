#   DSATUR implementation

import rw_csv
import statistics

def alg_dsatur(graph):
	# graph format: [n][0] value of the node
	# 							[n][n] node's neighbours
	degrees = list()
	saturation_degrees = [0] * len(graph)
	coloring = [0] * len(graph)
	uncolored_nodes = set(range(len(graph)))
	index_maximun_degree = 0
	maximum_degree = 0
	color_counter = 1

	# fill nodes degrees 
	for node in graph:
		degrees.append(len(node)-1)

	# finds node with maximum degree	
	for index in range(len(degrees)):
		if(degrees[index] > maximum_degree):
			index_maximum_degree = index
			maximum_degree = degrees[index]

	# updates saturation
	for index in range(1, degrees[index_maximum_degree]+1):
		saturation_degrees[graph[index_maximum_degree][index]-1] += 1

	# coloring first node
	coloring[index_maximum_degree] = color_counter
	uncolored_nodes.remove(index_maximum_degree)
	
	#while(len(uncolored_nodes) > 0):
	i = 0	
	while(i < 1):
		max_satur_degree = -1
		# gets maximum saturation degree
		for index in uncolored_nodes:
			if(saturation_degrees[index] > max_satur_degree):
				max_satur_degree = saturation_degrees[index]
		# gets list of indexes with max saturation degree 		
		indexes_max_satur_degree = [index for index in uncolored_nodes if saturation_degrees[index] == max_satur_degree] 		
		# print(max_satur_degree)
		# print(indexes_max_satur_degree)
		coloring_index = indexes_max_satur_degree[0]
		# if there are more than one node with the max saturation, picks the one with higher degree		
		if(len(indexes_max_satur_degree) > 1):
			maximum_degree = -1
			# finds node with maximum degree
			for index in indexes_max_satur_degree:
				if(degrees[index] > maximum_degree):
					coloring_index = index
					maximum_degree = degrees[index]
		print(coloring_index)
		# print(degrees)
		
		# Coloring node
		for number_color in range(1, color_counter+2):
			same_color = False
			for neighbour_node in graph[coloring_index]:
				if(coloring[neighbour_node-1] == number_color):
					same_color = True
					break
			if(not(same_color)):
				print("aqui", color_counter)
				coloring[coloring_index] = number_color
		
		# if number_color is a new color 
		if(coloring[coloring_index] > color_counter):
			color_counter += 1				 
		
		print(coloring)
		print(color_counter)
		i += 1
	# print(graph)
	# print(degrees)
	# print(index_maximum_degree)
	# print(saturation_degrees)
	# print(coloring)

def print_stats(graph, n_colors, runtime):
	n_nodes = len(graph)
	degrees = list()	
	for node in graph:
		degrees.append(len(node)-1)
	n_edges = sum(degrees)
	min_degree = min(degrees)
	max_degree = max(degrees)
	mean_degrees = statistics.mean(degrees)
	std_dev_degrees = statistics.stdev(degrees)
	
	print("Number of nodes: \t", n_nodes)
	print("Number of edges: \t", n_edges)
	print("Min. Degree: \t\t", min_degree)
	print("Max. Degree: \t\t", max_degree)
	print("Mean: \t\t\t", mean_degrees)	
	print("Std deviation: \t\t", std_dev_degrees)
	print("Number of colors: \t", n_colors)
	print("Runtime: \t\t", runtime)	

def main():
	graph = rw_csv.read_data()
	alg_dsatur(graph)
	print_stats(graph, 100, 100)
	#print(graph)



if __name__ == "__main__":
	main()
