# Funcions necessaries pel quiosc: (nom, imatge, categoria, preu) + nombre de ventes per la cuina
from pprint import pprint

productes = [
                { "id": "cc-zero",
                  "nom":"coca-cola zero",
                  "preu": 2,
                  "categoria": "beguda"
                },
                { "id": "cc",
                  "nom":"coca-cola",
                  "preu": 2.1,
                  "categoria": "beguda"
                },
                { "id": "beer1",
                  "nom":"cervesa A",
                  "preu": 3,
                  "categoria": "beguda"
                },
                { "id": "beer2",
                  "nom":"cervesa B",
                  "preu": 3,
                  "categoria": "beguda"
                },
                { "id": "oli1",
                  "nom":"oli verge extra",
                  "preu": 20,
                  "categoria": "olis"
                },
                { "id": "beer3",
                  "nom":"cervesa C",
                  "preu": 3,
                  "categoria": "beguda"
                },
                { "id": "oli2",
                  "nom":"oli verge extra",
                  "preu": 22,
                  "categoria": "olis"
                },
                { "id": "fanta",
                  "nom":"fanta",
                  "preu": 1.5,
                  "categoria": "beguda"
                }
                ]

def afegir_producte_a_base_de_dades():
    id_prod = input("Introdueix el id del producte a afegir: ")
    nom_prod = input("Introdueix el nom del producte: ")
    preu_prod = input("Introdueix el preu del producte: ")
    categoria_prod = input("Introdueix la categoria del producte: ")
    producte = { "id": id_prod,
                  "nom": nom_prod,
                  "preu": preu_prod,
                  "categoria": categoria_prod
                }
    productes.append(producte)
    return
#afegir_producte_a_base_de_dades()
pprint(productes)