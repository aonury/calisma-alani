"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    # Catalog uygulamamiz icerisinde yer alan urls.py dosyamizi proje urls dosyamiz icerisine cagirdik.
    url(r'^catalog/', include('catalog.urls')),
    
    # Ana linkimizi catalog/ url'ine aktaracagiz. Siteye girildiginde otomatik olarak /catalog/ url'i gelecek.
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
]


# Django default olarak CSS, Javascript ve resimler gibi statik dosyalari calistirmiyor. "Gelistirme" asamasinda
# asagidaki sekilde tanimlama yaparak bu durumun onune gecebiliriz.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)