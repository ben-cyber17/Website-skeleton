import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Prodotto, Tecnologia

# Questo sensore scatta DOPO che un Prodotto è stato eliminato dal DB
@receiver(post_delete, sender=Prodotto)
def auto_delete_file_on_delete_prodotto(sender, instance, **kwargs):
    """
    Cancella il file dell'immagine dal disco quando l'oggetto Prodotto
    viene eliminato dal database.
    """
    if instance.immagine:
        if os.path.isfile(instance.immagine.path):
            os.remove(instance.immagine.path)

# Questo sensore scatta DOPO che una Tecnologia è stata eliminata dal DB
@receiver(post_delete, sender=Tecnologia)
def auto_delete_file_on_delete_tecnologia(sender, instance, **kwargs):
    """
    Cancella l'icona della tecnologia dal disco se presente.
    """
    if instance.icona:
        if os.path.isfile(instance.icona.path):
            os.remove(instance.icona.path)