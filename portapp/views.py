from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404


def home(request):
    

    return render(request, "portapp/index.html")



def about(request):
    
    
    return render(request, 'portapp/about.html')



def contact(request):

    return render(request, 'portapp/contact.html')


def services(request):

    return render(request, 'portapp/services.html')


def portfolio(request):


    return render(request, 'portapp/portfolio.html')

def portfolio_details(request):
    # Fetch the specific project or return 404 if it doesn't exist

    return render(request, 'portapp/portfolio-details.html',)

from django.shortcuts import render

def custom_error_view(request, exception=None):
    return render(request, 'error.html', status=500)  # You can adjust this as needed
