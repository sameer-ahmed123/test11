from django.urls import path
from . import views
from . views import Signup,Login,Cart,Index
from .Middleware.auth import auth_middleware


urlpatterns = [
path('show',views.show),
path('edit/<int:id>',views.edit),
path('del/<int:id>',views.destroy),
# path('update/<int:id>',views.update),
# path('signup',views.signup1),
path('signup',Signup.as_view()),
path('login',Login.as_view(),name="login"),
path('logout',views.logout,name='logout'),
    path("",Index.as_view(),name="homepage"),
path('store',views.store,name='store'),
path('cart', auth_middleware(Cart.as_view()), name='cart')

]
