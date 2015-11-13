from celery import Celery
from sunpower import app
import requests


celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task(bind=True)
def fetch_url(url):
    with app.app_context():
        result = requests.get(url)
        return result