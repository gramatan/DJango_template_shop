# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
## login - pass : guest - guest
import os
from celery import Celery


# задать стандартный модуль настроек Django
# для программы 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
app = Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
