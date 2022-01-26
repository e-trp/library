from rest_framework.routers import DefaultRouter
from api.views import AuthorViewSet, BookViewSet, SubscriberViewSet


router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'subscribers', SubscriberViewSet)
urlpatterns = router.urls

