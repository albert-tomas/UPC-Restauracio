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
        
2. **Quiosc interactiu:** Eina digital per a la personalització d'encàrrecs, consulta de productes i gestió d’informació de manera accessible.
    Funcions disponibles:
       
       Servir comandes: Processa les comandes dels clients, retirant els productes sol·licitats i actualitzant les vendes amb la funció servir_encarrec().
       Mostrar catàleg de productes per vendes: Mostra els productes ordenats per la quantitat de vendes amb la funció mostrar_cataleg_per_ventes().

3. **Cuina:** Centre operatiu on es planifiquen i preparen els encàrrecs, optimitzant la recollida i el lliurament.

Participants: 
Xavi Moreno xavier.moreno.rubio@estudiantat.upc.edu
Carlota Griñó carlota.grino@estudiantat.upc.edu
Aina Aguilera aina.aguilera@estudiantat.upc.edu
Helena Fito Rosillo helena.fito@estudiantat.upc.edu