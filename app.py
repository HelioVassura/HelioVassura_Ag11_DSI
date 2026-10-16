
# Atividade: Controle de Níveis de Água
# Aluno: Helio Vassura

from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com os níveis, as situações e as cores
niveis_agua = [
    ("Nível 1", "Muito baixo (crítico)", Fore.RED),
    ("Nível 2", "Baixo", Fore.YELLOW),
    ("Nível 3", "Médio", Fore.GREEN),
    ("Nível 4", "Alto", Fore.CYAN),
    ("Nível 5", "Muito alto (alerta)", Fore.BLUE)
]

# Função responsável por exibir o alerta colorido
def exibir_alerta(nivel):
    if 1 <= nivel <= len(niveis_agua):
        nome, situacao, cor = niveis_agua[nivel - 1]

        mensagem = f"{nome}: {situacao}"
        print(cor + mensagem + Style.RESET_ALL)
    else:
        print("Nível de água inválido.")


# Programa principal
print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

# Simulação dos cinco níveis de água
for nivel in range(1, 6):
    exibir_alerta(nivel)

print("\nMonitoramento finalizado.")
