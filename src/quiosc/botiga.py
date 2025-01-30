# Variables
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

#Ordenador de preus
def ordena_productes(productes):
    productes = sorted(productes, key = lambda d:d["preu"])
    return productes

#Catàleg
def cataleg(productes):
    print("~CATÀLEG~")
    for element in productes:
      print(element["nom"], "-", element["preu"], "$", "-", element["quantitat"], "unitats disponibles")

#Categories existents
def categories_disponibles(productes):
    llista_categories=[]
    for element in productes:
        if element["categoria"] not in llista_categories:
           llista_categories.append(element["categoria"])
    return llista_categories

#Categoria d'un producte
def categoria_un_producte(productes, elProducte):
    for element in productes:
        if element["nom"]==elProducte:
            categ=element["categoria"]
            return categ
    return "No disposem d'aquest producte"

#Productes d'una categoria
def producte_categoria(productes, category):
    producte_trobat = False
    for element in productes:
      if element["categoria"]==category:
          producte_trobat = True
          print(element["nom"], "-", element["preu"], "$", "-", element["quantitat"], "unitats disponibles")
      if not(producte_trobat):
          print("Ho sentim, no disposem d'aquesta categoria")

#Registre d'usuari a la base de dades
def registrar_usuari(usuari, any, telefon):
  print('Usuari registrat amb éxit')
  perfil={"Nom usuari":{usuari}, "Any neixament": {any}, "Contacte": {telefon} }
  return perfil

#Proves

#productes=ordena_productes(productes)
#cataleg(productes)


#llista_categories=categories_disponibles(productes)
#print(llista_categories)


#laCategoria = categoria_un_producte(productes,"xocolata")
#print(laCategoria)


#producte_categoria(productes,"beguda")


#perfil=registrar_usuari("Xavi", 2005, 123456789)
#print(perfil)