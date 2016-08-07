import logging, time

from kafka import KafkaConsumer

from workers.worker1 import printNumbers


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )

consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest')

while True:
    consumer.subscribe(['craw-url'])

    for message in consumer:
        printNumbers.delay()
