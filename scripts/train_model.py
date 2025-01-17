from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import mlflow
import mlflow.sklearn

def train_model(X, y):
    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraîner le modèle
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Évaluer le modèle
    y_pred = model.predict(X_test)
    print("Rapport de classification :")
    print(classification_report(y_test, y_pred))

    # Enregistrer le modèle avec MLflow
    with mlflow.start_run():
        mlflow.log_params({"model": "RandomForest", "random_state": 42})
        mlflow.sklearn.log_model(model, "model")
        print("Modèle enregistré avec MLflow.")

    return model

# Exemple d'utilisation
if __name__ == "__main__":
    import pandas as pd
    from preprocess_data import preprocess_data

    df = pd.read_csv("transactions.csv")  # Remplacez par le chargement depuis l'API si nécessaire
    X, y = preprocess_data(df)
    train_model(X, y)