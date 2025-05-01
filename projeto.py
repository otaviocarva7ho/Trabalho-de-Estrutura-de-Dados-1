voo = {
    "código": "LAT1234",
    "destino": "São Paulo",
    "horário": "14:30"
}

companhia = {
    "nome": "LATAM",
    "voos": [voo1, voo2, voo3, ...]
}

fila_companhias = [companhia1, companhia2, ...]

def inserirCompanhia(fila, nomeCompanhia):
    companhia = {
        "nome": nomeCompanhia,
        "voos": []
    }
    fila.append(companhia)
    print(f'Companhia "{nomeCompanhia}" adicionada à fila.')

fila_companhias = []
inserirCompanhia(fila_companhias, "LATAM")
inserirCompanhia(fila_companhias, "GOL")