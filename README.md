# 🧠 Assistente de Voz com IA (ChatGPT + Reconhecimento de Fala)

Este projeto demonstra como criar um **assistente de voz em português** que:
- Ouve comandos pelo microfone
- Envia o texto para o ChatGPT (OpenAI)
- Fala a resposta em voz alta
- Para quando o usuário disser "Pode Parar"

## 📌 Tecnologias

| Biblioteca         | Função                            |
|--------------------|-----------------------------------|
| `speech_recognition` | Captura e transcrição de voz      |
| `pyttsx3`            | Síntese de voz offline            |
| `openai`             | Integração com ChatGPT            |
| `python-dotenv`      | Carrega variáveis de ambiente     |

## 📦 Instalação

```bash
git clone https://github.com/seu-usuario/assistente-voz-openai.git
cd assistente-voz-openai
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
```

## ▶️ Como usar

Crie um arquivo `.env` com sua chave da OpenAI:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx
```

Rode o assistente:

```bash
python assistente_voz_openai.py
```

## 🛑 Para encerrar

Diga: **"Pode Parar"**

## 🧠 Autor

Eduardo Silva
