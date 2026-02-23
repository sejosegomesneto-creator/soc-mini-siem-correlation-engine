# SOC Mini SIEM – Correlation Engine (v1)

Projeto desenvolvido para simular a lógica central de um mecanismo de correlação utilizado em ambientes SOC (Security Operations Center), focado na detecção de atividades suspeitas através da análise e correlação de múltiplas fontes de log.

---

## 📌 Objetivo

Simular um fluxo operacional de um SOC (Nível 1 / Nível 2), correlacionando múltiplas fontes de log para identificar comportamentos suspeitos.

O projeto realiza:

- Análise de falhas de autenticação SSH (`auth.log`)
- Análise de eventos de firewall (`firewall.log`)
- Correlação entre eventos
- Classificação de severidade
- Geração de alerta estruturado em JSON
- Mapeamento MITRE ATT&CK

---

## 🧠 Lógica de Correlação

Regras implementadas:

- Se um IP possuir **5 ou mais falhas SSH** e estiver **bloqueado no firewall** → Severidade **HIGH**
- Se um IP possuir **5 ou mais falhas SSH**, mas não estiver bloqueado → Severidade **MEDIUM**

Essa lógica simula um mecanismo básico de correlação utilizado em soluções SIEM.

---

## 🛡 MITRE ATT&CK

Mapeamento implementado:

- **Technique ID:** T1110  
- **Technique Name:** Brute Force  
- **Tactic:** Credential Access  

---

## 🏗 Estrutura do Projeto

```
soc-mini-siem-correlation-engine/
├── logs/
│   ├── auth.log
│   └── firewall.log
├── main.py
├── alert_generator.py
└── alert_*.json
```


---


## 📤 Exemplo de Alerta Gerado

```json
{
    "alert_type": "Correlated Suspicious Activity",
    "source_ip": "192.168.0.10",
    "ssh_failed_attempts": 6,
    "severity": "High",
    "mitre": {
        "technique_id": "T1110",
        "technique_name": "Brute Force",
        "tactic": "Credential Access"
    }
}
```

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
