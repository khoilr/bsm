import os
from datetime import datetime

import cv2
import pika
from dotenv import load_dotenv
from loguru import logger

from constants import FRAME_FREQUENCY, MAX_CAP_OPEN_FAILURES, MAX_READ_FRAME_FAILURES

load_dotenv()

# Environment variables
camera_url = os.environ.get("CAMERA_URL")
rabbitmq_host = os.environ.get("RABBITMQ_HOST", "localhost")
rabbitmq_port = os.environ.get("RABBITMQ_PORT", 5672)
rabbitmq_queue = os.environ.get("RABBITMQ_QUEUE", "hello")

# Configure logger
logger.add(f"logs/{datetime.now().astimezone().isoformat()}.log", rotation="500 MB")

# RabbitMQ server configuration
credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=rabbitmq_host,
        port=rabbitmq_port,
        credentials=credentials,
    )
)
channel = connection.channel()
channel.queue_declare(queue=rabbitmq_queue)


# Main function to capture frames, process faces, and save results
def main():
    """Handle errors and restart the camera if necessary."""

    frame_counter = 0
    read_frame_failures_counter = 0
    cap_open_failures_counter = 0

    while cap_open_failures_counter < MAX_CAP_OPEN_FAILURES:
        cap = cv2.VideoCapture(camera_url)

        if not cap.isOpened():
            logger.error("Failed to connect to the camera.")
            cap_open_failures_counter += 1
            continue

        logger.info("Connected to the camera.")
        cap_open_failures_counter = 0
        read_frame_failures_counter = 0

        while read_frame_failures_counter < MAX_READ_FRAME_FAILURES:
            ret, frame = cap.read()

            if not ret:
                logger.error("Failed to capture frame.")
                read_frame_failures_counter += 1
                continue

            read_frame_failures_counter = 0
            frame_counter += 1

            if frame_counter % FRAME_FREQUENCY == 0:
                # channel.basic_publish(exchange="", routing_key=rabbitmq_queue, body=frame)
                channel.basic_publish(exchange="", routing_key="hello", body=frame.dumps())
                print(" [x] Sent 'Hello World!'")

            if cv2.waitKey(1) == ord("q"):
                break

        logger.error(f"Read frame failures reached {MAX_READ_FRAME_FAILURES}. Restarting the camera...")

    logger.error(f"Capture open failures reached {MAX_CAP_OPEN_FAILURES}. Exiting the program...")


if __name__ == "__main__":
    main()
    connection.close()
