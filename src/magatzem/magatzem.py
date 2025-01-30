# Configuració inicial
num_prestatges_frigo = 4
num_prestatges_despensa = 12
num_nivells = 5 # No coneixem el número de Nivells
num_safates = 10 # No coneixem el número de safates, són il·limitades?

# Funció per Inicialitzar el magatzem
# Matrius tridimensionals (3D) per representar els prestatges, nivells i safates.
# Ordre LIFO (Last In, First Out)
camera_frigorifica = [[[[] for _ in range(num_safates)] for _ in range(num_nivells)] for _ in range(num_prestatges_frigo)]

despensa = [[[[] for _ in range(num_safates)] for _ in range(num_nivells)] for _ in range(num_prestatges_despensa)]


#Funcions Necessaries:

#Funció Per afegir productes. Li ha d'entrar, categoria, Producte i quantitat.

#Funció per obtenir produces per posició? Varis productes a l'hora?

#Buscar producte per la cuina lifo

#Retirar productes per la cuina

