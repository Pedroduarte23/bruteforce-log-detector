# Detector de Brute Force em Logs

Script em Python desenvolvido para monitorar arquivos de log em tempo real e identificar possíveis ataques de força bruta baseados em tentativas repetidas de IPs.

## 🚀 Como funciona
O script lê um arquivo de log, utiliza **Expressões Regulares (Regex)** para extrair endereços IP e conta a frequência de cada um. Se um IP ultrapassar o limite definido, um alerta é exibido no console.

## 🛠️ Tecnologias
* **Python 3.x**
* **Bibliotecas nativas:** `re`, `time`, `collections`

## 📋 Pré-requisitos
Ter um arquivo chamado `log.txt` no mesmo diretório do script.

## 🔧 Configuração
Você pode ajustar o limite de tentativas alterando a variável:
`limite = 5`
