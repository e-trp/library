from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
from api.views import AuthorViewSet, BookViewSet, SubscriberViewSet, UserRegistrationView, UserProfileView
from django.urls import path


router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'subscribers', SubscriberViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register_view'),
    path('auth/', ObtainAuthToken.as_view(), name='auth_auth'),
    path('profile/', UserProfileView.as_view(), name='user_profile')
]

urlpatterns += router.urls
