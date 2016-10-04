from django.shortcuts import render

from app.models import Link

# Create your views here.
def index(request):
    return render(request,'index.html') 

def events(request):
    return render(request,'events.html') 

def about(request):
    return render(request,'about.html') 

def ent(request):
    return render(request, 'entertainment.html')

def contact(request):
    return render(request,'contact.html')     


def signin(request):
    return render(request,'signin.html')  


def signup(request):
    return render(request,'signup.html')  

def hospital(request):
    return render(request,'hospital.html')  


def bank(request):
    return render(request,'bank.html') 

def police(request):
    return render(request,'police.html') 

def restaurant(request):
    return render(request,'restaurant.html') 

def temple(request):
    return render(request,'temple.html') 


def train(request):
    return render(request,'train.html') 




def link(request):
    full=Link.objects.all()
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 30:
            errors.append('Please enter at most 20 characters.')
        else:
            link = Link.objects.filter(name__icontains=q)
            return render(request, 'link_form.html',
                          {'link': link,'full':full})
        
    return render(request, 'link_form.html',
              {'errors': errors,'full':full})
