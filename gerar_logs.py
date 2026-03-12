import time
import random

arquivo_log = "log.txt"
# IPs fictícios para simular tráfego
ips_normais = ["192.168.1.15", "10.0.0.5", "172.16.0.20"]
ip_ataque = "192.168.1.100"

print("Gerador de logs iniciado... (Ctrl+C para parar)")

while True:
    # 80% de chance de ser um IP normal, 20% de ser o IP de ataque
    ip = ip_ataque if random.random() < 0.2 else random.choice(ips_normais)
    
    log_entry = f"LOGIN ATTEMPT FROM {ip} - Status: FAILED\n"
    
    with open(arquivo_log, "a", encoding="utf-8") as f:
        f.write(log_entry)
        print(f"Log gerado: {log_entry.strip()}")
    
    time.sleep(1) # Gera um log por segundo