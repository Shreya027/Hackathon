"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',views.index),
    url(r'^events/$',views.events),
    url(r'^about/$',views.about),
    url(r'^links/$',views.link),
    url(r'^entertainment/$',views.ent),
    url(r'^contact/$',views.contact),
    url(r'^signin/$',views.signin),
    url(r'^signup/$',views.signup),
    url(r'^hospital/$',views.hospital),
    url(r'^bank/$',views.bank),
    url(r'^train/$',views.train),
    url(r'^bank/$',views.bank),
    url(r'^restaurant/$',views.restaurant),
    url(r'^police/$',views.police),
    url(r'^temple/$',views.temple),
  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    
