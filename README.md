# UPC_Restauracio
# Sistema de Restauració Innovador per a la UPC

## Introducció

Aquest projecte té com a objectiu desenvolupar un sistema de restauració innovador per als usuaris del campus de la Universitat Politècnica de Catalunya (UPC). La iniciativa s'emmarca dins del compromís de la UPC amb la sostenibilitat, la tecnologia i la qualitat dels serveis, tot buscant optimitzar la gestió dels recursos, millorar els processos de preparació i lliurament de comandes, i oferir transparència i comoditat als usuaris.

El sistema es compon de tres seccions principals interconnectades:

1. **Magatzem:** Espai automatitzat amb prestatgeries robotitzades per gestionar eficientment productes refrigerats i no refrigerats.
   Les funcions disponibles es troben agrupades en un menú a test_magatzem.py
   Funcions disponibles: 
       inicialitzar_magatzem(): Inicialitza la matriu 3D que representa el magatzem amb el nombre de safates, nivells i estanteries especificats.
       coloca_producte(): Afegeix un producte al magatzem per categoria i quantitat.
       buscar_producte(): Cerca la ubicació d'un producte al magatzem segons la seva ID.
       retirar_producte(): Retira un producte del magatzem per la seva ID.
       obtenir_productes_safata(): Retorna la llista de productes d'una safata específica.
        
2. **Quiosc i botiga:** Eina digital per a la personalització d'encàrrecs, consulta de productes i gestió d’informació de manera accessible. Les funcions disponibles es troben agrupades a l'arxiu quiosc.py amb un menú.
    Funcions disponibles:
       registrar_usuari(): Recull les dades personals de nom, naixement i telèfon per introduir-les a un perfil i pujar-les a la base de dades dels usuaris.
       encàrrec(): Amb el nom d'usuari, afegeix la seva comanda a la llista de comandes dels usuaris per ser portada a la cuina.
       ordenador_productes(): Ordena el llistat de productes disponibles en ordre creixent de preu.
       cataleg(): Escriu una llista amb el nom, el preu i la quantitat de productes disponibles perquè els clients puguin escollir què volen.
       categories_disponibles: Retorna una llista amb totes les categories de productes disponibles.
       categoria_un_producte(): Permet consultar a quina categoria pertany qualsevol producte del catàleg.
       producte_categoria(): Retorna una llista amb tots els productes que pertanyen a la categoria demanada.

3. **Cuina:** Centre operatiu on es planifiquen i preparen els encàrrecs, optimitzant la recollida i el lliurament.

Participants: 
Xavi Moreno xavier.moreno.rubio@estudiantat.upc.edu
Carlota Griñó carlota.grino@estudiantat.upc.edu
Aina Aguilera aina.aguilera@estudiantat.upc.edu
Helena Fito Rosillo helena.fito@estudiantat.upc.edu
Albert