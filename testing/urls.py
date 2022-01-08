from django.urls import path
from . import views

urlpatterns = [
path('test',views.test),
path('',views.show),
path('edit/<int:id>',views.edit),
path('del/<int:id>',views.destroy),
path('update/<int:id>',views.update),
path('creds',views.creds),
path('signup',views.signup1),
path('login',views.login,name="login"),
path('logout',views.logout,name='logout'),
path('store',views.store,name='store'),
]
