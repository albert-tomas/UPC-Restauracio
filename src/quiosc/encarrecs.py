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

def encarrec(usuaris, nomUsuari, laComanda):
  usuari = "carlota"
  usuari.append(laComanda)


comanda = [{"comanda" : "coca-cola",
            "quantitat" : 2},
           {"comanda": "oli",
            "quantitat": 1}]

encarrec(usuaris,"carlota", comanda) 