from django.urls import path
from userDB import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<pk>', views.view_user, name='view_user')
]