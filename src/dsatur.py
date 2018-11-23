#   DSATUR implementation

import rw_csv
import statistics
import time

def get_neighbours_matrix(graph):
	neighbours = graph
	# deletes the first element of the list, leaving only the neighbours
	for i in range(0, len(graph)):
		del neighbours[i][0]
	return neighbours


def get_saturation_degree(node_index, neighbours, coloring):
	colors_list = set()
	# add the color of the neighbours of the node to the set
	for node in neighbours[node_index]:
		color = coloring[node-1]
		if(color != 0):
			colors_list.add(color)
	# returns the number of colors	
	return len(colors_list)
		

def alg_dsatur(graph):
	# [n][0] value of the node
	# [n][n] node's neighbours
	degrees = list()
	neighbours = get_neighbours_matrix(graph) 
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

	# coloring first node
	coloring[index_maximum_degree] = color_counter
	uncolored_nodes.remove(index_maximum_degree)

	# updates saturation
	for neighbour_node in neighbours[index_maximum_degree]:
		saturation_degrees[neighbour_node-1] = 	get_saturation_degree(neighbour_node-1, neighbours, coloring)
	
	while(len(uncolored_nodes) > 0):
		max_satur_degree = -1

		# gets maximum saturation degree
		for index in uncolored_nodes:
			if(saturation_degrees[index] > max_satur_degree):
				max_satur_degree = saturation_degrees[index]

		# gets list of indexes with max saturation degree 		
		indexes_max_satur_degree = [index for index in uncolored_nodes if saturation_degrees[index] == max_satur_degree] 		
	
		coloring_index = indexes_max_satur_degree[0]

		# if there are more than one node with the max saturation, picks the one with higher degree		
		if(len(indexes_max_satur_degree) > 1):
			maximum_degree = -1
			# finds node with maximum degree
			for index in indexes_max_satur_degree:
				if(degrees[index] > maximum_degree):
					coloring_index = index
					maximum_degree = degrees[index]
		
		# Coloring node
		for number_color in range(1, color_counter+1):
			same_color = False
			for neighbour_node in graph[coloring_index]:
				if(coloring[neighbour_node-1] == number_color):
					same_color = True
					break
			if(not(same_color)):
				coloring[coloring_index] = number_color
		
		# if node was not colored with existing colors 
		if(coloring[coloring_index] == 0):
			color_counter += 1
			coloring[coloring_index] = color_counter	 
		
		# remove node from uncolored set		
		uncolored_nodes.remove(coloring_index)		
		
		# update degree of saturation
		for neighbour_node in neighbours[coloring_index]:
			saturation_degrees[neighbour_node-1] = 	get_saturation_degree(neighbour_node-1, neighbours, coloring)
	
	print("Graph", graph)
	print("Degrees", degrees)
	print("Sat degrees", saturation_degrees)
	print("Coloring", coloring)
	return coloring


def validate_coloring(graph, coloring):
	for node_index in range(len(graph)):
		for neighbour_index in range(1, len(graph[node_index])):
			if(coloring[node_index] == coloring[graph[node_index][neighbour_index]-1]):
				return False
	return True


'''def print_stats(graph, n_colors, runtime):
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
'''

def main():
	graph = rw_csv.read_data()
	t0 = time.perf_counter()
	coloring = alg_dsatur(graph)
	time_elapsed = time.perf_counter() - t0
	#print_stats(graph, max(coloring), time_elapsed)
	rw_csv.write_colors(coloring)
	rw_csv.write_data(graph, max(coloring), time_elapsed)

if __name__ == "__main__":
	main()