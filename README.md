# 🤖 Automations - AI WhatsApp Assistant

Sistema de automação de mensagens com Inteligência Artificial integrado ao WhatsApp via Chatwoot.

Este projeto recebe mensagens de usuários, processa com IA (OpenAI) mantendo histórico de conversa, e responde automaticamente.

---

## 🚀 Funcionalidades

* ✅ Recebimento de mensagens via webhook (Chatwoot)
* ✅ Integração com API da OpenAI
* ✅ Memória de conversas por usuário (session_id)
* ✅ Respostas automáticas com contexto
* ✅ Envio de mensagens de volta via Chatwoot
* ✅ Estrutura modular e escalável

---

## 🧠 Como funciona

1. O usuário envia uma mensagem no WhatsApp
2. O Chatwoot dispara um webhook para `/webhook`
3. O sistema:

   * Identifica o usuário (telefone)
   * Recupera o histórico da conversa
   * Envia tudo para a OpenAI
4. A IA gera uma resposta contextual
5. A resposta é enviada de volta ao usuário

---

## 🏗️ Estrutura do Projeto

```
automations/
│
├── main.py                # Entrada da API (FastAPI)
├── ai_assistent.py       # Lógica de IA e memória
├── run.py                # Script para disparo em massa
│
├── db/
│   └── memory.py         # Funções de histórico (get/save)
│
├── services/
│   ├── send_message.py       # Envio de mensagem individual
│   └── send_mass_message.py  # Envio em massa
│
└── .env                  # Variáveis de ambiente
```

---

## ⚙️ Tecnologias

* Python
* FastAPI
* OpenAI API
* Supabase / Banco de dados
* Chatwoot (WhatsApp)
* Webhooks
* dotenv

---

## 🔑 Variáveis de Ambiente

Crie um arquivo `.env` na raiz e coloque as variáveis de ambiente como OPENAI_API_KEY e URL_CHATWOOT

## ▶️ Como rodar o projeto

### 1. Instalar dependências

```bash
pip install fastapi uvicorn python-dotenv openai
```

---

### 2. Rodar o servidor

```bash
uvicorn main:app --reload
```

---

### 3. Endpoint disponível

```
POST /webhook
```

---

## 🔄 Fluxo do Webhook

O endpoint `/webhook` recebe dados no formato:

```json
{
  "message_type": "incoming",
  "content": "Mensagem do usuário",
  "sender": {
    "phone_number": "5511999999999"
  }
}
```

---

## 🧠 Lógica da IA

Arquivo: `ai_assistent.py`

* Recupera histórico com `get_history(session_id)`
* Adiciona nova mensagem
* Envia para OpenAI (`gpt-4.1-mini`)
* Salva resposta no banco
* Retorna resposta final

---

## 💬 Exemplo de fluxo

```text
Usuário: "Olá"
IA: "Oi! Como posso te ajudar?"

Usuário: "Qual o preço?"
IA: "O preço depende do serviço, posso te explicar melhor..."
```

A IA mantém contexto da conversa automaticamente.

---

## 📦 Envio de mensagens

### Individual:

```python
send_message(URL_CHATWOOT, account_id, conversation_id, mensagem)
```

### Em massa:

```python
numbers = []
send_message(numbers)
```

---

## 📌 Melhorias futuras

* [ ] Suporte a múltiplos agentes
* [ ] Controle de contexto (limite de tokens)
* [ ] Dashboard de conversas
* [ ] Integração com CRM
* [ ] Personalidade configurável da IA


---

## 📄 Licença

Uso interno / projeto em desenvolvimento.

---

## 👨‍💻 Autor

Desenvolvido por Daniel — focado em automação, IA e sistemas inteligentes.
