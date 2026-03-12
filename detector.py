import re
import time
from collections import Counter
from datetime import datetime # Para registrar o horário do alerta
import os # Para limpar o terminal

arquivo_log = "log.txt"
arquivo_historico = "historico_ataques.txt"
limite = 5

def limpar_tela():
    # Limpa o terminal dependendo do sistema (Windows ou Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')

print("Monitorando logs em tempo real...\n")

while True:
    limpar_tela()
    print(f"--- Verificação em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ---")
    
    try:
        with open(arquivo_log, "r") as arquivo:
            logs = arquivo.readlines()

        ips = []
        for linha in logs:
            ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", linha)
            if ip:
                ips.append(ip.group())

        contador = Counter(ips)

        for ip, tentativas in contador.items():
            if tentativas >= limite:
                msg_alerta = f"⚠️ ALERTA DE ATAQUE | IP: {ip} | Tentativas: {tentativas}"
                print(msg_alerta)
                
                # Salva no histórico sem apagar o que já existia
                with open(arquivo_historico, "a") as hist:
                    horario = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    hist.write(f"[{horario}] {msg_alerta}\n")
                    
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo_log} não foi encontrado.")

    print("\nPróxima verificação em 5 segundos...")
    time.sleep(5)