
# Housing Model

## Description
Ce sous-projet fait partie de la troisième étape du projet global et se concentre sur l'implémentation d'un modèle de machine learning pour prédire la valeur médiane des maisons (`median_house_value`). Il inclut l'analyse des données, l'entraînement du modèle, la création d'une API pour les prédictions, et la dockerisation de l'API.

---

## Étapes de réalisation

### 1. Initialisation du sous-projet
- Un environnement Python a été configuré à l'aide d'un gestionnaire de dépendances comme  `pyenv`.
- Les dépendances nécessaires sont listées dans le fichier `requirements.txt`.

---

### 2. Téléchargement des données
- Les données complètes ont été téléchargées depuis Kaggle : [California Housing Prices Dataset](https://www.kaggle.com/api/v1/datasets/download/camnugent/california-housing-prices).
- Les données sont enregistrées dans le fichier `data/housing.csv`.

---

### 3. Analyse des données
- Exploration des relations entre les variables présentes dans les données.
- Prétraitement des données pour :
  - Traiter les valeurs manquantes (`NaN`).
  - Identifier et gérer les valeurs aberrantes.

---

### 4. Implémentation du modèle
- Un script Python a été développé pour entraîner un modèle de machine learning capable de prédire `median_house_value`.
- Le modèle entraîné est enregistré dans un fichier `.pkl` (`random_forest_model.pkl`) pour une utilisation ultérieure.

---

### 5. Création d'une API pour les prédictions
- Une API Flask a été développée pour permettre :
  - La réception des données utilisateur au format JSON.
  - Le calcul de prédictions à l'aide du modèle entraîné.
  - Le retour des résultats sous forme de réponse JSON.

---

### 6. Dockerisation
- Une image Docker a été créée pour l'API en utilisant le fichier `Dockerfile`.
- L'API est accessible via le conteneur Docker avec le nom d'image `housing-model`.

---

## Utilisation

### Entraîner le modèle
Pour entraîner le modèle localement :
```bash
python analyze_data2.ipynb
```

### Lancer l'API localement
Exécutez les commandes suivantes :
```bash
python app.py
```
L'API sera disponible à l'adresse `http://127.0.0.1:5000`.
Pour voir le résultat d'une prédiction test développé dans le fichier app.py il faut se rendre à l'adresse `http://127.0.0.1:5000/predict_test`

### Lancer avec Docker
Pour construire et exécuter l'API dans un conteneur Docker :
```bash
docker build -t housing-model .
docker run -d -p 5000:5000 housing-model
```

---

## Structure du projet

```
housing-model/
│
├── app.py                  # API Flask
├── analyze_data2.ipynb     # Notebook d'analyse des données et entraînement
├── random_forest_model.pkl # Modèle entraîné
├── requirements.txt        # Liste des dépendances
├── Dockerfile              # Fichier de configuration Docker
├── .env                    # Fichier d'environnement
├── data/
│   └── housing.csv         # Dataset téléchargé
└── README.md               # Documentation du sous-projet
```

---

## Remarques
- Les données de prédiction sont envoyées à l'API au format JSON, et les résultats sont également retournés en JSON.
- La dockerisation garantit une portabilité complète de l'API.
