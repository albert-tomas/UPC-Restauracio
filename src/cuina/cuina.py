#Funcions necessaries
#Planificar encarrec, la funció necesita retornar les posicions al magatzem de tots els productes de l'encarrec
#Servir encarrec crita a la funció de retirar producte del magatzem
#Consulta productes populars: necesita del parametre vendes de la clase producte
#Afegir nou encarrec a la cua
from ipaddress import collapse_addresses
from pprint import pprint

from src.magatzem.magatzem import inicialitzar_magatzem, coloca_producte, buscar_producte, retirar_producte

from src.magatzem.productes import productes

# Configuració inicial es fa a test_magatzem
num_prestatges_camera = 4
num_prestatges_despensa = 4
num_nivells = 4 # Nombre de nivells
num_safates = 4 # Nombre de safates en una casella
capacitat_safata = 4 #Nombre d'elements que caben en una safata
despensa = inicialitzar_magatzem(num_safates,num_nivells,num_prestatges_despensa)
camera = inicialitzar_magatzem(num_safates,num_nivells,num_prestatges_camera)

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

comandes = [
    {
    "nom": "carlota",
    "comandes": [{
            "comanda" : "cc",
            "quantitat" : 3},
           {"comanda": "oli1",
            "quantitat": 8}]
    },
    {
      "nom": "xavi",
      "comandes":[
            {"comanda" : "oli2",
            "quantitat" : 1}]
    }
]

posicio = buscar_producte(despensa,camera,"cc-zero")
#print ( posicio)
def servir_encarrec(comandes, despensa, camera):
    primera_comanda = comandes[0]
    llista_primer_comanda = primera_comanda["comandes"]
    for i in range (len(llista_primer_comanda)):
        primer_producte = llista_primer_comanda[i]
        for temp in range (primer_producte["quantitat"]):
            posicio = buscar_producte(despensa,camera,primer_producte["comanda"])
            if  posicio!=None:
                retirar_producte(despensa,camera, primer_producte["comanda"])

            else:
                print("Ja no ens queden mes: ",primer_producte["comanda"])
    comandes.pop(0) #elimino la primera comanda ja realitzada
    print(comandes)

servir_encarrec(comandes,despensa,camera)

pprint(despensa)