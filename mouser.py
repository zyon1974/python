# chat gpt (dovrebbe far muovere il mous in cerchio, non fa nulla)
import math
import time
import pyautogui

# Imposta il centro del cerchio
center_x = 500  # Modifica queste coordinate con la posizione desiderata
center_y = 500

# Imposta il raggio del cerchio
radius = 200

# Imposta il numero di passi per completare il cerchio
num_steps = 360

# Calcola l'angolo tra ciascun passo
angle_increment = 2 * math.pi / num_steps

# Esegui il movimento circolare
for step in range(num_steps):
    # Calcola le coordinate del prossimo punto sul cerchio
    x = center_x + int(radius * math.cos(angle_increment * step))
    y = center_y + int(radius * math.sin(angle_increment * step))

    # Sposta il cursore del mouse alle nuove coordinate
    pyautogui.moveTo(x, y)

    # Aggiorna la posizione ogni 0.01 secondi (10 ms)
    time.sleep(0.01)

# Riporta il cursore in posizione iniziale
pyautogui.moveTo(center_x, center_y)
