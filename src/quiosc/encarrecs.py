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


#definim una comanda del nou usuari 

encarrec(usuaris,"carlota", comanda) #fem un nou encarrec al perfil carlota