from django.conf import settings
from . import views
from django.contrib.auth import views as  auth_views
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name="register-authentication"),
    path('accounts/profile/',views.profile_info,name='profile'),
    path('profile_edit', views.profile_edit, name='profile_edit'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]