# funcoes primitivas para manipulacao de pilha

def push(p, v):  # p representa o repositorio-lista e v o valor a ser inserido
    p.append(v)


def pop(p):
    return p.pop()


def vazia(p):
    return False if p else True

def mostraTopo(p):
    if vazia(p):
        print('A pilha esta vazia')
    else:
        v=pop(p)
        push(p,v)
        print(v)

def esvaziarPilha(p):

    while not vazia(p):
        pop(p)

    print('a pilha ficou vazia')

def mostraPilha(p):

    aux = []
    while not vazia(p):
        v = pop(p)
        print(v)
        push(aux, v)
    while not vazia(aux):
        v = pop(aux)
        push(p, v)

p=[]
mostraTopo(p)
push(p,10)
push(p,201)
push(p,30)
push(p,403)
push(p,50)
mostraTopo(p)
print('Conteudo da pilha')
mostraPilha(p)
print(f'Valor retirado da pilha: {pop(p)}')
print(f'Valor retirado da pilha: {pop(p)}')
print(f'Valor retirado da pilha: {pop(p)}')
esvaziarPilha(p)
mostraTopo(p)

