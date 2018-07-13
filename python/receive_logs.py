"""subscribe"""
#!/usr/bin/env python
import pika

# establish a connection with RabbitMQ
CONNECTION = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
CHANNEL = CONNECTION.channel()

# give the exchange a name consistent with emit_log.py
CHANNEL.exchange_declare(exchange='logs',
                         # broadcast all messages received to all queues known
                         exchange_type='fanout')

# use a server-generated random queue name (delete when connection is closed)
RESULT = CHANNEL.queue_declare(exclusive=True)
QUEUE_NAME = RESULT.method.queue

# bind exchange to send messages to queue
CHANNEL.queue_bind(exchange='logs', queue=QUEUE_NAME)

print ' [*] Waiting for logs. To exit press CTRL+C'

# build a function to respond to MQ inputs
def callback(chan, method, properties, body):
    """subscribe a callback function to..."""
    # print un-used variables for inspection
    print ["chan:", chan]
    print ["method:", method]
    print ["properties:", properties]
    # print report of logs
    print " [x] %r" % body

# set function to respond to queue
CHANNEL.basic_consume(callback,
                      queue=QUEUE_NAME,
                      no_ack=True)

CHANNEL.start_consuming()
