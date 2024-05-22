import os
import http.server
import socketserver

# Imposta la porta del server (prova una porta diversa, ad esempio 8081)
PORT = 8081

# Cambia la directory corrente alla directory del progetto
os.chdir('C:/Users/anton/Documents/SICKILY/pagina_antonio')

# Crea un handler per gestire le richieste
handler = http.server.SimpleHTTPRequestHandler

# Avvia il server
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Server attivo su http://localhost:{PORT}")
    httpd.serve_forever()
