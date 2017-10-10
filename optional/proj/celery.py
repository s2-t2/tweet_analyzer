from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('proj',
        broker='amqp://alice:alice123@192.168.0.7:5672/alice_vhost',
        backend='rpc://',
        include=['proj.tasks'])

#Optional configuration, 
app.conf.update(
        result_expires=3600,
        )

if __name__ == '__main__' :
    app.start()
