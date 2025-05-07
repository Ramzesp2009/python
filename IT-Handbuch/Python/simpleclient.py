import socket
import sys

# Host von Kommandozeile, sonst localhost
host = "localhost"
if len(sys.argv) > 1:
    host = sys.argv[1]
# Serververbindung
sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.getprotobyname("tcp")
)
ip = socket.gethostbyname(host)
port = 11111
sock.connect((ip, port))
print("<0> Zurücksetzen, <X> Beenden, Sonstige Eingabe: Info.")
# Kommunikationsschleife
while True:
    line = input("> ")
    # Je nach Eingabe Befehle an den Server senden
    if line == "x" or line == "X":
        # Beenden
        sock.send(b"exit")
    else:
        # Standart: Anzahl/Datum erfragen
        sock.send(bytes(line, "UTF-8"))
    # Serverantwort lesen und ausgeben
    antwort = sock.recv(1000).decode("UTF-8")
    print(f"Antwort von {host}: {antwort}")
    # Beenden?
    if line == "x" or line == "X":
        break