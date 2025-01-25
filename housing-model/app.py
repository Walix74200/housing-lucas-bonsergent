from flask import Flask, request, jsonify
import numpy as np
import joblib

# Créer une instance Flask
app = Flask(__name__)

# Charger le modèle entraîné
model = joblib.load("random_forest_model.pkl")  # Assurez-vous que le fichier existe dans le même dossier

# Route racine pour vérifier que le serveur fonctionne
@app.route('/')
def home():
    return "Bienvenue sur l'API de prédiction des prix des maisons !"

# Route pour effectuer une prédiction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtenir les données envoyées dans la requête POST
        data = request.get_json()

        # Liste des colonnes requises par le modèle
        required_columns = [
            'longitude', 'latitude', 'housing_median_age', 'total_rooms',
            'total_bedrooms', 'population', 'households', 'median_income',
            'ocean_proximity_INLAND', 'ocean_proximity_ISLAND',
            'ocean_proximity_NEAR BAY', 'ocean_proximity_NEAR OCEAN'
        ]

        # Vérifier les colonnes manquantes
        missing_columns = [col for col in required_columns if col not in data]
        if missing_columns:
            return jsonify({'error': f"Les colonnes suivantes manquent : {', '.join(missing_columns)}"}), 400

        # Ajouter les colonnes manquantes avec une valeur par défaut (0)
        for col in required_columns:
            if col not in data:
                data[col] = 0

        # Préparer les données pour la prédiction
        input_data = np.array([data[col] for col in required_columns]).reshape(1, -1)

        # Effectuer la prédiction
        prediction = model.predict(input_data)

        # Retourner la prédiction au format JSON
        return jsonify({'prediction': float(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/predict_test')
def predict_test():
    # Exemple de données
    example_data = {
    "longitude": -118.0,
    "latitude": 34.0,
    "housing_median_age": 30.0,
    "total_rooms": 2000,
    "total_bedrooms": 400,
    "population": 1000,
    "households": 300,
    "median_income": 4.5,
    "ocean_proximity_INLAND": 1,
    "ocean_proximity_ISLAND": 0,
    "ocean_proximity_NEAR BAY": 0,
    "ocean_proximity_NEAR OCEAN": 0,
    "rooms_per_household": 6.67,
    "bedrooms_per_room": 0.2,
    "population_per_household": 3.33
}

    try:
        # Préparer les données pour la prédiction
        input_data = np.array([example_data[col] for col in [
            'longitude', 'latitude', 'housing_median_age', 'total_rooms',
            'total_bedrooms', 'population', 'households', 'median_income',
            'ocean_proximity_INLAND', 'ocean_proximity_ISLAND', 'ocean_proximity_NEAR BAY',
            'ocean_proximity_NEAR OCEAN'
        ]]).reshape(1, -1)

        # Effectuer la prédiction
        prediction = model.predict(input_data)

        # Afficher le résultat dans le navigateur
        return f"Résultat de la prédiction : {float(prediction[0])}"

    except Exception as e:
        return f"Erreur : {str(e)}"

# Lancer le serveur Flask
if __name__ == '__main__':
    (app.run(host='0.0.0.0', port=5000))
