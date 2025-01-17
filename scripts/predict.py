def predict_fraud(model, X_scaled):
    # Faire des prédictions
    predictions = model.predict(X_scaled)
    print("Prédictions terminées.")
    return predictions