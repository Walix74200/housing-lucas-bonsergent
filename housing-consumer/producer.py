import json
import time
import logging
from confluent_kafka import Producer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("housing-producer")

def delivery_report(err, msg):
    """ Callback appelé lorsque le broker a confirmé la réception. """
    if err is not None:
        logger.error(f"Échec de livraison: {err}")
    else:
        logger.info(f"Message envoyé au topic {msg.topic()} partition {msg.partition()} offset {msg.offset()}")

def main():
    producer_conf = {
        'bootstrap.servers': 'broker:9092'  # ou "localhost:29092"
    }

    producer = Producer(producer_conf)

    topic_name = "housing_topic"

    # Exemple de message JSON
    msg = {
      "longitude": -122.23,
      "latitude": 37.88,
      "housing_median_age": 52,
      "total_rooms": 880,
      "total_bedrooms": 129,
      "population": 322,
      "households": 126,
      "median_income": 8.3252,
      "median_house_value": 358500,
      "ocean_proximity": "NEAR BAY"
    }

    # On convertit en string JSON
    json_msg = json.dumps(msg)

    # On envoie un message
    producer.produce(topic_name, value=json_msg, callback=delivery_report)
    producer.flush()

    logger.info("Message produit, en attente de confirmation du broker...")

if __name__ == "__main__":
    main()
