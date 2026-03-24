# core/forms.py
from django import forms
from .models import Contatto

class ContattoForm(forms.ModelForm):
    # Aggiungiamo il campo per la privacy
    accetto_privacy = forms.BooleanField(
        required=True,
        label="Accetto il trattamento dei dati personali per finalià tecniche.",
        error_messages={'required': 'Devi accettare l\'informativa sulla privacy per continuare.'}
    )

    class Meta:
        model = Contatto
        fields = ['nome', 'email', 'oggetto', 'messaggio']
        widgets = {
            'messaggio': forms.Textarea(attrs={'rows': 4}),
        }
