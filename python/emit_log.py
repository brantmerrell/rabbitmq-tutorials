#!/usr/bin/env python
"""emit"""
import sys
import pika

# establish a connection with RabbitMQ
CONNECTION = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
CHANNEL = CONNECTION.channel()

# give the exchange a name consistent with receive_logs.py
CHANNEL.exchange_declare(exchange='logs',
                         #
                         exchange_type='fanout')

MESSAGE = ' '.join(sys.argv[1:]) or "info: Hello World!"
CHANNEL.basic_publish(exchange='logs',
                      routing_key='',
                      body=MESSAGE)
print " [x] Sent %r" % MESSAGE
CONNECTION.close()
