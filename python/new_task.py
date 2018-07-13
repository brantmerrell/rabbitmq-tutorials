"""send input to be executed by RabbitMQ"""
#!/usr/bin/env python
import sys
import pika

# establish a connection with RabbitMQ
CONNECTION = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
CHANNEL = CONNECTION.channel()

# create a queue called task_queue; mark queue & messages as durable
CHANNEL.queue_declare(queue='task_queue', durable=True)

# for message paste arguments into string; if they do not exist, use hello world
MESSAGE = ' '.join(sys.argv[1:]) or "Hello World!"

CHANNEL.basic_publish(exchange='',
                      # specify the queue to which to publish
                      routing_key='task_queue',
                      # specify the text to send
                      body=MESSAGE,
                      # use persistent delivery_mode property
                      properties=pika.BasicProperties(
                          delivery_mode=2, # make message persistent
                      ))
print " [x] Sent %r" % MESSAGE
CONNECTION.close()
