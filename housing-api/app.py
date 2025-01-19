from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialisation de l'application Flask et de SQLAlchemy
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Définition du modèle pour la table "houses"
class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    housing_median_age = db.Column(db.Integer, nullable=False)
    total_rooms = db.Column(db.Integer, nullable=False)
    total_bedrooms = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    households = db.Column(db.Integer, nullable=False)
    median_income = db.Column(db.Float, nullable=False)
    median_house_value = db.Column(db.Float, nullable=False)
    ocean_proximity = db.Column(db.String, nullable=False)

# Créer toutes les tables dans la base de données (si elles n'existent pas déjà)
with app.app_context():
    db.create_all()

# Route de test pour vérifier la connexion
@app.route('/')
def index():
    return "Connexion réussie à la base de données PostgreSQL!"

# Route GET pour récupérer toutes les maisons
@app.route('/houses', methods=['GET'])
def get_houses():
    houses = House.query.all()
    return jsonify([
        {
            'id': house.id,
            'longitude': house.longitude,
            'latitude': house.latitude,
            'housing_median_age': house.housing_median_age,
            'total_rooms': house.total_rooms,
            'total_bedrooms': house.total_bedrooms,
            'population': house.population,
            'households': house.households,
            'median_income': house.median_income,
            'median_house_value': house.median_house_value,
            'ocean_proximity': house.ocean_proximity,
        } for house in houses
    ])

# Route POST pour ajouter une nouvelle maison
@app.route('/houses', methods=['POST'])
def add_house():
    data = request.json
    new_house = House(
        longitude=data['longitude'],
        latitude=data['latitude'],
        housing_median_age=data['housing_median_age'],
        total_rooms=data['total_rooms'],
        total_bedrooms=data['total_bedrooms'],
        population=data['population'],
        households=data['households'],
        median_income=data['median_income'],
        median_house_value=data['median_house_value'],
        ocean_proximity=data['ocean_proximity'],
    )
    db.session.add(new_house)
    db.session.commit()
    return jsonify({'message': 'House added successfully'}), 201

# Point d'entrée de l'application
if __name__ == '__main__':
    app.run(debug=True)
