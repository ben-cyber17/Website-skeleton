# core/models.py
from django.db import models

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()
    icona = models.ImageField(upload_to='tecnologie/', blank=True, null=True)
    
    # NUOVO CAMPO: memorizza la posizione per il drag-and-drop
    ordine = models.PositiveIntegerField(
        default=0, 
        blank=False, 
        null=False,
    )

    def __str__(self):
        return self.nome

    class Meta:
        # NUOVA RIGA: dice a Django di ordinare sempre in base a questo campo
        ordering = ['ordine'] 
        verbose_name_plural = "Tecnologie"

class Prodotto(models.Model):
    nome = models.CharField(max_length=200)
    descrizione_breve = models.CharField(max_length=255)
    descrizione_dettagliata = models.TextField()
    prezzo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    immagine = models.ImageField(upload_to='prodotti/')
    tecnologie_utilizzate = models.ManyToManyField(Tecnologia, related_name='prodotti')
    creato_il = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Prodotti"

class PosizioneLavorativa(models.Model):
    titolo = models.CharField(max_length=200)
    dipartimento = models.CharField(max_length=100)
    descrizione = models.TextField()
    requisiti = models.TextField()
    data_pubblicazione = models.DateField(auto_now_add=True)
    attiva = models.BooleanField(default=True)

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Posizioni Lavorative (Lavora con noi)"

class Contatto(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    oggetto = models.CharField(max_length=200)
    messaggio = models.TextField()
    data_invio = models.DateTimeField(auto_now_add=True)
    letto = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} - {self.oggetto}"

    class Meta:
        verbose_name_plural = "Messaggi Contatti"
