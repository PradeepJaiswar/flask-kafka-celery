from celery import Celery

app = Celery('worker1', broker='amqp://guest@localhost//')

@app.task(name='flask-rest-api.tasks.printNumbers')
def printNumbers():
    for number in range(100):
        print(number)
