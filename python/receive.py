"""create local queue and listen for messages"""
#!/usr/bin/env python
import pika

# establish a connection with RabbitMQ
CONNECTION = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
CHANNEL = CONNECTION.channel()

# create a queue named 'hello'
CHANNEL.queue_declare(queue='hello')

# subscribe a callback function to...
def callback(body, chan, method, properties):
    """subscribe a callback function to..."""
    print " [x] Received %r" % body
    print " [x] Received %r" % chan
    print " [x] Received %r" % method
    print " [x] Received %r" % properties


# set RabbitMQ to send messages from queue to callback
CHANNEL.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print ' [*] Waiting for messages. To exit press CTRL+C'
# set never-ending loop to run callbacks whenever necessary
CHANNEL.start_consuming()
