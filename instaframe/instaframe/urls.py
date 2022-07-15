"""instaframe URL Configuration"""

# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
#    path('sorted/', views.sort_integers),
#    path('hello/<str:name>/<int:age>/', views.say_hi)

    path('', include('posts.urls')),
    path('users/', include('users.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
