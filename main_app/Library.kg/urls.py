from django.contrib import admin
from django.urls import path, include
from main_app import views as main_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # старые функции
    path('', main_views.home),
    path('contacts/', main_views.contacts),
    path('time/', main_views.current_time),
    path('random/', main_views.random_number),
    path('about/', main_views.about_me),

    # новое приложение books
    path('books/', include('books.urls')),
]

# статика и медиа для разработки
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
