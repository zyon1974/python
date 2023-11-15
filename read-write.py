import requests

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

# Sostituisci con il testo che desideri inviare
testo_da_inviare = "Questo è un esempio di testo da inviare al server PHP."
invia_testo_al_server(testo_da_inviare)
