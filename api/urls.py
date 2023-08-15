from intelweb.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import *
from django.urls import path, include
from django.conf.urls.static import static

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('event', EventViewSet , basename='events')

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# router = DefaultRouter()
# router.register('events', EventViewSet, basename='item')

urlpatterns = [
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.jwt')),
#    path('get_events/', views.showEvents.as_view()),
#    path('get_projects/', views.showProjects.as_view()),
#    path('get_blogs/', views.showBlogs.as_view()),
   path('projects/', views.Projects_view.as_view()),
   path('blogs/', views.Blogs_view.as_view()),
   path('events/', views.Event.as_view()),
#    path('api/', include(router.urls)),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
