#Fucnions necessaries
#EXEMPLE
productes= [
                { "quantitat": "12",
                  "nom":"coca-cola zero",
                  "preu": 2,
                  "categoria": "beguda"
                },
                { "quantitat": "3",
                  "nom":"coca-cola",
                  "preu": 2.1,
                  "categoria": "beguda"
                },
                { "quantitat": "6",
                  "nom":"cervesa A",
                  "preu": 3,
                  "categoria": "beguda"
                },
                { "quantitat": "0",
                  "nom":"cervesa B",
                  "preu": 3,
                  "categoria": "beguda"
                },
                { "quantitat": "32",
                  "nom":"oli verge",
                  "preu": 20,
                  "categoria": "olis"
                },
                { "quantitat": "16",
                  "nom":"cervesa C",
                  "preu": 3,
                  "categoria": "beguda"
                },
                { "quantitat": "18",
                  "nom":"oli verge extra",
                  "preu": 22,
                  "categoria": "olis"
                },
                { "quantitat": "0",
                  "nom":"fanta",
                  "preu": 1.5,
                  "categoria": "beguda"
                }
                ]
#Ordenar els productes per preu
def ordena_productes(productes):
    productes = sorted(productes, key = lambda d:d["preu"])
    return productes

#Retornar productes d'una categoria
def producte_categoria(productes):
    print("Quina categoria vols buscar?")
    category=input()
    categ=category.lower()
    producte_trobat = False
    for element in productes:
      if element["categoria"]==categ:
          producte_trobat = True
          print(element["nom"], "-", element["preu"], "$", "-", element["quantitat"], "unitats disponibles")
      if not(producte_trobat):
          print("Ho sentim, no disposem d'aquesta categoria")

#Retornar cataleg de productes ordenat per preu
def cataleg(productes):
    print("~CATÀLEG~")
    for element in productes:
        print(element["nom"], "-", element["preu"], "$", "-", element["quantitat"], "unitats disponibles")

#Categories disponibles
def categories_disponibles(productes):
    llista_categories=[]
    for element in productes:
        if element["categoria"] not in llista_categories:
           llista_categories.append(element["categoria"])
    return llista_categories

print("Bon dia! Benvingut/da al Quiosc de la UPC!")
while True:
    option=input("Què vols fer? \n (A) Accedir al catàleg \n (B) Consultar les categories \n (C) Consultar productes d'una categoria \n (D) Sortir \n -->")
    if option in ['A','a']:
        productes = ordena_productes(productes)
        cataleg(productes)
        decision=input("Avisa quan vulguis tornar:\n -->")
    elif option in ['B','b']:
        llista_categories=categories_disponibles(productes)
        print(f"Llista de categories: {llista_categories}")
        decision=input("Avisa quan vulguis tornar:\n -->")
    elif option in ['C','c']:
        producte_categoria(productes)
        decision=input("Avisa quan vulguis tornar:\n -->")
    elif option in ['D','d']:
        print("Gràcies per venir!")
        break


'''
#Categoria d'un producte
def categoria_un_producte(productes, elProducte):

  # filter / lambda
    for element in productes:
        if element["nom"]==elProducte:
            categ=element["categoria"]
            return categ

    return "sense categoria"

laCategoria = categoria_un_producte(productes, "fanta")
print(laCategoria)
'''