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
def cataleg(productes)
    print("~CATÀLEG~")
    for element in productes:
        print(element["nom"], "-", element["preu"], "$", "-", element["quantitat"], "unitats disponibles")

#Encarrecs realitzats per un usuari
#Encarrec. Pex: Usuari Joan - 5 Colacaos i 3 arros. Sumar al contador de encarrecs de cada producte.

#Registrar usuaris amb base de dades
base_dades=[{"nom":"Carlota","naixement":"2005","telefon":"652900676"}]
def registrar_usuari(base_dades):
  usuari = input("Registre d'usuari. Benvingut! Escrigui el seu nom d'usuari: ")
  any_neixament = input('Escrigui el seu any de neixament: ')
  telèfon = input('Escrigui el seu número de telèfon: ')
  print('Usuari registrat amb éxit')
  nou_usuari={"nom":usuari,"naixement":any_neixament,"telefon":telèfon}
  base_dades=base_dades.append(nou_usuari)
  return base_dades

#Categories disponibles
def categories_disponibles(productes):
    llista_categories=[]
    for element in productes:
        if element["categoria"] not in llista_categories:
           llista_categories.append(element["categoria"])
    print(f"Llista de categories: {llista_categories}")

#Categoria d'un producte
def categoria_un_producte(productes):
    print("Quin producte del catàleg vols buscar?")
    product=input()
    prod=product.lower()
    for element in productes:
        if element["nom"]==prod:
           categ=element["categoria"]
           print(f"El producte {prod} és de la categoria {categ}.")