#trova l'indirizzo ssh della macchina

import socket
import subprocess

def get_ssh_address():
    # Ottieni l'hostname della macchina
    hostname = socket.gethostname()

    try:
        # Esegui il comando per ottenere l'indirizzo IP associato all'hostname
        result = subprocess.check_output(["hostname", "-I"])
        ip_address = result.decode("utf-8").strip().split()[0]  # Prendi il primo indirizzo IP

        return f"ssh {hostname}@{ip_address}"
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione del comando: {e}")
        return None

if __name__ == "__main__":
    ssh_command = get_ssh_address()

    if ssh_command:
        print(f"Comando SSH: {ssh_command}")
    else:
        print("Impossibile ottenere il comando SSH.")
