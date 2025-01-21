#!/bin/sh

flask db upgrade  # Appliquer les migrations Alembic
exec "$@"  # Continuer avec la commande CMD définie dans le Dockerfile
