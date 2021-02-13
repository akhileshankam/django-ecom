from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('order/',views.order,name='order'),
    path('signupform/',views.signupform,name='signupform'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('loginform/',views.loginform,name='loginform'),
    path('cart/', views.cart, name='cart'),
    path('logout/',views.logout,name='logout'),
    path('search/',views.search,name='search'),
    path('confirm/',views.confirm,name='confirm'),
    path('cart2/',views.cart2,name='cart2'),
]
