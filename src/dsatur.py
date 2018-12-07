#   DSATUR implementation

import rw_csv
import statistics
import time

def get_vizinhos_matriz(grafo):
	vizinhos = grafo
	# deleta o primeiro elemento de cada linha da matrix, deixando apenas os vizinhos
	for i in range(0, len(grafo)):
		del vizinhos[i][0]
	return vizinhos


def get_grau_saturacao(vertice_indice, vizinhos, coloracao):
	lista_cores = set()
	# adiciona as cores dos vizinhos a lista de cores
	for vertice in vizinhos[vertice_indice]:
		cor = coloracao[vertice-1]
		if(cor != 0):
			lista_cores.add(cor)
	# retorna o grau de saturacao (numero de cores diferentes dos vizinhos)
	return len(lista_cores)
		

def alg_dsatur(grafo):
	# [n][0] valor do vertice
	# [n][n] vertices vizinhos
	graus = list()
	vizinhos = get_vizinhos_matriz(grafo) 
	grau_saturacao = [0] * len(grafo)
	coloracao = [0] * len(grafo)
	vertices_descoloridos = set(range(len(grafo)))
	indice_grau_maximo = 0
	grau_maximo = 0
	contador_cores = 1

	# preenche os graus 
	for vertice in grafo:
		graus.append(len(vertice)-1)

	# encontra o vertice com maior grau	
	for indice in range(len(graus)):
		if(graus[indice] > grau_maximo):
			indice_grau_maximo = indice
			grau_maximo = graus[indice]

	# colore primeiro vertice
	coloracao[indice_grau_maximo] = contador_cores
	vertices_descoloridos.remove(indice_grau_maximo)

	# atualiza saturacao
	for vertice_vizinho in vizinhos[indice_grau_maximo]:
		grau_saturacao[vertice_vizinho-1] = get_grau_saturacao(vertice_vizinho-1, vizinhos, coloracao)
	
	while(len(vertices_descoloridos) > 0):
		maximo_grau_sat = -1

		# encontra maximo grau de saturacao
		for indice in vertices_descoloridos:
			if(grau_saturacao[indice] > maximo_grau_sat):
				maximo_grau_sat = grau_saturacao[indice]

		# lista de indices com grau maximo de saturacao		
		indices_maximo_grau_sat = [indice for indice in vertices_descoloridos if grau_saturacao[indice] == maximo_grau_sat] 		
	
		indice_coloracao = indices_maximo_grau_sat[0]

		# caso haja mais de um indice com grau maximo de saturacao, escolhe o de maior grau para colorir		
		if(len(indices_maximo_grau_sat) > 1):
			grau_maximo = -1
			# finds vertice with maximo grau
			for indice in indices_maximo_grau_sat:
				if(graus[indice] > grau_maximo):
					indice_coloracao = indice
					grau_maximo = graus[indice]
		
		# colore vertice
		for num_cor in range(1, contador_cores+1):
			cor_igual = False
			for vertice_vizinho in grafo[indice_coloracao]:
				if(coloracao[vertice_vizinho-1] == num_cor):
					cor_igual = True
					break
			if(not(cor_igual)):
				coloracao[indice_coloracao] = num_cor
		
		# se o vertice nao foi colorido com as cores existentes, colore com uma nova cor
		if(coloracao[indice_coloracao] == 0):
			contador_cores += 1
			coloracao[indice_coloracao] = contador_cores	 
		
		# remove vertice dos descoloridos	
		vertices_descoloridos.remove(indice_coloracao)		
		
		# atualiza grau de saturacao
		for vertice_vizinho in vizinhos[indice_coloracao]:
			grau_saturacao[vertice_vizinho-1] = get_grau_saturacao(vertice_vizinho-1, vizinhos, coloracao)
	
	#print("grafo", grafo)
	#print("graus", graus)
	#print("Sat graus", grau_saturacao)
	#print("coloracao", coloracao)
	return coloracao


def validate_coloracao(grafo, coloracao):
	for vertice_indice in range(len(grafo)):
		for vizinho_indice in range(1, len(grafo[vertice_indice])):
			if(coloracao[vertice_indice] == coloracao[grafo[vertice_indice][vizinho_indice]-1]):
				return False
	return True


def main():
	grafo = rw_csv.read_data()
	t0 = time.perf_counter()
	coloracao = alg_dsatur(grafo)
	tempo = time.perf_counter() - t0

	rw_csv.write_colors(coloracao)
	rw_csv.write_data(grafo, max(coloracao), tempo)

if __name__ == "__main__":
	main()
