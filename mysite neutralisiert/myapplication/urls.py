from django.urls import path
from . import views

app_name = 'myapplication'
urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('logout/', views.logout_user, name='logout_user'),
    path('register/', views.register_user, name='register_user'),
    path('index/', views.index, name='index'),
    path('application_documents/', views.application_documents, name='application_documents'),
    path('application_documents/<str:document>/', views.document_view, name='document'),
    path('contact/', views.contact, name='contact'),
    path('skills/', views.skills, name='skills'),
    path('jobs/', views.jobs, name='jobs'),
]
