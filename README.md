# SOC Mini SIEM – Correlation Engine (v2)

Projeto desenvolvido para simular o funcionamento de um mecanismo de correlação utilizado em ambientes de Security Operations Center (SOC).

O objetivo é demonstrar como múltiplas fontes de log podem ser analisadas e correlacionadas para identificar comportamentos suspeitos e gerar alertas estruturados.

# 🎯 Objetivo

Simular um fluxo operacional de um SOC (Nível 1 / Nível 2), correlacionando múltiplas fontes de log para identificar comportamentos suspeitos e gerar alertas estruturados.

O projeto demonstra:

- Análise de logs de autenticação
- Correlação com eventos de firewall
- Detecção de padrões suspeitos
- Geração de alertas estruturados
- Mapeamento de técnicas MITRE ATT&CK

---

# 🚀 Versão 2 – Melhorias implementadas

A versão 2 do projeto adiciona melhorias importantes no mecanismo de detecção para aproximar o comportamento do motor de correlação de um SIEM utilizado em ambientes reais.

Principais melhorias:

• Detecção de brute force baseada em **janela de tempo**  
• **Threshold configurável** para eventos suspeitos  
• **Regras configuráveis via YAML**  
• **Whitelist de IPs confiáveis** para reduzir falsos positivos  
• Correlação aprimorada com eventos de firewall  
• Saída estruturada de alertas em **JSON**  
• Arquitetura modular separando **parsers, engine e configuração**

---

# 🧠 Lógica de Detecção

O mecanismo de correlação identifica possíveis ataques de **SSH brute force** através da seguinte lógica:

1. Monitorar eventos de **Failed SSH Login**
2. Agrupar eventos por **endereço IP**
3. Verificar se o número de falhas excede o **threshold configurado**
4. Validar se os eventos ocorreram dentro de uma **janela de tempo**
5. Correlacionar com eventos de **bloqueio do firewall**
6. Gerar alerta estruturado em JSON

---

# 🗂 Estrutura do Projeto

```
soc-mini-siem-correlation-engine
│
├── logs
│ ├── auth.log
│ └── firewall.log
│
├── config
│ ├── rules.yaml
│ └── whitelist.txt
│
├── engine
│ └── correlation_engine.py
│
├── parsers
│ ├── auth_parser.py
│ └── firewall_parser.py
│
├── output
│ └── alerts.json
│
├── alert_generator.py
├── main.py
└── README.md

---

# 📄 Fontes de Log Utilizadas

### auth.log

Contém eventos de autenticação SSH.

Exemplo:

Failed password for invalid user admin from 192.168.0.10 port 54421 ssh2

---

### firewall.log

Contém eventos de bloqueio de conexão pelo firewall.

Exemplo:

BLOCK SRC=192.168.0.10 DST=192.168.0.1 PROTO=TCP DPT=22

---

# ⚙️ Configuração de Regras

Arquivo:

config/rules.yaml

Exemplo:

```yaml
ssh_bruteforce:
  threshold: 5
  window_seconds: 60
  severity_if_blocked: high
  severity_if_not_blocked: medium

Descrição:

| Parâmetro               | Função                              |
| ----------------------- | ----------------------------------- |
| threshold               | Número mínimo de tentativas falhas  |
| window_seconds          | Janela de tempo para correlação     |
| severity_if_blocked     | Severidade quando firewall bloqueia |
| severity_if_not_blocked | Severidade sem bloqueio             |

# 🛡 Whitelist

IPs confiáveis podem ser ignorados na análise.

Arquivo:

config/whitelist.txt

Exemplo:

127.0.0.1
192.168.0.1
10.0.0.5

# 🚨 Exemplo de Alerta Gerado

{
  "timestamp": "2026-03-08T17:32:00Z",
  "alert_type": "Correlated Suspicious Activity",
  "rule_name": "ssh_bruteforce_correlation",
  "source_ip": "192.168.0.10",
  "ssh_failed_attempts": 5,
  "time_window_seconds": 60,
  "firewall_blocked": true,
  "severity": "high",
  "mitre": {
    "technique_id": "T1110",
    "technique_name": "Brute Force",
    "tactic": "Credential Access"
  }
}

🧩 Mapeamento MITRE ATT&CK

| Técnica     | ID    | Tática            |
| ----------- | ----- | ----------------- |
| Brute Force | T1110 | Credential Access |


▶️ Como Executar o Projeto

Clone o repositório:

git clone https://github.com/sejosegomesneto-creator/soc-mini-siem-correlation-engine.git

Entre no diretório:
cd soc-mini-siem-correlation-engine

Instale dependências:
python3 -m pip install pyyaml

Execute:
python3 main.py

📊 Fluxo Simulado de SOC

O projeto simula o trabalho de um analista SOC:

1️⃣ Coleta de logs
2️⃣ Análise de eventos
3️⃣ Correlação de atividades
4️⃣ Identificação de padrão suspeito
5️⃣ Geração de alerta estruturado

## 🎯 Cenário Simulado

O projeto simula um cenário comum em ambientes SOC onde um atacante tenta realizar um ataque de força bruta via SSH.

Fluxo simulado:

1. O projeto simula um cenário comum em ambientes SOC onde um atacante realiza múltiplas tentativas de autenticação SSH caracterizando um ataque de força bruta.
2. Os eventos são registrados no arquivo `auth.log`
3. O firewall detecta comportamento suspeito e bloqueia o IP
4. O mecanismo de correlação analisa os eventos
5. Um alerta estruturado é gerado com severidade apropriada

📚 Conceitos de Segurança Demonstrados

- Log Analysis (Análise de Logs)
- Event Correlation (Correlação de Eventos)
- Threat Detection (Detecção de Ameaças)
- SSH Brute Force Detection
- MITRE ATT&CK Mapping (T1110 - Brute Force)
- SIEM Fundamentals
- SOC Analyst Workflow (Nível 1 / Nível 2)

## 🔍 Objetivo Educacional

Este projeto foi desenvolvido como laboratório prático para estudo de:

- Análise de logs
- Correlação de eventos de segurança
- Detecção de ataques de brute force
- Estrutura de um mecanismo de correlação semelhante a SIEM
- Mapeamento de eventos para MITRE ATT&CK

O objetivo é demonstrar conceitos fundamentais utilizados por analistas SOC na detecção de atividades suspeitas em ambientes reais.


## 👨‍💻 Autor

**José Barbosa Gomes Neto**

Analista SOC Jr | Blue Team | SIEM | Correlação de Eventos  

🔗 GitHub: https://github.com/sejosegomesneto-creator  
🔗 LinkedIn: www.linkedin.com/in/jose-barbosa-ti
