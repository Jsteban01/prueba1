from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("hello world <h1>otro</h1>")

def about(request):
    return HttpResponse("About, ¡FUNCIONA!")
