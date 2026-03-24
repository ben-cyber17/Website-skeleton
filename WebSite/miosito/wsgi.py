# miosito/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

# Indica a Django dove trovare le impostazioni
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miosito.settings')

application = get_wsgi_application()