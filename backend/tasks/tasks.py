from celery import shared_task

@shared_task
def hello(name):
    print(f'hello {name}')