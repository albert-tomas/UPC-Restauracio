#Registrar usuaris amb base de dades
base_dades=[{"nom":"Carlota","naixement":"2005","telefon":"652900676"},{"nom":"Aina","naixement":"2005","telefon":"644718544"},{"nom":"Xavi","naixement":"2005","telefon":"677865454"}]
def registrar_usuari():
    usuari = input("Escrigui el seu nom d'usuari: ")
    any_neixament = input('Escrigui el seu any de neixament: ')
    telèfon = input('Escrigui el seu número de telèfon: ')
    print('Usuari registrat amb éxit')
    nou_usuari={"nom":usuari,"naixement":any_neixament,"telefon":telèfon}
    base_dades.append(nou_usuari)
    return

registrar_usuari()
print(base_dades)