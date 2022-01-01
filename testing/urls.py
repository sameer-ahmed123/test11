from django.urls import path
from . import views

urlpatterns = [
path('test',views.test),
path('sh',views.show),
path('edit/<int:id>',views.edit),
path('del/<int:id>',views.destroy),
path('update/<int:id>',views.update),
path('creds',views.creds),
path('signup',views.signup1),
path('login',views.login),
]
