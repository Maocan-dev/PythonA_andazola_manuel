from django.shortcuts import render

# Create your views here.
def denuncias(request):
    context = {}
    template_name = 'denuncias.html'
    
    return render(request, template_name, context)
