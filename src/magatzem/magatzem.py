from pprint import pprint
from productes import productes

# Configuració inicial
num_prestatges_frigo = 4
num_prestatges_despensa = 4
num_nivells = 4 # No coneixem el número de Nivells
num_safates = 4 # No coneixem el número de safates, són il·limitades?
capacitat_safata = 4 #Nombre d'elements que hi ha en una safata

# Funció per Inicialitzar el magatzem
# Matrius tridimensionals (3D) per representar els prestatges, nivells i safates.
# Ordre LIFO (Last In, First Out)

#print(productes)



# despensa = [[[1,2,3],[4,5,6],[7,8,9]],
#            [[10,11,12],[13,14,15],[16,17,18]],
#            [[19,20,21],[22,23,24],[25,26,27]]]
#Fa el mateix que abans però amb les dimensions correctes
despensa = [[[[] for safata in range(num_safates)] for nivell in range(num_nivells)] for prestatges in range(num_prestatges_despensa)]

def buscar_categoria(despensa,id_producte):
     for product in productes:
        if product["id"] == id_producte:
            return product["categoria"]

def coloca_producte(despensa, id_producte):
    
    categoria = buscar_categoria(despensa, id_producte)

    for estanteria in despensa:
        for nivell in estanteria:
                for safata in nivell:
                    if len(safata) == 0:
                         safata.append(categoria)
                         safata.append([id_producte])
                         return
                    if categoria != safata[0]:
                        break
                    if len(safata[1]) < capacitat_safata:
                        #l = [id_producte]
                        safata[1].append(id_producte)
                        #safata[1] = "test2"
                        return

coloca_producte(despensa, "cc")
coloca_producte(despensa, "oli1")
coloca_producte(despensa, "cc")
coloca_producte(despensa, "cc")
coloca_producte(despensa, "oli1")
coloca_producte(despensa, "cc")
coloca_producte(despensa, "cc")
coloca_producte(despensa, "oli2")
coloca_producte(despensa, "cc")
coloca_producte(despensa, "cc")
# coloca_producte(despensa, "oli1")
# coloca_producte(despensa, "cc")
# coloca_producte(despensa, "cc")
# coloca_producte(despensa, "oli1")
# coloca_producte(despensa, "cc")
# coloca_producte(despensa, "cc")
# coloca_producte(despensa, "cc")
# coloca_producte(despensa, "cc")
# coloca_producte(despensa, "cc")
# coloca_producte(despensa, "cc")
# coloca_producte(despensa, "cc")
# coloca_producte(despensa, "cc")
# coloca_producte(despensa, "cc")
# coloca_producte(despensa, "cc")
# coloca_producte(despensa, "cc")
pprint(despensa)



def buscar_producte(despensa, id_producte):
     
     categoria = buscar_categoria(despensa, id_producte)

     estanteria_index = 0
     nivell_index = 0
     safata_index = 0
     producte_index = 0

     for estanteria in despensa:
        for nivell in estanteria:
            for safata in nivell:
                if safata and safata[0] == categoria:

                        for producte in safata[1]:
                            if id_producte == producte:
                                return [estanteria_index, nivell_index, safata_index, producte_index]
                            producte_index += 1
                        producte_index = 0
                safata_index += 1
            nivell_index += 1
            safata_index = 0
        estanteria_index += 1
        nivell_index = 0
                     
print(buscar_producte(despensa, "oli2"))
                     

#Funcions Necessaries:

#Funció Per afegir productes. Li ha d'entrar, categoria, Producte i quantitat.

#Funció per obtenir produces per posició? Varis productes a l'hora?

#Buscar producte per la cuina lifo

#Retirar productes per la cuina

