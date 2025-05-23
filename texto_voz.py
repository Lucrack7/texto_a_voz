import pyttsx3

# Inicializa el motor de TTS
engine = pyttsx3.init()

# Configura propiedades opcionales: velocidad, volumen, voz
engine.setProperty('rate', 150)    # Velocidad de habla
engine.setProperty('volume', 0.9)  # Volumen (0.0 a 1.0)

# Texto que se va a convertir a voz
texto = input("Ingrese un texto: ")

# Reproduce el texto
engine.say(texto)
engine.runAndWait()

voices = engine.getProperty('voices')
for idx, voice in enumerate(voices):
    print(f"Voz {idx}: {voice.name} - {voice.id}")

# Cambiar voz (esto depende del sistema operativo y voces instaladas)
engine.setProperty('voice', voices[0].id)  # Prueba con 0 o 1
