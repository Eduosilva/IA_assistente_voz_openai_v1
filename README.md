
## 🧠 Assistente de Voz com IA (ChatGPT + Reconhecimento de Fala)

Este projeto demonstra como criar um **assistente de voz em português** que:

* **Ouve comandos pelo microfone**
* **Envia o texto para o ChatGPT (OpenAI)**
* **Fala a resposta em voz alta**
* **Para quando o usuário disser "Pode Parar"**

---

### 📌 Tecnologias e Bibliotecas Utilizadas

| Biblioteca           | Função                           |
| -------------------- | -------------------------------- |
| `speech_recognition` | Captura e transcrição de fala    |
| `pyttsx3`            | Síntese de voz (fala) local      |
| `openai`             | Comunicação com a API do ChatGPT |

---

### ✅ Pré-requisitos

* Python 3.8+
* Microfone funcional
* Conta na [OpenAI](https://platform.openai.com)

---

### 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/assistente-voz-openai.git
cd assistente-voz-openai
```

2. Crie um ambiente virtual e ative:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` com sua chave da OpenAI:

```
OPENAI_API_KEY=sk-...
```

Ou cole diretamente no código (não recomendado para produção).

---

### ▶️ Como usar

Execute o assistente com:

```bash
python assistente_voz_openai.py
```

Fale algo como:

> "Qual a capital da França?"

O assistente irá:

* Ouvir sua fala
* Consultar o ChatGPT
* Responder com voz

Para encerrar, diga:

> **"Pode Parar"**

---

### 📄 Exemplo de saída

```
🎤 Ouvindo...
Você disse: Qual a capital da França?
Assistente: A capital da França é Paris.
```

---

### 🚨 Observações

* Em ambientes barulhentos, a acurácia da voz pode cair.
* A velocidade da fala pode ser ajustada com `tts.setProperty('rate', 170)`
* O modelo usado é o `gpt-3.5-turbo`

---

### 📚 Referências

* [OpenAI Python SDK](https://platform.openai.com/docs/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [pyttsx3](https://pyttsx3.readthedocs.io/)

---

### 🧠 Autor

Eduardo Silva (você pode colocar seu LinkedIn e GitHub https://www.linkedin.com/in/eduardo-silva-92b36a21/)

---

### ✅ Próximos passos sugeridos

* Interface com botão para gravar e parar
* Comandos locais personalizados (ex: abrir navegador, responder e-mail)
* Exportar histórico em `.txt` ou `.csv`

---
