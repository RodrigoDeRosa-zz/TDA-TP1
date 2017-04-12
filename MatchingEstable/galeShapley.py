import Queue

def galeShapley(A, E):
	"""
	Resuelve el problema de perfect matching para los dos arreglos A y E recibidos,
	con |A| = |E|
	"""
	n = len(A) #Tamaño de los arreglos
	sig_deseado = [0]*n #Se inicializa con 0 todos los desados
	H = [None]*n #Lista de parejas vacia
	pendientes = Queue.Queue(n) #Cola de valores por visitar
	preferencia = []

	e_actual = 0
	lista_e = []
	for i in range n:
		lista_e.append(E[e_actual].index(i))
		e_actual += 1

	while not pendientes.empty():
		a = pendientes.get()
		e_d = A[a][sig_deseado[a]]
		sig_deseado[a] += 1
		a_rival = H[e_d]

		if a_rival is None:
			H[e_d] = a
		elif preferencia[e_d][a_rival] < preferencia[e_d][a]:
			H[e_d] = a
			pendientes.put(a_rival)
		else:
			pendientes.put(a)

	return H
