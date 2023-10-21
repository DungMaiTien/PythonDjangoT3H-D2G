"""
URL configuration for mysite project.

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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('product1.urls')),
    path('blog/', include('blog.urls')),
    path('abm/',include('abm.urls')),
    path('register/',include('register.urls')),
    path('login/',include('login2.urls')),
    path('logout/',include('logout2.urls')),
    path('cs/',include('cs.urls')),
    path('size/',include('size.urls')),
    path('prf/',include('prf.urls')),
    path('cart/',include('cart.urls')),

    



    
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
