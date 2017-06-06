from django.conf.urls import url
#from django.views.generic import TemplateView
from . import views

app_name = 'UserSignUp'

urlpatterns = [
	#url(r'^connection/',TemplateView.as_view(template_name = 'SignUpPage.html')),
	url(r'^register/', views.UserFormView.as_view(), name = 'register'),
    url(r'^login/', views.LoginForm.as_view(), name='login'),
    url(r'^mynotes/', views.NotesCreate.as_view(), name='mynotes'),
    url(r'^search/', views.SearchTag.as_view(), name='search'),
    url(r'^loggout/$', views.loggout, name='loggout'),
]