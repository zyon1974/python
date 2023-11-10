import requests
from bs4 import BeautifulSoup
import re

# Parola chiave da cercare nei domini
keyword = "python"

# URL di partenza per la ricerca di domini
start_url = "https://www.google.com/search?q=intitle:index.of+" + keyword

# Numero massimo di risultati da ottenere
max_results = 1000

# Numero di risultati per pagina di ricerca di Google (10 è il massimo)
results_per_page = 10

# Lista per archiviare i domini trovati
domains = set()

# Loop per cercare i domini con la parola chiave
while len(domains) < max_results:
    response = requests.get(start_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('cite')
        
        for result in search_results:
            # Estrai il dominio dalla stringa
            domain = re.search(r'(https?://[^/]+)', result.text)
            if domain:
                domains.add(domain.group(1))
            
        # Trova il link per la pagina successiva (se presente)
        next_link = soup.find('a', {'id': 'pnnext'})
        if next_link:
            start_url = "https://www.google.com" + next_link['href']
        else:
            break
    else:
        print("Errore nella richiesta HTTP")
        break

# Stampare i domini trovati
for i, domain in enumerate(domains):
    print(f"{i + 1}. {domain}")

# Salva i domini in un file di testo
with open('domains.txt', 'w') as file:
    for domain in domains:
        file.write(domain + '\n')
        
print("finito")
print(response)