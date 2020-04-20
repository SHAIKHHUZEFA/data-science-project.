from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Register),
    path('Fin',views.Fin,name="Fin")
]
