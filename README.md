# 🚀 STOCK ALERT BOT

![Python](https://img.shields.io/badge/python-3.12+-blue)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-green)

Bot simples de monitoramento de ações com regras automáticas de alerta.

---

## ⚡ O QUE FAZ

- Busca preço em tempo real
- Monitora múltiplos ativos
- Gera alertas por regra (acima/abaixo)
- Evita alertas repetidos
- Roda em loop contínuo

---

## 📁 ESTRUTURA

```text
app/
├── core/
│   ├── alert.py
│   └── state.py
│
├── services/
│   └── fetcher.py
│
└── main.py

run.py