def push(p, v):
    p.append(v)

def pop(p):
    return p.pop()

def vazia(p):
    return False if p else True

def inserir(f, v):
    f.append(v)

def retirar(f):
    return f.pop(0)

def vazia_fila(f):
    return False if f else True

def inserirCompanhia(fila, nomeCompanhia):
    companhia = {
        "nome": nomeCompanhia,
        "voos": []
    }
    inserir(fila, companhia)
    print(f'Companhia "{nomeCompanhia}" adicionada à fila.')

def adicionarVoo(fila, nomeCompanhia, codigo, destino, horario):
    for companhia in fila:
        if companhia["nome"] == nomeCompanhia:
            voo = {
                "codigo": codigo,
                "destino": destino,
                "horario": horario
            }
            push(companhia["voos"], voo)
            print(f'Voo {codigo} adicionado à companhia "{nomeCompanhia}"')
            return
    print(f'Companhia "{nomeCompanhia}" não encontrada na fila.')

def atenderVoo(fila):
    if vazia_fila(fila):
        print("Não há companhias na fila.")
        return

    companhia = fila[0]

    if vazia(companhia["voos"]):
        print(f'Companhia "{companhia["nome"]}" não possui voos para atender.')
        retirar(fila)
        print(f'Companhia "{companhia["nome"]}" removida da fila.')
    else:
        voo = pop(companhia["voos"])
        print(f'Voo atendido da companhia "{companhia["nome"]}":')
        print(f'Código: {voo["codigo"]}, Destino: {voo["destino"]}, Horário: {voo["horario"]}')
        
        if vazia(companhia["voos"]):
            retirar(fila)
            print(f'Companhia "{companhia["nome"]}" não possui mais voos e foi removida da fila.')

def removerCompanhia(fila, nomeCompanhia):
    if vazia_fila(fila):
        print("A fila está vazia")
        return
    
    fila_temp = []

    removida = False
    while not vazia_fila(fila):
        companhia = retirar(fila)
        if companhia["nome"] != nomeCompanhia:
            inserir(fila_temp, companhia)
        else:
            print(f'Companhia "{nomeCompanhia}" removida da fila')
            removida = True

    while not vazia_fila(fila_temp):
        inserir(fila, retirar(fila_temp))

    if not removida:
        print(f'Companhia "{nomeCompanhia}" não encontrada na fila')

fila_companhias = []
inserirCompanhia(fila_companhias, "LATAM")
inserirCompanhia(fila_companhias, "GOL")

adicionarVoo(fila_companhias, "LATAM", "LAT123", "São Paulo", "14:00")
adicionarVoo(fila_companhias, "LATAM", "LAT124", "Rio de Janeiro", "15:30")
adicionarVoo(fila_companhias, "GOL", "GOL456", "Salvador", "16:45")

atenderVoo(fila_companhias)
atenderVoo(fila_companhias)
atenderVoo(fila_companhias)

removerCompanhia(fila_companhias, "LATAM")