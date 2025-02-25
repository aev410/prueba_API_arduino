from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import serial, time

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las IPs (puedes cambiar esto)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)


@app.get("/")
def hola_mundo():
    return "Hola Mundo"

@app.get("/arduino/{nled}")
def blink_led(nled):
    arduino = serial.Serial("COM5", 9600)
    time.sleep(2)
    #  Configuracion Arduino
    arduino.write(str(nled).encode())
    arduino.close()
    return f"Led encendido {nled} veces"


# a = 1
# while(a != '0'):
#     a = input("Introduce un numero:\n")
#     arduino.write(str(a).encode())
