from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contacto(request):
    if request.method == "POST":
        return render(request, "gracias.html")
    return render(request, "contacto.html")