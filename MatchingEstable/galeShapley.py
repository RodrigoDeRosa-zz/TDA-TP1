import Queue

def galeShapley(A, E):
	"""
	Algoritmo de Gale & Shapley para la resolucion del problema de perfect
	matching.
		- A : Lista con listas de preferencias de cada aplicante, en su indice.
		- E : Lista con listas de preferencias de cada reviewer, en su indice.
	"""
	n = len(A) #Cantidad de aplicantes
	pendientes = setQueue(n); #Cola de aplicantes por proponerse
	H = [None]*n #Lista de matching --> H[e] = aplicante asociado a e
	sigDeseado = [0]*n #Posicion del proximo reviewer a proponerse de ai
	preferencia = setPreferenceDict(E, n) #Diccionario de preferencias de cada reviewer

	while not pendientes.empty():
		aplicante = pendientes.get()
		reviewerDeseado = A[aplicante][sigDeseado[aplicante]]
		sigDeseado[aplicante] += 1 #Si tiene que volver a proponerse, sera al proximo de la lista

		aplicanteRival = H[reviewerDeseado] #Aplicante aceptado previamente

		if aplicanteRival is None:
			#Si todavia no habia rival, se define al aplicante como el asociado al reviewer
			H[reviewerDeseado] = aplicante
		elif preferencia[reviewerDeseado][aplicanteRival] > preferencia[reviewerDeseado][aplicante]:
			#Si el reviewer prefiere al aplicante, se cambia
			H[reviewerDeseado] = aplicante
			pendientes.put(aplicanteRival) #El rival debe buscar una nueva pareja
		else:
			pendientes.put(aplicante) #Espera su turno para proponersele al proximo en la lista
	return setCoupleList(H)

def galeShapleyVacants(A, E, Q):
	"""
	Algoritmo de Gale & Shapley para la resolucion del problema de perfect
	matching con cantidad de vacantes por reviewer distinto de 1.
		- A : Lista con listas de preferencias de cada aplicante, en su indice.
		- E : Lista con listas de preferencias de cada reviewer, en su indice.
		- Q : Lista con las vacantes del hospital que corresponde al indice.
	"""
	n = len(A) #Cantidad de aplicantes
	pendientes = setQueue(n); #Cola de aplicantes por proponerse
	H = [] #Lista de matching --> H[e] = lista de aplicantes aceptados
	for i in xrange(n):
		H.append([])
	sigDeseado = [0]*n #Posicion del proximo reviewer a proponerse de ai
	preferencia = setPreferenceDict(E, n) #Diccionario de preferencias de cada reviewer

	while not pendientes.empty():
		aplicante = pendientes.get()

		reviewerDeseado = A[aplicante][sigDeseado[aplicante]]
		sigDeseado[aplicante] += 1 #Si tiene que volver a proponerse, sera al proximo de la lista

		cantidadAceptados = len(H[reviewerDeseado])

		if cantidadAceptados < Q[reviewerDeseado]:
			#Si todavia hay vacantes en el hospital, se agrega.
			H[reviewerDeseado].append(aplicante)
		else:
			#Se debe chequear si alguno de los aplicantes tiene menor preferencia que el nuevo
			rival = getMinPreferenceRival(preferencia, reviewerDeseado, H[reviewerDeseado])
			if preferencia[reviewerDeseado][rival] > preferencia[reviewerDeseado][aplicante]:
				H[reviewerDeseado].remove(rival)
				H[reviewerDeseado].append(aplicante)
				pendientes.put(rival)
			else:
				pendientes.put(aplicante) #Espera su turno para proponersele al proximo en la lista
	return setCoupleList(H)

def setQueue(n):
	"""
	Crea una cola con los numeros del 0 a n.
	"""
	queue = Queue.Queue();
	for i in xrange(n):
		queue.put(i)
	return queue

def setPreferenceDict(E, n):
	"""
	Crea un diccionario en el que se guarda el ranking de cada reviewer:
		pref[ei][ai] = posicion de ai en el ranking de ei
	"""
	return dict( (e, dict( (a, E[e].index(a)) for a in xrange(n))) for e in xrange(n) ) #He aqui la magia de python

def getMinPreferenceRival(preferencia, deseado, rivales):
	"""
	Devuelve el rival de menor preferencia para el reviewer deseado
		- preferencia : Diccionario de preferencias de todos los reviewers
		- deseado : Reviewer al que se quiere proponer
		- rivales : Lista de aplicantes rivales
	"""
	menor = rivales[0]
	rival = menor
	for i in xrange(1, len(rivales)):
		rival = rivales[i]
		if preferencia[deseado][rival] > preferencia[deseado][menor]:
			menor = rival
	return rival

def setCoupleList(H):
	"""
	Crea una lista de cuplas con el resultado dado por el matching:
		[(e0, [ai, ..., ak]), ... , (en, [aj, ..., an]), ...]
	"""
	couples = []
	for i in xrange(len(H)):
		couple = (i, H[i])
		couples.append(couple)
	return couples
