import requests
from bs4 import BeautifulSoup

# Fonction pour récupérer le contenu HTML d'une page web
def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# Fonction pour extraire des informations à partir du HTML
def scrape(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Exemple : Récupérer tous les liens sur la page
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

# URL de la page à scraper
print("Veuiller renseigner l'url du site à scraper : ")
url_to_scrape = input()

# Récupérer le contenu HTML de la page
html_content = get_html(url_to_scrape)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# Si le HTML a été récupéré avec succès, procéder au scraping
if html_content:
    scrape(html_content)
