usuaris = [
    {
    "nom": "carlota",
    "comandes": []
    },
    {
      "nom": "xavi",
      "comandes":[
            {"comanda" : "coca-cola",
            "quantitat" : 1},
           {"comanda": "oli",
            "quantitat": 2}]
    }]

#entrem ja uns usuaris manualment, amb unes comandes inicials

def encarrec(usuaris, nomUsuari, laComanda):
  usuari = "carlota"
  usuari.append(laComanda)

# definim una funció encarrec amb les variables del vector usaris per anar afegint els nous encàrrecs, 
#l'usuari que fa l'encarrec i la comanda amb les quantitas que vol

comanda = [{"comanda" : "coca-cola",
            "quantitat" : 2},
           {"comanda": "oli",
            "quantitat": 1}]

def encarrec(usuaris, nomUsuari, laComanda):
  for u in usuaris:
    if u["nom"] == nomUsuari:
      for element in comanda:
        u['comandes'].append(element)

encarrec(usuaris,"carlota", comanda)
print(usuaris)



# Proves encàrrec
'''
from src.magatzem.productes import productes

  def encarrec(productes):
    nom_usuari = input("Indiqui el seu nom d'usuari: ")
    veure_catleg = input( " Vols veure el cataleg? ")
    veure_cataleg=veure_catleg.lower()
    if veure_cataleg== "si" or veure_cataleg == "sí": cataleg(productes)
    comanda=[]; quantitats=[];
    continuar="si"
    while continuar=="si" or continuar=="sí" :
          comanda1 = input("Que vols demanar?" )
          quantitat1 = input("Quantes vols?" )
          comanda=comanda.append(comanda1)
          quantitats=quantitats.append(quantitat1)
          continua= input("Vols demanar alguna cosa més?" )
          continuar=continua.lower()
          if continuar != "si" and continuar != "sí" :
            print("Gràcies per fer la teva comanda")
    return comanda,quantitats

  print(encarrec(productes))

  def cataleg(productes):
      print("~CATÀLEG~")
      for element in productes:
        print(element["nom"], "-", element["preu"], "$", "-", element["quantitat"], "unitats disponibles")

  comandes=[{"Usuari":"Carlota", "Producte1":"coca-cola", "Quantitat1":5},{"Usuari":"Aina", "Producte1":"oli verge", "Quantitat1":3} ]
  def encarrec(productes):
    nom_usuari = input("Indiqui el seu nom d'usuari: ")
    veure_catleg = input( " Vols veure el cataleg? ")
    veure_cataleg=veure_catleg.lower()
    if veure_cataleg=="si" or veure_cataleg=="sí":
      cataleg(productes)
    continuar="si"
    i=1
    demanda=[{"Usuari":nom_usuari}]
    while continuar=="si" or continuar=="sí" :
              demanda=demanda.append(1)
              comanda = input("Que vols demanar?")
              quantitat = input("Quantes vols?")
              continua= input("Vols demanar alguna cosa més?")
              continuar=continua.lower()
              demanda[i]={f"{comanda}":quantitat}
              i=i+1
              if continuar != "si" and continuar != "sí" :
                print("Gràcies per fer la teva comanda")
    comandes.append(demanda)
    return comandes

  comandes=encarrec(productes)
  print(comandes)
  # print(comanda)
  # print(quantitats)

  ''' 