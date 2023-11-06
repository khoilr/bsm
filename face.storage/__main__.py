import pika
import os
from dotenv import load_dotenv

load_dotenv()


def insert_data_callback(ch, method, properties, body):
    # Process and insert data into the database
    data = body.decode("utf-8")

    # Your data insertion logic here
    print(f"Data Inserted: {data}")


def retrieve_data_callback(ch, method, properties, body):
    # Retrieve and send data in response
    data = body.decode("utf-8")

    # Your data retrieval logic here
    # Send the data back to the requester using a separate channel
    print(f"Data Retrieved: {data}")


host = os.environ.get("RABBITMQ_HOST", "localhost")
port = os.environ.get("RABBITMQ_PORT", 5672)

connection = pika.BlockingConnection(pika.ConnectionParameters(host, port))
channel = connection.channel()

# Declare channels for data insertion and retrieval
insertion_channel = "data_insertion"
retrieval_channel = "data_retrieval"

channel.queue_declare(queue=insertion_channel)
channel.queue_declare(queue=retrieval_channel)

# Set up consumers for both tasks
channel.basic_consume(queue=insertion_channel, on_message_callback=insert_data_callback, auto_ack=True)
channel.basic_consume(queue=retrieval_channel, on_message_callback=retrieve_data_callback, auto_ack=True)

print("Waiting for data insertion and retrieval requests. To exit, press Ctrl+C")

# Start consuming messages continuously
channel.start_consuming()
