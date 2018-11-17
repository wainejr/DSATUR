#   DSATUR implementation

import rw_csv
import statistics
import time

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
	for neighbour_node in range(1, degrees[index_maximum_degree]+1):
		saturation_degrees[graph[index_maximum_degree][neighbour_node]-1] += 1

	# coloring first node
	coloring[index_maximum_degree] = color_counter
	uncolored_nodes.remove(index_maximum_degree)
	
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
		for neighbour_node in range(1, len(graph[coloring_index])):
			saturation_degrees[graph[coloring_index][neighbour_node] - 1] += 1
	
	# print(graph)
	# print(degrees)
	# print(index_maximum_degree)
	# print(saturation_degrees)
	# print(coloring)
	return coloring

def validate_coloring(graph, coloring):
	for node_index in range(len(graph)):
		for neighbour_index in range(1, len(graph[node_index])):
			if(coloring[node_index] == coloring[graph[node_index][neighbour_index]-1]):
				return False
	return True

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
	t0 = time.perf_counter()
	coloring = alg_dsatur(graph)
	time_elapsed = time.perf_counter() - t0
	print_stats(graph, max(coloring), time_elapsed)
	rw_csv.write_colors(coloring)
	print(coloring)
	print(validate_coloring(graph, coloring))
	#print(graph)



if __name__ == "__main__":
	main()
