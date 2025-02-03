## Housing Model

### Description
Ce sous-projet fait partie de la troisième étape du projet global et se concentre sur l'implémentation d'un modèle de machine learning pour prédire la valeur médiane des maisons (*median_house_value*). Il inclut l'analyse des données, l'entraînement du modèle, la création d'une API pour les prédictions, et la dockerisation de l'API.

---

## Étapes de réalisation

### 1. Initialisation du sous-projet
- Un environnement Python a été configuré à l'aide d'un gestionnaire de dépendances comme pyenv.
- Les dépendances nécessaires sont listées dans le fichier `requirements.txt`.

### 2. Téléchargement des données
- Les données complètes ont été téléchargées depuis Kaggle : *California Housing Prices Dataset*.
- Les données sont enregistrées dans le fichier `data/housing.csv`.

### 3. Analyse des données
- Exploration des relations entre les variables présentes dans les données.
- Prétraitement des données pour :
  - Traiter les valeurs manquantes (*NaN*).
  - Identifier et gérer les valeurs aberrantes.

### 4. Implémentation du modèle
- Un script Python a été développé pour entraîner un modèle de machine learning capable de prédire *median_house_value*.
- Le modèle entraîné est enregistré dans un fichier `.pkl` (*random_forest_model.pkl*) pour une utilisation ultérieure.

### 5. Création d'une API pour les prédictions
- Une API Flask a été développée pour permettre :
  - La réception des données utilisateur au format JSON.
  - Le calcul de prédictions à l'aide du modèle entraîné.
  - Le retour des résultats sous forme de réponse JSON.

### 6. Dockerisation
- Une image Docker a été créée pour l'API en utilisant le fichier `Dockerfile`.
- L'API est accessible via le conteneur Docker avec le nom d'image `housing-model`.

### 7. Utilisation

#### Entraîner le modèle
Pour entraîner le modèle localement :
```bash
python analyze_data2.ipynb
```

#### Lancer l'API localement
Exécutez les commandes suivantes :
```bash
python app.py
```
L'API sera disponible à l'adresse `http://127.0.0.1:5000`. Pour voir le résultat d'une prédiction test développé dans le fichier `app.py`, il faut se rendre à l'adresse `http://127.0.0.1:5000/predict_test`.

#### Lancer avec Docker
Pour construire et exécuter l'API dans un conteneur Docker :
```bash
docker build -t housing-model .
docker run -d -p 5000:5000 housing-model
```

---

## TP3 : Gestion des Expérimentations et Déploiement avec MLflow

Dans cette troisième partie du projet, nous allons mettre en place MLflow afin de suivre nos expérimentations, gérer les versions de notre modèle et déployer ce dernier sous forme d’API Dockerisée MLflow.

### 1. Suivi d’Expérimentations avec MLflow

#### Installation de MLflow
```bash
pip install mlflow
```

#### Démarrer l’UI MLflow
```bash
mlflow ui
```
L’interface web sera disponible à l’adresse [http://127.0.0.1:5000](http://127.0.0.1:5000).

#### Logger les paramètres, métriques et artefacts
Ajoutez dans votre script d'entraînement :
```python
mlflow.set_experiment("Housing Model Experiment")
with mlflow.start_run():
    mlflow.log_param("model_type", "RandomForestRegressor")
    mlflow.log_param("n_estimators", best_rf_model.n_estimators)
    mlflow.log_param("max_depth", best_rf_model.max_depth)
    
    mlflow.log_metric("r2_score", r2_score_val)
    
    mlflow.sklearn.log_model(
        sk_model=best_rf_model,
        artifact_path="housing_rf_model"
    )
```

### 2. Gestion du Modèle via la Model Registry

#### Enregistrer le modèle
Dans l’UI MLflow, ouvrez le run → *Register Model* → choisissez un nom (ex. `Housing_Model_Nom`).
Ou via code :
```python
client = MlflowClient()
model_uri = mlflow.get_artifact_uri("housing_rf_model")
client.register_model(model_uri, "Housing_Model_Nom")
```

### 3. Déploiement du Modèle en mode MLflow

#### Construction d’une image Docker MLflow
```bash
mlflow models build-docker \
    -m "models:/Housing_Model_Lucas@champion" \
    -n "housing_model_image"
```

#### Lancer le conteneur et tester l’API
```bash
docker run -p 1234:8000 housing_model_image
```

Tester une prédiction :
```bash
curl -X POST http://127.0.0.1:1234/invocations \
     -H "Content-Type: application/json" \
     -d '{
           "columns": [...],
           "data": [[...]]
         }'
```

### 4. (Optionnel) Docker Compose
```yaml
version: '3'
services:
  mlflow-housing-model:
    image: housing_model_image
    ports:
      - "1234:8000"
```
Lancer le service :
```bash
docker-compose up -d
```

