"""create local queue & send hello world"""
#!/usr/bin/env python
import pika
# establish a CONNECTION with RabbitMQ
CONNECTION = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
CHANNEL = CONNECTION.channel()

# create a queue named 'hello'
CHANNEL.queue_declare(queue='hello')

# use the default exchange
CHANNEL.basic_publish(exchange='',
                      # specify the queue to which to publish
                      routing_key='hello',
                      # specify the text to send
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
# close the CONNECTION
CONNECTION.close()
