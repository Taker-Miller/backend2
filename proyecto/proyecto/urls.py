
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autos/', include('Auto.urls')),
    path('clientes/', include('Cliente.urls')),
    path('', RedirectView.as_view(url='autos/', permanent=True)),  
]
