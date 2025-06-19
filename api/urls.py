from django.urls import path
from .views import public_endpoint, protected_endpoint
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('public/', public_endpoint),
    path('protected/', protected_endpoint),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
