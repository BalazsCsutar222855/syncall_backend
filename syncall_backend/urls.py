
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calendar_core.urls')),
    path('editor/', include('editor_core.urls'))
]
