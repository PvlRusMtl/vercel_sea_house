from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from houses.views import houses_list, house_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', houses_list, name='home'),
    path('<int:house_id>', house_detail, name='house')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

