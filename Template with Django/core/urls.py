from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('start.urls',namespace='start')),
    path('blog/', include('blogs.urls',namespace='blogs')),
    path('account/', include('accounts.urls',namespace='accounts')),
    path('contact/', include('contact.urls',namespace='contact')),
    path('bank/', include('bank.urls',namespace='bank')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
