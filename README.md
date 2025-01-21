
# Housing API Project

Ce projet est une API Flask containerisée avec Docker qui interagit avec une base de données PostgreSQL pour gérer des informations de logements. Il inclut des routes pour ajouter et récupérer des données de maisons.

---

## Fonctionnalités principales
- Ajouter une maison via une requête POST.
- Récupérer toutes les maisons via une requête GET.
- Base de données PostgreSQL persistante.

---

## Prérequis
- **Docker** et **Docker Compose** installés sur votre machine.
- **Python 3.10+** installé (si vous souhaitez exécuter localement sans Docker).

---

## Étapes pour exécuter avec Docker

### 1. Cloner le projet
Clonez le dépôt GitHub sur votre machine locale :
```bash
git clone https://github.com/votre-utilisateur/housing-lucas-bonsergent.git
cd housing-lucas-bonsergent
```

### 2. Configurer le fichier `.env`
Créez un fichier `.env` à la racine du projet avec les variables suivantes :
```env
DB_HOST=db
DB_PORT=5432
DB_NAME=housing
DB_USER=housing_user
DB_PASSWORD=housing_user
```

### 3. Lancer les conteneurs Docker
Construisez et démarrez les conteneurs avec la commande suivante :
```bash
docker-compose up --build
```

### 4. Vérifier les conteneurs en cours d'exécution
Assurez-vous que les conteneurs fonctionnent :
```bash
docker ps
```
Vous devriez voir deux conteneurs : 
- `housing-api` (API Flask)
- `housing-db` (PostgreSQL)

### 5. Accéder à l'API
L'API est accessible à l'adresse suivante :
```plaintext
http://localhost:5000
```

---

## Étapes pour faire des requêtes API

### 1. Ajouter une maison (POST)
Utilisez la commande suivante pour ajouter une maison dans la base de données :
```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "longitude": -121.5,
  "latitude": 38.5,
  "housing_median_age": 30,
  "total_rooms": 1500,
  "total_bedrooms": 300,
  "population": 800,
  "households": 250,
  "median_income": 4.5,
  "median_house_value": 250000.0,
  "ocean_proximity": "INLAND"
}' http://localhost:5000/houses
```

### 2. Récupérer toutes les maisons (GET)
Utilisez cette commande pour récupérer la liste des maisons enregistrées :
```bash
curl http://localhost:5000/houses
```

---

## Structure du projet

Voici la structure des fichiers et répertoires du projet :

```
housing-lucas-bonsergent/
│
├── housing-api/
│   ├── app.py                 # Code principal de l'API Flask
│   ├── config.py              # Configuration Flask et PostgreSQL
│   ├── requirements.txt       # Dépendances Python
│   ├── Dockerfile             # Dockerfile pour containeriser l'API
│   ├── entrypoint.sh          # Script pour lancer les migrations et l'API
│   └── docker-compose.yml     # Configuration Docker Compose pour l'API et la base de données
│
└── .env                       # Variables d'environnement (non versionnées dans Git)
```
