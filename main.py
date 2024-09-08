import speech_recognition as sr
import openai
from datetime import datetime
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave de API de OpenAI desde las variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configuración inicial
recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000

# Historia de la conversación
historico_mensajes = []
palabras_clave = ['cerrar', 'salir', 'apagar']

def consultar_asistente(mensajes):
    respuesta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=mensajes,
        max_tokens=150
    )
    return respuesta.choices[0].message['content'].strip()

while True:
    with sr.Microphone() as source:
        try:
            print("Escuchando...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio, language="es-ES")
            
            if any(palabra in text.lower() for palabra in palabras_clave):
                print("Saliendo...")
                break  # Salir del bucle
            
            if "jarvis" in text.lower():
                print("USUARIO: " + text)
                # Añadir la entrada del usuario al historial
                ahora = datetime.now()
                fecha_actual = ahora.strftime("%d de %B de %Y")
                hora_actual = ahora.strftime("%H:%M:%S")
                mensaje_usuario = {"role": "user", "content": text}
                mensaje_contexto = {"role": "system", "content": f"Eres un asistente virtual diseñado únicamente para responder ante el nombre Jarvis. La fecha actual es {fecha_actual} y la hora es {hora_actual}."}
                historico_mensajes.append(mensaje_contexto)
                historico_mensajes.append(mensaje_usuario)
                
                # Consultar al asistente
                respuesta = consultar_asistente(historico_mensajes)
                
                # Añadir la respuesta del asistente al historial
                mensaje_asistente = {"role": "assistant", "content": respuesta}
                historico_mensajes.append(mensaje_asistente)
                
                # Limpiar la pantalla
                os.system('cls' if os.name == 'nt' else 'clear')
                
                print("JARVIS: " + respuesta)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                 
        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print(f"Error al conectar con el servicio de reconocimiento: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
