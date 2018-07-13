"""perform worker task (sleep) in queue"""
#!/usr/bin/env python
import time
import pika

CONNECTION = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
CHANNEL = CONNECTION.channel()

CHANNEL.queue_declare(queue='task_queue', durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'

# subscribe a callback function to...
def rename_fun(chan, method, properties, body):
    """subscribe a callback function to..."""
    print properties
    print " [x] Received %r" % body
    # assign task
    time.sleep(body.count(b'.'))
    print " [x] Done"
    chan.basic_ack(delivery_tag=method.delivery_tag)
# limit simultaneous task count to 1
CHANNEL.basic_qos(prefetch_count=1)
# set RabbitMQ to send messages from queue to (callback) function
CHANNEL.basic_consume(rename_fun,
                      queue='task_queue')

CHANNEL.start_consuming()
