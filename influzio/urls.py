"""
URL configuration for influzio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from instaapp.views import TestLogin,Testexperimental,Testsignup,signup_view,login_view,logout_view,search_view,index,TermServices,TOS
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('login',login_view,name='login'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    path('exp',Testexperimental,name='exp'),
    path('signup',signup_view, name='signup'),
    path('logout',logout_view,name='logout'),
    path('example/<str:param>/', search_view, name='example'),
      path('terms',TermServices,name='terms'),
        path('tos',TOS,name='tos'),
]


