
def push(p, v):  # Empilhar
    p.append(v)


def pop(p):  # Desempilhar
    return p.pop()


def vazia(p):  # Verificar se está vazia
    return False if p else True


def calcPosfixa(epos):
    pilha = []
    for crt in epos:
        if crt.isdigit():
            push(pilha, float(crt))
        else:
            b = pop(pilha)  # segundo termo
            a = pop(pilha)  # primeiro termo
            if crt == '+':
                r = a + b
            elif crt == '-':
                r = a - b
            elif crt == '*':
                r = a * b
            else:
                r = a / b
            push(pilha, r)

    return pop(pilha)


print('\nValor:', calcPosfixa('328*+'))