def inserir(f, v):
    f.append(v)  # insere um valor no final da lista


def retirar(f):
    return f.pop(0)  # retira e retorna um valor do início da lista


def vazia_fila(f):
    return False if f else True

fila = []
inserir(fila, 10)
inserir(fila, 20)
inserir(fila, 30)

print(f'Elemento retirado da fila: {retirar(fila)}')

