from pprint import pprint
from productes import productes
from categories import *

# Configuració inicial
num_prestatges_camera = 4
num_prestatges_despensa = 4
num_nivells = 4 # Nombre de nivells
num_safates = 4 # Nombre de safates en una casella
capacitat_safata = 4 #Nombre d'elements que hi caben en una safata

#Funcions Necessaries:

#Funció Per afegir productes. Li ha d'entrar, categoria, Producte i quantitat.

#Funció per obtenir produces per posició? Varis productes a l'hora?

#Buscar producte per la cuina lifo

#Retirar productes per la cuina


# Creem una matriu tridimensional (amb nombre de nivells i prestatges, i nombre de safates per casella)
# Tal com hem plantejat el codi, cada safata serà una llista, el primer element serà la
# categoria dels productes, i el segon element serà la llista dels productes (només guardem la id del producte)
# Exemple de safata: ["beguda", ["cc", "cc", "beer1"]]
def inicialitzar_despensa():
    # despensa = [[[1,2,3],[4,5,6],[7,8,9]],
    #            [[10,11,12],[13,14,15],[16,17,18]],
    #            [[19,20,21],[22,23,24],[25,26,27]]]
    #Fa el mateix que abans però amb les dimensions correctes
    despensa = [[[[] for safata in range(num_safates)] for nivell in range(num_nivells)] for prestatges in range(num_prestatges_despensa)]
    return despensa

def inicialitzar_camera():
    # despensa = [[[1,2,3],[4,5,6],[7,8,9]],
    #            [[10,11,12],[13,14,15],[16,17,18]],
    #            [[19,20,21],[22,23,24],[25,26,27]]]
    #Fa el mateix que abans però amb les dimensions correctes
    camera = [[[[] for safata in range(num_safates)] for nivell in range(num_nivells)] for prestatges in range(num_prestatges_camera)]
    return camera

# Quan busquem un producte amb una certa id al magatzem, primer hem de saber a quina categoria pertany
def buscar_categoria(id_producte):
     for product in productes:
        if product["id"] == id_producte:
            return product["categoria"]

# Actualment a cada casella hi pot haver una única categoria de productes, col·loquem els productes a la primera posició disponible
# De moment no mirem res més (com que a un mateix nivell només hi pot haver una categoria)
def coloca_producte(despensa, camera, id_producte):

    zona_magatzem_nom = determinar_zona_magatzem(id_producte)

    if zona_magatzem_nom == "despensa":
        zona_magatzem = despensa
    else:
        zona_magatzem = camera
    
    #busquem la categoria del producte que volem col·locar
    categoria = buscar_categoria(id_producte)

    # Recorrem de dalt a l'esquerra a baix a la dreta
    for estanteria in zona_magatzem:
        for nivell in estanteria:
                for safata in nivell:
                    # Si la safata està buida, no té cap categoria o producte, l'afegim aquí i acabem
                    if len(safata) == 0:
                         safata.append(categoria)
                         safata.append([id_producte])
                         return
                    # Si la categoria de la safata no correspon al producte que volem col·locar, 
                    # anem a la següent casella directament, no cal mirar les safates de darrere
                    if categoria != safata[0]:
                        break
                    # Si a la safata hi caben productes i la categoria és correcte, l'afegim, sino continuarem a la següent safata
                    if len(safata[1]) < capacitat_safata:
                        safata[1].append(id_producte)
                        return
    
    if zona_magatzem_nom == "despensa":
        despensa = zona_magatzem
    else:
        camera = zona_magatzem


# Aquesta funció retorna la primera posició del producte que volem buscar
# Exemple: [0,1,0,2] vol dir estanteria 0, nivell 1, safata 0 i agafem la coca-cola número 2
def buscar_producte(despensa, camera, id_producte):
     
     categoria = buscar_categoria(id_producte)

     zona_magatzem_nom = determinar_zona_magatzem(id_producte)

     if zona_magatzem_nom == "despensa":
        zona_magatzem = despensa
     else:
        zona_magatzem = camera

     estanteria_index = 0
     nivell_index = 0
     safata_index = 0
     producte_index = 0

     for estanteria in zona_magatzem:
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

# Quan es vulgui afegir o treure un producte li passarem la id i ens dirà si correspon a la despensa o la camera
def determinar_zona_magatzem(id_producte):
    
    categoria = buscar_categoria(id_producte)

    # categories_despensa = ["begudes", "olis", "peixos", "vegetals", "snacks", "salses", "lactics", "llegums_arrossos_pasta"]
    # categories_camera = ["postres", "iogurts", "carns", "fruites", "embotits", "formatges", "verdures"]

    if categoria in CATEGORIES_DESPENSA:
        return "despensa"
    elif categoria in CATEGORIES_CAMERA:
        return "camera"
    else:
        print("La categoria no és correcta")

#Li diem una safata concreta i retorna la llista dels productes
def obtenir_productes_safata(prestatge_index, nivell_index, safata_index, zona_magatzem):
    
    if zona_magatzem == "despensa":
        return despensa[prestatge_index][nivell_index][safata_index]
    
    else:
        return camera[prestatge_index][nivell_index][safata_index]


def retirar_producte(despensa, camera, id_producte):
    producte = buscar_producte(despensa, camera, id_producte)

    zona_magatzem_nom = determinar_zona_magatzem(id_producte)

    if zona_magatzem_nom == "despensa":
        zona_magatzem = despensa
    else:
        zona_magatzem = camera

    zona_magatzem[producte[0]][producte[1]][producte[2]][1].pop(producte[3])

    #print(despensa[llista[0]][llista[1]][llista[2]][1][llista[3]])

    if zona_magatzem_nom == "despensa":
        despensa = zona_magatzem
    else:
        camera = zona_magatzem
    
    


# CODI PRINCIPAL
despensa = inicialitzar_despensa()
camera = inicialitzar_camera()

coloca_producte(despensa, camera, "cc")
coloca_producte(despensa, camera, "oli1")
coloca_producte(despensa, camera, "cc")
coloca_producte(despensa, camera, "cc")
coloca_producte(despensa, camera, "oli2")
coloca_producte(despensa, camera, "cc")
coloca_producte(despensa, camera, "cc")
coloca_producte(despensa, camera, "oli1")
coloca_producte(despensa, camera, "cc")
coloca_producte(despensa, camera, "cc")
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

# print(despensa[0][1][0])
                     
# print(buscar_producte(despensa, camera, "oli2"))

# print(obtenir_productes_safata(0,1,0,"despensa"))
                     

retirar_producte(despensa, camera, "oli1")
pprint(despensa)
# lista = ['olis', ['oli1', 'oli2', 'oli3']]

# print(lista[1][0])
# lista[1].pop(0)
# print(lista)

# llista = [0, 1, 0, 2]

# print(despensa[llista[0]][llista[1]][llista[2]][1][llista[3]])