#Registrar usuaris amb base de dades
base_dades=[{"nom":"Carlota","naixement":"2005","telefon":"652900676"}]
def registrar_usuari(base_dades):
  usuari = input("Escrigui el seu nom d'usuari: ")
  any_neixament = input('Escrigui el seu any de neixament: ')
  telèfon = input('Escrigui el seu número de telèfon: ')
  print('Usuari registrat amb éxit')
  nou_usuari={"nom":usuari,"naixement":any_neixament,"telefon":telèfon}
  base_dades=base_dades.append(nou_usuari)
  return base_dades

  #Registrar usuari
  def registrar_usuari():
  usuari = input("Escrigui el seu nom d'usuari: ")
  any_neixament = input('Escrigui el seu any de neixament: ')
  telèfon = input('Escrigui el seu número de telèfon: ')
  print('Usuari registrat amb éxit')
  perfil={"Nom usuari":{usuari}, "Any neixament": {any_neixament}, "Contacte": {telèfon} }
  return perfil