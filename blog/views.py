from django.shortcuts import render , redirect
from blog.models import service
from blog.models import Contact_Me
from blog.models import skills

def portfolio(request):
    return render(request, 'blog/portfolio.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def education(request):
    return render(request, 'blog/education.html')

def services(request):
    services = service.objects.all()
    data= {
        'services':services
    }
    return render(request, 'blog/services.html', data)

def My_skills(request):
    My_skills = skills.objects.all()
    skills_data = {
        'skills':My_skills
    }
    return render(request, 'blog/skills.html', skills_data)

def project(request):
    return render(request, 'blog/projects.html')

def form(request):
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('sub')
            msg = request.POST.get('msg')
            print(f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {msg} ")
            form_data = Contact_Me(name=name, email=email,subject=subject,msg=msg)
            if name.strip() == '' or email.strip() == '' or subject.strip() == '':
                pass
            else:
                form_data.save()
                return redirect('/thanks')
    except:
        pass
    return render(request, 'blog/form.html', )

def thanks(request):
    return render(request, 'blog/thanks.html')