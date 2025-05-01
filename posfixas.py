
def push(p, v):  # Empilhar
    p.append(v)


def pop(p):  # Desempilhar
    return p.pop()


def vazia(p):  # Verificar se está vazia
    return False if p else True


def precedencia(op):
    prioridades = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return prioridades.get(op, 0)


def infixa_para_posfixa(expressao):
    pilha = []
    saida = []

    for char in expressao:
        if char.isalnum():  # Se for operando (número/letra)
            saida.append(char)
        elif char == '(':
            push(pilha, char)
        elif char == ')':
            topo = pop(pilha)
            while topo != '(':
                saida.append(topo)
                topo = pop(pilha)
        else:  # Operador
            while not vazia(pilha):
                topo = pop(pilha)
                if precedencia(topo) < precedencia(char):
                    push(pilha, topo)
                    break
                saida.append(topo)
            push(pilha, char)

    while not vazia(pilha):
        saida.append(pop(pilha))

    return ''.join(saida)

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


# Exemplo de uso
expressao = "A+B*(C^D-E)"  # Exemplo de expressão infixa
print(infixa_para_posfixa(expressao))  # Saída esperada: "ABCD^E-*+"
expressao = "3+4*(2-1)"  # Exemplo de expressão infixa
print(infixa_para_posfixa(expressao))

print('\nValor:', calcPosfixa('328*+'))
