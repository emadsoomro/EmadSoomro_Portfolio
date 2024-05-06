from django.urls import path
from . import views
urlpatterns = [
    path('', views.portfolio, name='Portfolio'),
    path('about/', views.about, name='About'),
    path('education/', views.education, name='Education'),
    path('services/', views.services, name='Services'),
    path('skills/', views.My_skills, name='Skills'),
    path('projects/', views.project, name='Projects'),
    path('contact/', views.contact, name='Contact'),
    path('form/', views.form, name='Form'),
    path('thanks/', views.thanks, name='Thank You'),
]