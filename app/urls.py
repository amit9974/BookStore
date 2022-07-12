from os import stat
from re import template
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("",views.BookStore,name="bookstore"),
    path("main/",views.main_page,name="main"),
    path("register/",views.Registration_page,name="register"),
    path("login",auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path("logout",auth_views.LogoutView.as_view(template_name="logout.html"),name="logout"),

]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)