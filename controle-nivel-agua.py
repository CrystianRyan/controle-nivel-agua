from colorama import Fore, Style, init

# Inicializa o colorama (necessário principalmente no Windows)
init(autoreset=False)

# Lista com as mensagens de cada nível (índice 0 = nível 1)
situacoes = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)",
]


def definir_cor(nivel):
    """Retorna a cor correspondente ao nível informado (1 a 5)."""
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


def exibir_situacao(nivel):
    """Exibe no terminal a situação do reservatório com a cor do nível."""
    if 1 <= nivel <= len(situacoes):
        cor = definir_cor(nivel)
        mensagem = situacoes[nivel - 1]
        print(f"{cor}Reservatório: {mensagem}")
    else:
        print(f"{Fore.WHITE}Nível inválido: {nivel}")


def main():
    print("=== Monitoramento do Reservatório de Água ===\n")

    # Simulação: valores definidos no código
    leituras = [1, 2, 3, 4, 5]

    for nivel in leituras:
        exibir_situacao(nivel)

    # Restaura o estilo padrão do terminal
    print(Style.RESET_ALL, end="")
    print("\nMonitoramento finalizado.")


main()