lista = {'Juan': 3107035469, 'Pablo': 3045569321}

def elimina(lista, usuario):
    return lista.pop(usuario, '')

print(elimina(lista, 'Pablo'))