"""
URL configuration for backend_elromero project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from tienda import views

urlpatterns = [
    path('gerente-elromero/', admin.site.urls),
    path('api/', include('tienda.tienda_urls')),
    path('nuevo-producto', views.agregar_producto, name='agregar_producto'),
    path('editar-producto/<int:pk>', views.editar_producto, name='editar_producto'),
    path('cambiar-estado/<int:pk>', views.cambiar_estado_producto, name='cambiar_estado_producto'),
    path('', views.tienda, name='tienda'),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
