from pprint import pprint
from productes import productes
from categories import *

from magatzem import coloca_producte, inicialitzar_magatzem, retirar_producte, buscar_producte, determinar_zona_magatzem, obtenir_productes_safata
from productes import afegir_producte_a_base_de_dades
from magatzem import coloca_producte, inicialitzar_magatzem, retirar_producte, buscar_producte, determinar_zona_magatzem, obtenir_productes_safata
from productes import afegir_producte_a_base_de_dades

print("Per inicialitzar el magatzem introdueix les seguents dades: ")
num_prestatges_despensa = int(input("Introdueix el nombre de prestatges de la despensa: "))
num_prestatges_camara = int(input("Introdueix el nombre de prestatges de la camara frigorifica: "))
num_nivells = int(input("Introdueix el nombre de nivells per prestatge: "))
num_safates = int(input("Introdueix el nombre de safates per nivell: "))
despensa = inicialitzar_magatzem(num_safates,num_nivells,num_prestatges_despensa)
camera = inicialitzar_magatzem(num_safates,num_nivells,num_prestatges_camara)

productes_actualitzats = productes

coloca_producte(despensa, camera, "cc", productes_actualitzats)
coloca_producte(despensa, camera, "oli1", productes_actualitzats)
coloca_producte(despensa, camera, "cc", productes_actualitzats)
coloca_producte(despensa, camera, "cc", productes_actualitzats)
coloca_producte(despensa, camera, "oli2", productes_actualitzats)
coloca_producte(despensa, camera, "cc", productes_actualitzats)
coloca_producte(despensa, camera, "cc", productes_actualitzats)
coloca_producte(despensa, camera, "oli1", productes_actualitzats)
coloca_producte(despensa, camera, "cc", productes_actualitzats)
coloca_producte(despensa, camera, "cc", productes_actualitzats)
operacio = -1

while operacio != 0:
    print("Quina operació vols realitzar? (0, 1, 2, 3, 4) ")
    print("0- Sortir del menú")
    print("1- Mostrar la despensa")
    print("2- Afegir nou producte a la base de dades")
    print("3- Afegir producte a la despensa o a la camara")
    print("4- Eliminar producte de la despensa o de la camara")
    print("5- Mostrar llista de productes disponibles")
    print("6- Buscar ubicació del producte al magatzem")
    print("7- Obtenir llistat de productes de una safata")
    print("")
    operacio = int(input(""))
    if operacio == 1:
        pprint(despensa)
    if operacio == 2:
        productes_actualitzats = afegir_producte_a_base_de_dades()
        print("Operació Realitzada correctament")
    if operacio == 3:
        id_producte_afegir = input("Introdueix en id del producte a afegir (Si no esta a la base de dades -> 2): ")
        coloca_producte(despensa, camera, id_producte_afegir, productes_actualitzats)
        print("Operació Realitzada correctament")
    if operacio == 4:
        id_producte_retirar = input("Introdueix en id del producte a retirar (El producte ha de estar al cataleg -> 1): ")
        retirar_producte(despensa, camera, id_producte_retirar, productes_actualitzats)
        print("Operació Realitzada correctament")
    if operacio == 5:
        pprint(productes_actualitzats)
        print("Operació Realitzada correctament")
    if operacio == 6:
        id_producte = input("Introdueix l'id del producte que desitja buscar: ")
        zona_magatzem = determinar_zona_magatzem(id_producte, productes_actualitzats)
        [estanteria_index, nivell_index, safata_index, producte_index] = buscar_producte(despensa, camera, id_producte, productes_actualitzats)
        print(f"El producte amb id {id_producte} el pots trobar a la {zona_magatzem}, "
    f"a la prestatgeria {estanteria_index}, nivell {nivell_index}, safata {safata_index}.")
    if operacio == 7:
        zona_magatzem = input("En quina zona està el producte (despensa o camera)? ")
        prestatge_index = int(input("A quin prestatge està la safata? "))
        nivell_index = int(input("A quin nivell està la safata? "))
        safata_index = int(input("En quina posició està la safata? "))

        productes_safata = obtenir_productes_safata(prestatge_index, nivell_index, safata_index, zona_magatzem, despensa, camera)
        print(productes_safata)
    if operacio <0 or operacio>7:
        print("Numero incorrecte")

#pprint(despensa)
#retirar_producte(despensa, camera, "oli1")
#pprint(despensa)