from django.shortcuts import render, redirect
# ⚠️ Humne yahan aapke saare naye models (Skill, Profile, Project) ko import kiya hai:
from .models import ContactMessage, Skill, Profile, Project  

def home(request):
    # Admin panel se saari skills aur profile photo lekar HTML ko bhejna:
    skills = Skill.objects.all()
    profile = Profile.objects.first()
    
    context = {
        'skills': skills,
        'profile': profile,
    }
    return render(request, 'core/home.html', context)

def projects(request):
    # Admin panel se saare logistic projects lekar HTML ko bhejna:
    all_projects = Project.objects.all()
    
    context = {
        'projects': all_projects,
    }
    return render(request, 'core/projects.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')  
        message = request.POST.get('message')
        
        ContactMessage.objects.create(name=name, email=email, phone=phone, message=message)
        return redirect('home')
        
    return render(request, 'core/contact.html')


