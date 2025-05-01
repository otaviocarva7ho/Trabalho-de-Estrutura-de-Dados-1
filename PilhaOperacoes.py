# funcoes primitivas para manipulacao de pilha

def push(p, v):  # p representa o repositorio-lista e v o valor a ser inserido
    p.append(v)


def pop(p):
    return p.pop()


def vazia(p):
    return False if p else True

p=[]
push(p,10)
push(p,201)
push(p,30)
push(p,403)
push(p,50)

print(f'Valor retirado da pilha: {pop(p)}')
print(f'Valor retirado da pilha: {pop(p)}')
print(f'Valor retirado da pilha: {pop(p)}')

