from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from author.api.viewsets import AuthorViewSet
from book.api.viewsets import BookViewSet


router = routers.DefaultRouter()
router.register("author", AuthorViewSet)
router.register("book", BookViewSet)

urlpatterns = [
    path(settings.API_BASE_PATH, include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)