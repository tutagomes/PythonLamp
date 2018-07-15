#!/usr/bin/python3
from flask
import Flask, request, send_from_directory
import RPi.GPIO as gpio
# Configurando como BOARD, Pinos Fisicos
gpio.setmode(gpio.BOARD)
# Configurando a direcao do Pino
gpio.setup(12, gpio.OUT)# Usei 11 pois meu setmode é BOARD, se estive usando BCM seria
17
gpio.output(12, gpio.HIGH)
gpio.output(12, gpio.LOW)
app = Flask(__name__)
global lampstate
lampstate = False
# função principal de controle
@app.route('/lamp/<state>', methods = ['GET'])
def result(state = None):
 global lampstate
if state == "on":
 print("Lampada ligada")
lampstate = True
gpio.output(12, gpio.HIGH)
elif state == "off":
 print("Lampada desligada")
lampstate = False
gpio.output(12, gpio.LOW)
elif state == "get":
 print(lampstate)
else :
 lampstate = not lampstate
if lampstate:
 gpio.output(12, gpio.HIGH)
else :
 gpio.output(12, gpio.LOW)
return str(lampstate)# resposta para o request.
@app.route('/<path:path>')
def send_js(path):
 # fornece o diretório web como raiz do servidor
 return send_from_directory('web', path)
if __name__ == "__main__":
 # define que o servidor será executado na porta 80, aceitando conexões de todos os
hosts.
 app.run(debug = False, use_reloader = True, host = '0.0.0.0', port = 80)

