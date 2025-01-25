FROM python:3.13-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY app.py .
COPY random_forest_model.pkl .

# Installer les outils système pour compiler les bibliothèques natives
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    make \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port utilisé par Flask
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "app.py"]
