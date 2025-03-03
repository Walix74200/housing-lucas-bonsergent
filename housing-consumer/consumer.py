import json
import logging
import requests
from confluent_kafka import Consumer, KafkaError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("housing-consumer")

# URL de ton service housing-api 
HOUSING_API_URL = "http://housing-api:8000/houses"

def main():
    consumer_conf = {
        'bootstrap.servers': 'broker:9092',  
        'group.id': 'housing-consumers',
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(consumer_conf)
    topic_name = "housing_topic"

    # On s'abonne au topic
    consumer.subscribe([topic_name])
    logger.info(f"Consumer abonné au topic: {topic_name}")

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue  # pas de message récupéré
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # Fin de la partition
                    continue
                else:
                    logger.error(f"Erreur consumer : {msg.error()}")
                    continue

            # On récupère le message et on l’envoie à l’API
            record_value = msg.value().decode('utf-8')
            logger.info(f"Message reçu: {record_value}")

            try:
                # Convertir en JSON
                data = json.loads(record_value)

                # Envoyer la data au service housing-api
                response = requests.post(HOUSING_API_URL, json=data)
                if response.status_code == 200:
                    logger.info("Message transmis à housing-api avec succès!")
                else:
                    logger.error(f"Erreur de transmission. Status code: {response.status_code}")
            except Exception as e:
                logger.error(f"Erreur lors du parsing ou de l'envoi: {e}")

    except KeyboardInterrupt:
        logger.info("Arrêt du consumer...")
    finally:
        consumer.close()

if __name__ == "__main__":
    main()
