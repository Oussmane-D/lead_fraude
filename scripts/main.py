from load_data import load_data_from_api
from preprocess_data import preprocess_data
from train_model import train_model
from save_model import save_model

def main():
    # Charger les données depuis l'API
    API_URL = 'https://real-time-payments-api.herokuapp.com/current-transactions'  # Remplacez par l'URL de votre API
    df = load_data_from_api(API_URL)

    # Prétraiter les données
    X, y = preprocess_data(df)

    # Entraîner le modèle
    model = train_model(X, y)

    # Enregistrer le modèle
    save_model(model, "fraud_detection_model")

if __name__ == "__main__":
    main()