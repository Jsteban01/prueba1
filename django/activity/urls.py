"""
URL configuration for activity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from PRUEBA.views import link01
#from PRUEBA import views  (otra manera de importar)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', link01),
    #path('se pone vacio por que no lleva nada antes que el "urls de la app" ', include('PRUEBA.urls')),
    #path('', hello),
    #path('about/', about),
    #path('about/', views.about)  (junto con la otra manera de importar)
]
