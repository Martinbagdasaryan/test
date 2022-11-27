from django.shortcuts import render , redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import carousel

# Create your views here.


class Home(ListView):
    template_name = 'index.html'

    def get(self, request):
        
        car=carousel.objects.all()
        car1=[car[0]]
        car2=car[1:100]
        return render(request, self.template_name,{'car1':car1,'car2':car2})

class About(ListView):
    template_name = 'about.html'
    
    def get(self, request):
        car=carousel.objects.all()
        car1=[car[0]]
        
        return render(request, self.template_name,{'car1':car1})

class Blog(ListView):
    template_name = 'blog.html'

    def get(self, request):
        
        
        return render(request, self.template_name)

class Class(ListView):
    template_name = 'class.html'

    def get(self, request):
        
        
        return render(request, self.template_name)

class Contact(ListView):
    template_name = 'contact.html'

    def get(self, request):
        
        
        return render(request, self.template_name)

class Detail(ListView):
    template_name = 'detail.html'

    def get(self, request):
        
        
        return render(request, self.template_name)

class Team(ListView):
    template_name = 'team.html'

    def get(self, request):
        
        
        return render(request, self.template_name)

class Test(ListView):
    template_name = 'testimonial.html'

    def get(self, request):
        
        
        return render(request, self.template_name)
