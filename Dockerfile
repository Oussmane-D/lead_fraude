# Utiliser une image de base Python officielle légère
FROM python:3.9-slim

# Mettre à jour le système et installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier uniquement le fichier requirements.txt pour optimiser le cache Docker
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers dans le conteneur
COPY . .

# Ajouter /app au PYTHONPATH
ENV PYTHONPATH=/app

# Définir la commande par défaut pour exécuter le script principal
CMD ["python", "scripts/predict.py"]
