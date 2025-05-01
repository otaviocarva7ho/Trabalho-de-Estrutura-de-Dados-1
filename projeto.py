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

fila_companhias = []
inserirCompanhia(fila_companhias, "LATAM")
inserirCompanhia(fila_companhias, "GOL")

adicionarVoo(fila_companhias, "LATAM", "LAT123", "São Paulo", "14:00")
adicionarVoo(fila_companhias, "LATAM", "LAT124", "Rio de Janeiro", "15:30")
adicionarVoo(fila_companhias, "GOL", "GOL456", "Salvador", "16:45")
