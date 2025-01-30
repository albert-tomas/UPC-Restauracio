from pprint import pprint
from productes import productes
from categories import *
from magatzem import  *
from src.magatzem.productes import afegir_producte_a_base_de_dades

print("Per inicialitzar el magatzem introdueix les seguents dades: ")
num_prestatges_despensa = int(input("Introdueix el nombre de prestatges de la despensa: "))
num_prestatges_camara = int(input("Introdueix el nombre de prestatges de la camara frigorifica: "))
num_nivells = int(input("Introdueix el nombre de nivells per prestatge: "))
num_safates = int(input("Introdueix el nombre de safates per nivell: "))
despensa = inicialitzar_despensa(num_safates,num_nivells,num_prestatges_despensa)
camera = inicialitzar_despensa(num_safates,num_nivells,num_prestatges_camara)

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
operacio = -1

while ( operacio != 0):
    print("Quina operació vols realitzar? (0, 1, 2, 3, 4) ")
    print("0- Sortir del menú")
    print("1- Mostrar la despensa")
    print("2- Afegir nou producte a la base de dades")
    print("3- Afegir producte a la despensa o a la camara")
    print("4- Eliminar producte de la despensa o de la camara")
    print("")
    operacio = int(input(""))
    if (operacio == 1):
        pprint(despensa)
    if (operacio == 2):
        afegir_producte_a_base_de_dades()
        print("Operació Realitzada correctament")
    if (operacio == 3 ):
        id_producte_afegir = input("Introdueix en id del producte a afegir (Si no esta a la base de dades -> 2): ")
        coloca_producte(despensa, camera, id_producte_afegir)
        print("Operació Realitzada correctament")
    if (operacio == 4):
        id_producte_retirar = input("Introdueix en id del producte a retirar (El producte ha de estar al cataleg -> 1): ")
        retirar_producte(despensa, camera, id_producte_retirar)
        print("Operació Realitzada correctament")
    if (operacio <0 or operacio>4):
        print("Numero incorrecte")

#pprint(despensa)
#retirar_producte(despensa, camera, "oli1")
#pprint(despensa)