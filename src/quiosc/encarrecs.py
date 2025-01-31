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