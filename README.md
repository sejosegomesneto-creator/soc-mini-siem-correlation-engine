# SOC Mini SIEM – Correlation Engine (v1)

Projeto voltado para simulação prática de atividades de um SOC (Security 
Operations Center), com foco em correlação de eventos e geração de alertas 
estruturados.

---

## 📌 Objetivo

Simular um fluxo operacional de um SOC (Nível 1 / Nível 2), 
correlacionando múltiplas fontes de log para identificar comportamentos 
suspeitos.

O projeto realiza:

- Análise de falhas de autenticação SSH (auth.log)
- Análise de eventos de firewall (firewall.log)
- Correlação entre eventos
- Classificação de severidade
- Geração de alerta estruturado em JSON
- Mapeamento MITRE ATT&CK

---

## 🧠 Lógica de Correlação

Regras implementadas:

- Se um IP possuir **5 ou mais falhas SSH** e estiver **bloqueado no 
firewall** → Severidade **HIGH**
- Se um IP possuir **5 ou mais falhas SSH**, mas não estiver bloqueado → 
Severidade **MEDIUM**

Essa lógica simula um mecanismo básico de correlação de um SIEM.

---

## 🛡 MITRE ATT&CK

Mapeamento implementado:

- Technique ID: **T1110**
- Technique Name: **Brute Force**
- Tactic: **Credential Access**

---

## 🏗 Estrutura do Projeto
soc-mini-siem-correlation-engine/
├── logs/
│ ├── auth.log
│ └── firewall.log
├── main.py
├── alert_generator.py
└── alert_*.json


---

## ⚙ Tecnologias Utilizadas

- Python 3
- Regex (extração de IP)
- Manipulação de arquivos
- Estruturação JSON
- Simulação de logs Linux
- Conceitos de SOC
- MITRE ATT&CK Framework

---

## ▶ Como Executar

```bash
python3 main.py


## Version 2 Enhancements

- Time-window based correlation
- Configurable threshold via YAML
- Whitelist filtering to reduce false positives
- Structured alert output in JSON
- Improved SSH brute-force correlation logic

## Detection Logic

The engine detects repeated failed SSH login attempts from the same source IP within a configurable time window and correlates the result with firewall block events.

## Configuration

Rules are stored in:

- `config/rules.yaml`

Whitelist is stored in:

- `config/whitelist.txt`
