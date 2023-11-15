import geocoder

def ottieni_posizione_geografica():
    # Utilizza il modulo geocoder per ottenere la posizione geografica
    posizione = geocoder.ip('me')

    # Verifica se la posizione è stata trovata con successo
    if posizione.ok:
        latitudine, longitudine = posizione.latlng
        indirizzo = posizione.address
        print(f"Posizione geografica:")
        print(f"Latitudine: {latitudine}")
        print(f"Longitudine: {longitudine}")
        print(f"Indirizzo: {indirizzo}")
    else:
        print("Impossibile ottenere la posizione geografica.")

if __name__ == "__main__":
    ottieni_posizione_geografica()