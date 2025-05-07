import socket
import os
import time
import datetime

# Eine einzelne Clientverbindung verarbeiten
def handle_conn(clientsocket, address):
    number = 0
    # Anfragen lesen
    while True:
        request= clientsocket.recv(1000)
        if request == b"exit":
            # Beenden bei 'exit'
            break
        if request == b"reset":
            # Reset? Anzahl zurucksetzen.
            number = 0
        # Datum und Uhrzeit
        ts = datetime.datetime.fromtimestamp(
            time.time()
        ).strftime("%Y-%m-%d %H:%M:%S")
        # Anzahl erhohen
        number += 1
        # Ausgabe an den Client
        clientsocket.send(bytes(f"{number}. Anfrage: '{ts}'", "UTF-8"))
        # Log-Ausgabe (Konsole)
        print(f"{address[0]}: {request} ({ts})")
    clientsocket.send(b"Bye.\n")
    print("Connection closed by peer.")

# Lauschendes Socket erzeugen und konfigurieren
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("", 11111))
serversocket.listen(socket.SOMAXCONN)
print("Server lauscht an Port 11111 ...")
# Accept-Schleife
while True:
    (clientsocket, address) = serversocket.accept()
    # Verbindungsaufbau? Child-Prozess erzeugen
    child = os.fork()
    if child == 0:
        # Im Child-Prozess verbindung verarbeiten
        handle_conn(clientsocket, address)
        # Wieder da? Child-Prozess beende
        exit(0)