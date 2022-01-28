from rest_framework.routers import DefaultRouter
from api.views import AuthorViewSet, BookViewSet, SubscriberViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'subscribers', SubscriberViewSet)
urlpatterns = router.urls
