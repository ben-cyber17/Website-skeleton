# core/admin.py
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin 
from .models import Prodotto, Tecnologia, PosizioneLavorativa, Contatto

# MODIFICA: Aggiungiamo SortableAdminMixin
@admin.register(Tecnologia)
class TecnologiaAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('nome', 'ordine')

@admin.register(Prodotto)
class ProdottoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'prezzo', 'creato_il')
    filter_horizontal = ('tecnologie_utilizzate',)

@admin.register(Contatto)
class ContattoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'oggetto', 'data_invio', 'letto')
    list_filter = ('letto', 'data_invio')
    readonly_fields = ('nome', 'email', 'oggetto', 'messaggio', 'data_invio')

admin.site.register(PosizioneLavorativa)
