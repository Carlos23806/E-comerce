from django.shortcuts import render
from .forms import CreateNewUser

# Create your views here.

def Logup(request):
    title = "Registro"
    return render(request,'Logup.html', {
        'title': title,
        'form': CreateNewUser
    })