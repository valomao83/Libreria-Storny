#from django.contrib import admin
from django.urls import path
from Storni import views 
from Storni.views import userCreateViews

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('Registro/', userCreateViews.Registro, name='Registro'),
    path('', userCreateViews.Login, name='Login')
]