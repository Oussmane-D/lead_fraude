import requests
import pandas as pd

def load_data_from_api(api_url):
    # Récupérer les données depuis l'API
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        print("Données chargées depuis l'API :")
        print(df.head())
        return df
    else:
        raise Exception(f"Erreur lors de la récupération des données : {response.status_code}")

# Exemple d'utilisation
if __name__ == "__main__":
    API_URL = 'https://real-time-payments-api.herokuapp.com/current-transactions'  # Remplacez par l'URL de votre API
    df = load_data_from_api(API_URL)