import os
import time

import pika

ANALYSED_COMPLAINTS = "ANALYSED_COMPLAINTS"
NEED_TO_ANALYSE = "NEED_TO_ANALYSE"


def on_need_to_analyse_msg(ch, method, properties, body):
    print("Received %r" % body)
    channel.basic_publish(exchange='', routing_key=ANALYSED_COMPLAINTS, body=body)
    print("Sent to " + ANALYSED_COMPLAINTS)


if __name__ == '__main__':
    time.sleep(20)
    host = os.getenv('RABBIT_HOST', 'localhost')
    conn = pika.BlockingConnection(pika.URLParameters('amqp://guest:guest@' + host + ':5672/%2F'))
    channel = conn.channel()

    channel.queue_declare(queue=ANALYSED_COMPLAINTS, durable=True)
    channel.queue_declare(queue=NEED_TO_ANALYSE, durable=True)

    channel.basic_consume(queue=NEED_TO_ANALYSE, on_message_callback=on_need_to_analyse_msg, auto_ack=True)
    channel.start_consuming()
