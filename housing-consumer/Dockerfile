FROM python:3.9-slim

# On crée un répertoire de travail
WORKDIR /app

# Copier le fichier requirements (ou pyproject.toml/poetry.lock) si tu utilises Poetry
COPY pyproject.toml poetry.lock /app/

# Installer Poetry puis les dépendances
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copier le code du consumer
COPY consumer.py /app/

CMD [ "python", "consumer.py" ]
