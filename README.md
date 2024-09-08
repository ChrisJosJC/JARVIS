# Asistente Virtual Jarvis

![Asistente Virtual](./assets/assistant.png)

Este proyecto es un asistente virtual que utiliza reconocimiento de voz para interactuar con el modelo de lenguaje GPT-4 de OpenAI. El asistente responde a comandos y preguntas cuando detecta la palabra clave "Jarvis". También se configura para finalizar la ejecución al escuchar comandos específicos como "cerrar", "salir", o "apagar".

## Requisitos

Para ejecutar este proyecto, necesitarás:

- **Python 3.7 o superior**
- La biblioteca `speech_recognition`
- La biblioteca `openai`
- La biblioteca `python-dotenv`

## Instalación

Sigue estos pasos para configurar el proyecto:

1. **Clonar el repositorio o descargar el archivo del proyecto:**

   ![Clonar Repositorio](./assets/clone.png)

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. **Crear un entorno virtual e instalar las dependencias:**

   ![Entorno Virtual](./assets/venv.png)

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```

3. **Instalar las dependencias necesarias:**

   Crea un archivo `requirements.txt` con el siguiente contenido:

   ```
   speech_recognition
   openai
   python-dotenv
   ```

   Luego ejecuta:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno:**

   Crea un archivo `.env` en el directorio del proyecto con el siguiente contenido:

   ```env
   OPENAI_API_KEY=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
   ```

## Uso

1. **Ejecutar el script Python:**

   ![Ejecutar Script](./assets/run.png)

   ```bash
   python nombre_del_script.py
   ```

   El asistente virtual comenzará a escuchar a través del micrófono. Dirígete a él diciendo la palabra clave "Jarvis" seguida de tu comando o pregunta.

2. **Finalizar el programa:**

   - Para salir del bucle y finalizar el programa, di "cerrar", "salir" o "apagar".

## Cómo Funciona

1. **Reconocimiento de Voz:**

   - Utiliza la biblioteca `speech_recognition` para capturar y convertir audio en texto.

2. **Consulta al Asistente Virtual:**

   - Envía el texto reconocido al modelo de lenguaje GPT-4 de OpenAI a través de la API para obtener respuestas.

3. **Control de Ejecución:**
   - El programa verifica si el texto contiene comandos específicos para salir del bucle y finalizar la ejecución.

## Configuración Adicional

- Puedes ajustar el umbral de energía del micrófono y otros parámetros en el script según tus necesidades.

- Para modificar el comportamiento del asistente o las palabras clave, edita el código fuente directamente.

## Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz un commit (`git commit -am 'Añadida nueva característica'`).
4. Envía tu rama al repositorio remoto (`git push origin feature/nueva-caracteristica`).
5. Crea una pull request en GitHub.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---

Para preguntas o problemas, abre un issue en el repositorio o contacta al mantenedor.

---

**Iconos y recursos:**

- ![Python Logo](https://www.python.org/static/img/python-logo.png)
- ![Logo de OpenAI](https://openai.com/favicon.ico)
- [Imagen de Asistente Virtual](./assets/assistant.png)
- [Imagen de Clonar Repositorio](./assets/clone.png)
- [Imagen de Entorno Virtual](./assets/venv.png)
- [Imagen de Ejecutar Script](./assets/run.png)
