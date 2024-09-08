import speech_recognition as sr
import openai
from datetime import datetime
import os
import pyttsx3
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración inicial
recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000

# Configurar pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Ajustar la velocidad de la voz
engine.setProperty('volume', 1)  # Ajustar el volumen (0.0 a 1.0)

# Obtener la clave de API de OpenAI de las variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Historia de la conversación
historico_mensajes = []
palabras_clave = ['cerrar', 'salir', 'apagar',"descansa"]

def consultar_asistente(mensajes):
    respuesta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=mensajes,
        max_tokens=150
    )
    return respuesta.choices[0].message['content'].strip()

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def escuchar_comando():
    with sr.Microphone() as source:
        try:
            print("Escuchando...")
            recognizer.adjust_for_ambient_noise(source)  
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            return recognizer.recognize_google(audio, language="es-ES")
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"Error al conectar con el servicio de reconocimiento: {e}")
            return None
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            return None

while True:
    text = escuchar_comando()
    
    if text is None:
        continue
    
    text_lower = text.lower().strip()

    # Verificar si el texto coincide exactamente con una palabra clave
    if text_lower in palabras_clave:
        hablar("Apagando...")
        print("Apagando...")
        break  # Salir del bucle
    
    if "jarvis" in text_lower:
        print("USUARIO: " + text)
        
        # Añadir la entrada del usuario al historial
        ahora = datetime.now()
        fecha_actual = ahora.strftime("%d de %B de %Y")
        hora_actual = ahora.strftime("%H:%M:%S")
        mensaje_usuario = {"role": "user", "content": text}
        mensaje_contexto = {"role": "system", "content": f"Eres un asistente  diseñado únicamente para responder ante el nombre Jarvis, debes de simular ser como Jarvis y hablar como el, me refiero a el Jarvis de Tony Stark en Marvel. La fecha actual es {fecha_actual} y la hora es {hora_actual}."}
        historico_mensajes.append(mensaje_contexto)
        historico_mensajes.append(mensaje_usuario)
        
        while True:
            # Consultar al asistente
            respuesta = consultar_asistente(historico_mensajes)
            
            # Añadir la respuesta del asistente al historial
            mensaje_asistente = {"role": "assistant", "content": respuesta}
            historico_mensajes.append(mensaje_asistente)
            
            # Limpiar la pantalla
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("JARVIS: " + respuesta)
            hablar(respuesta)
            
            # Esperar una respuesta si la respuesta de Jarvis contiene una pregunta
            if "?" in respuesta:
                print("Esperando respuesta del usuario...")
                respuesta_usuario = escuchar_comando()
                if respuesta_usuario:
                    print("USUARIO: " + respuesta_usuario)
                    # Añadir la respuesta del usuario al historial
                    historico_mensajes.append({"role": "user", "content": respuesta_usuario})
                else:
                    break  # Salir del bucle de preguntas si no se recibe respuesta
            else:
                break  # Salir del bucle de preguntas si no hay pregunta en la respuesta

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
