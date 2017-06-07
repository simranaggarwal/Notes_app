from django.conf.urls import url
from . import views

app_name = 'UserSignUp'

urlpatterns = [
	url(r'^register/', views.UserFormView.as_view(), name = 'register'),
    url(r'^login/', views.LoginForm.as_view(), name='login'),
    url(r'^mynotes/', views.NotesCreate.as_view(), name='mynotes'),
    url(r'^search/', views.SearchTag.as_view(), name='search'),
    url(r'^logout/$', views.logout, name='logout'),
]