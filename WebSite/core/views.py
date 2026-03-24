# core/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Prodotto, Tecnologia, PosizioneLavorativa
from .forms import ContattoForm

def lista_prodotti(request):
    # Recupera tutti i prodotti ordinati per data
    prodotti = Prodotto.objects.all().order_by('-creato_il')
    return render(request, 'core/prodotti.html', {'prodotti': prodotti})

def lista_tecnologie(request):
    tecnologie = Tecnologia.objects.all()
    return render(request, 'core/tecnologie.html', {'tecnologie': tecnologie})

def lavora_con_noi(request):
    # Mostra solo le posizioni attive
    posizioni = PosizioneLavorativa.objects.filter(attiva=True)
    return render(request, 'core/lavora_con_noi.html', {'posizioni': posizioni})

def contatti(request):
    if request.method == 'POST':
        form = ContattoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Il tuo messaggio è stato inviato con successo!')
            return redirect('contatti')
    else:
        form = ContattoForm()
    
    return render(request, 'core/contatti.html', {'form': form})

def home(request):
    return render(request, 'core/home.html')