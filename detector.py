import re
import time
from collections import Counter

arquivo_log = "log.txt"
limite = 5

print("Monitorando logs em tempo real...\n")

while True:
    
    with open(arquivo_log, "r") as arquivo:
        logs = arquivo.readlines()

    ips = []

    for linha in logs:
        ip = re.search(r"\d+\.\d+\.\d+\.\d+", linha)
        if ip:
            ips.append(ip.group())

    contador = Counter(ips)

    for ip, tentativas in contador.items():
        if tentativas >= limite:
            print("⚠ ALERTA DE ATAQUE")
            print("IP suspeito:", ip)
            print("Tentativas:", tentativas)
            print()

    time.sleep(5)