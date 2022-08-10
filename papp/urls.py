from os.path import basename

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from core import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'profile', views.ProfileViewSet, basename='me')
router.register(r'address', views.AddressViewSet)
router.register(r'interested-in', views.InterestedInViewSet)

router.register(r'post', views.PostViewSet, basename='post')
router.register(r'likes', views.LikesViewSet, basename='likes')
router.register(r'mypost', views.MyPostViewSet, basename='mypost')


urlpatterns = [
    path('', include(router.urls)),
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('test/', include('posts.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
