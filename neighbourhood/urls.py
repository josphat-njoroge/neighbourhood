from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LogoutView, LoginView
from hood import views as hood_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hood.urls')), 
    path('register/', hood_views.register, name='register'), 
    # path('accounts/', include('registration.backends.simple.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('login/', LoginView.as_view(template_name= '/'), name='user_login'),
    # path('logout/', LogoutView.as_view(template_name='/'), name="user_logout"),
]
