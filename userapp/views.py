from django.shortcuts import render,HttpResponse

# Create your views here.
def sayhello(request):
    return HttpResponse("django project is created and web page is executed")

def html_page(request):
    return render(request, 'index.html')