from django.urls import path
from authentication.views import RegisterView
# from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.authtoken import views

urlpatterns = [
    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', RegisterView.as_view(), name='auth_register'),
    path('get-token-auth/', views.obtain_auth_token)
]