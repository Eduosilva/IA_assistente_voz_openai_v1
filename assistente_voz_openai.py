import speech_recognition as sr
import pyttsx3
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

r = sr.Recognizer()
tts = pyttsx3.init()

def ouvir_microfone():
    with sr.Microphone() as source:
        print("🎤 Ouvindo...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            texto = r.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto}")
            return texto
        except sr.UnknownValueError:
            print("❌ Não entendi o que foi dito.")
            return ""
        except Exception as e:
            print("❌ Erro ao ouvir:", e)
            return ""

def responder_chatgpt(pergunta):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": pergunta}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("❌ Erro na OpenAI:", e)
        return "Desculpe, houve um erro ao tentar responder sua pergunta."

def falar(texto):
    print(f"Assistente: {texto}")
    tts = pyttsx3.init(driverName='sapi5')
    tts.setProperty('rate', 170)
    tts.say(texto)
    tts.runAndWait()
    tts.stop()

while True:
    comando = ouvir_microfone()
    if comando.strip() == "":
        print("🔁 Nada foi entendido, ouvindo novamente...")
    if comando:
        if "pode parar" in comando.lower():
            falar("Encerrando. Até mais!")
            break
        resposta = responder_chatgpt(comando)
        falar(resposta)
