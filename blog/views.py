from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {}) 

##esto es una funcion def y regresa una funcion render que construye nuestra plantilla.
