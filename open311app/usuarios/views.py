from django.shortcuts import render

# Create your views here.

def usuarios(request):
    context = {}
    template_name = 'usuarios.html'
    
    return render(request, template_name, context)
