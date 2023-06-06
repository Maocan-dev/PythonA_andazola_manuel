from django.shortcuts import render

# Create your views here.
def respuestas(request):
    context={}
    template_name = 'respuestas.html'
    
    return render(request, template_name, context)