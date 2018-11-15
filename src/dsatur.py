#   DSATUR implementation

import rw_csv


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
	
		
	print(graph)
	print(degrees)
	print(index_maximum_degree)
	print(saturation_degrees)
	print(coloring)

def main():
	graph = rw_csv.read_data()
	alg_dsatur(graph)
	#print(graph)



if __name__ == "__main__":
	main()
