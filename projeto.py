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

# Adiciona uma nova companhia aérea na fila
def inserirCompanhia(fila, nomeCompanhia):
    companhia = {
        "nome": nomeCompanhia,
        "voos": []
    }
    inserir(fila, companhia)
    print(f'Companhia "{nomeCompanhia}" adicionada à fila.')

# Adiciona um voo à pilha de uma companhia específica
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

# Atende (remove) o voo do topo da pilha da primeira companhia da fila
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

# Remove uma companhia específica da fila
def removerCompanhia(fila, nomeCompanhia):
    if vazia_fila(fila):
        print("A fila está vazia")
        return
    
    fila_temp = []
    removida = False

    # Transfere companhias para fila temporária exceto a que será removida
    while not vazia_fila(fila):
        companhia = retirar(fila)
        if companhia["nome"] != nomeCompanhia:
            inserir(fila_temp, companhia)
        else:
            print(f'Companhia "{nomeCompanhia}" removida da fila')
            removida = True

    # Restaura a fila original
    while not vazia_fila(fila_temp):
        inserir(fila, retirar(fila_temp))

    if not removida:
        print(f'Companhia "{nomeCompanhia}" não encontrada na fila')

# Cancela um voo de uma companhia específica
def cancelarVoo(fila, nomeCompanhia, codigoVoo):
    if vazia_fila(fila):
        print("A fila está vazia.")
        return

    fila_temp = []
    encontrou = False

    while not vazia_fila(fila):
        companhia = retirar(fila)

        if companhia["nome"] == nomeCompanhia:
            pilha_voos = companhia["voos"]
            pilha_temp = []

            # Procura o voo e remove
            while not vazia(pilha_voos):
                voo = pop(pilha_voos)
                if voo["codigo"] == codigoVoo:
                    print(f'Voo {codigoVoo} cancelado da companhia "{nomeCompanhia}".')
                    encontrou = True
                    break
                else:
                    push(pilha_temp, voo)

            # Restaura os demais voos
            while not vazia(pilha_temp):
                push(pilha_voos, pop(pilha_temp))

        inserir(fila_temp, companhia)

    while not vazia_fila(fila_temp):
        inserir(fila, retirar(fila_temp))

    if not encontrou:
        print(f'Voo {codigoVoo} não encontrado na companhia "{nomeCompanhia}".')

# Suspende (joga para o final) um voo de uma companhia
def suspenderVoo(fila, nomeCompanhia, codigoVoo):
    if vazia_fila(fila):
        print("A fila está vazia.")
        return

    fila_temp = []
    voo_suspenso = None
    encontrou = False

    while not vazia_fila(fila):
        companhia = retirar(fila)

        if companhia["nome"] == nomeCompanhia:
            pilha_voos = companhia["voos"]
            pilha_temp = []

            # Encontra o voo a ser suspenso
            while not vazia(pilha_voos):
                voo = pop(pilha_voos)
                if voo["codigo"] == codigoVoo and not encontrou:
                    voo_suspenso = voo
                    encontrou = True
                else:
                    push(pilha_temp, voo)

            # Restaura a pilha
            while not vazia(pilha_temp):
                push(pilha_voos, pop(pilha_temp))

            # Coloca o voo suspenso no final da pilha
            if encontrou:
                pilha_aux = []
                while not vazia(pilha_voos):
                    push(pilha_aux, pop(pilha_voos))
                push(pilha_voos, voo_suspenso)
                while not vazia(pilha_aux):
                    push(pilha_voos, pop(pilha_aux))

                print(f'Voo {codigoVoo} suspenso (adiado) na companhia "{nomeCompanhia}".')

        inserir(fila_temp, companhia)

    while not vazia_fila(fila_temp):
        inserir(fila, retirar(fila_temp))

    if not encontrou:
        print(f'Voo {codigoVoo} não encontrado na companhia "{nomeCompanhia}".')

# Troca a posição de dois voos de uma mesma companhia
def trocarVoos(fila, nomeCompanhia, codigoVoo1, codigoVoo2):
    if vazia_fila(fila):
        print("A fila está vazia.")
        return
    
    fila_temp = []
    trocou = False

    while not vazia_fila(fila):
        companhia = retirar(fila)

        if companhia["nome"] == nomeCompanhia:
            pilha_voos = companhia["voos"]
            pilha_temp = []
            voo1 = voo2 = None

            # Transfere todos os voos para pilha_temp, procurando os dois voos
            while not vazia(pilha_voos):
                voo = pop(pilha_voos)
                if voo["codigo"] == codigoVoo1:
                    voo1 = voo
                elif voo["codigo"] == codigoVoo2:
                    voo2 = voo
                push(pilha_temp, voo)

            # Se os dois voos foram encontrados, trocamos
            if voo1 and voo2:
                pilha_reorganizada = []

                while not vazia(pilha_temp):
                    voo = pop(pilha_temp)
                    if voo["codigo"] == codigoVoo1:
                        push(pilha_reorganizada, voo2)
                    elif voo["codigo"] == codigoVoo2:
                        push(pilha_reorganizada, voo1)
                    else:
                        push(pilha_reorganizada, voo)

                # Restaura a pilha original
                while not vazia(pilha_reorganizada):
                    push(pilha_voos, pop(pilha_reorganizada))

                print(f'Voos {codigoVoo1} e {codigoVoo2} trocados na companhia "{nomeCompanhia}".')
                trocou = True
            else:
                # se não encontrou ambos, restaura os voos como estavam
                while not vazia(pilha_temp):
                    push(pilha_voos, pop(pilha_temp))

                print(f'Um ou ambos os voos não foram encontrados na companhia "{nomeCompanhia}".')

        inserir(fila_temp, companhia)

    while not vazia_fila(fila_temp):
        inserir(fila, retirar(fila_temp))

    if not trocou:
        print(f'Não foi possível trocar os voos {codigoVoo1} e {codigoVoo2}')

# Mostra todas as companhias e seus voos (do topo para a base)
def mostrarCompanhiaVoo(fila):
    if vazia_fila(fila):
        print("A fila está vazia")
        return
    
    fila_temp = []

    while not vazia_fila(fila):
        companhia = retirar(fila)
        print(f'\nCompanhia: {companhia["nome"]}')

        pilha_voos = companhia["voos"]
        pilha_temp = []

        if vazia(pilha_voos):
            print(" Nenhum voo cadastrado")
        else:
            print(" Voos (do topo para a base):")
            while not vazia(pilha_voos):
                voo = pop(pilha_voos)
                print(f' Código: {voo["codigo"]}, Destino: {voo["destino"]}, Horário: {voo["horario"]}')
                push(pilha_temp, voo)

            while not vazia(pilha_temp):
                push(pilha_voos, pop(pilha_temp))
        inserir(fila_temp, companhia)
    while not vazia_fila(fila_temp):
        inserir(fila, retirar(fila_temp))

# Busca todos os voos de todas as companhias com destino específico
def buscarVoosDestino(fila, destino):
    if vazia_fila(fila):
        print("A fila está vazia.")
        return

    encontrou = False
    fila_temp = []

    while not vazia_fila(fila):
        companhia = retirar(fila)
        pilha_voos = companhia["voos"]
        pilha_temp = []

        while not vazia(pilha_voos):
            voo = pop(pilha_voos)
            if voo["destino"].lower() == destino.lower():
                print(f'\nCompanhia: {companhia["nome"]}')
                print(f'  Código: {voo["codigo"]}, Destino: {voo["destino"]}, Horário: {voo["horario"]}')
                encontrou = True
            push(pilha_temp, voo)

        while not vazia(pilha_temp):
            push(pilha_voos, pop(pilha_temp))

        inserir(fila_temp, companhia)

    while not vazia_fila(fila_temp):
        inserir(fila, retirar(fila_temp))

    if not encontrou:
        print(f'Nenhum voo encontrado para o destino "{destino}".')

# Mostra estatísticas gerais do sistema
def mostrarEstatisticas(fila):
    if vazia_fila(fila):
        print("Não há companhias na fila.")
        return

    fila_temp = []
    total_companhias = 0
    total_voos = 0
    companhia_mais_voos = None
    max_voos = 0

    while not vazia_fila(fila):
        companhia = retirar(fila)
        total_companhias += 1

        pilha_voos = companhia["voos"]
        pilha_temp = []
        num_voos = 0

        while not vazia(pilha_voos):
            voo = pop(pilha_voos)
            push(pilha_temp, voo)
            num_voos += 1

        while not vazia(pilha_temp):
            push(pilha_voos, pop(pilha_temp))

        total_voos += num_voos

        if num_voos > max_voos:
            max_voos = num_voos
            companhia_mais_voos = companhia["nome"]

        inserir(fila_temp, companhia)

    while not vazia_fila(fila_temp):
        inserir(fila, retirar(fila_temp))

    print("\n=== Estatísticas do Aeroporto ===")
    print(f"Total de companhias na fila: {total_companhias}")
    print(f"Total de voos cadastrados: {total_voos}")
    if companhia_mais_voos:
        print(f"Companhia com maior número de voos: {companhia_mais_voos} ({max_voos} voos)")

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

cancelarVoo(fila_companhias, "LATAM", "LAT124")

trocarVoos(fila_companhias, "LATAM", "LAT123", "LAT124")

mostrarCompanhiaVoo(fila_companhias)

buscarVoosDestino(fila_companhias, "São Paulo")

mostrarEstatisticas(fila_companhias)