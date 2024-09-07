from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from myapp.views.auth_views import SignupView, LoginAPIView  # 경로 수정

urlpatterns = [
    path('admin/', admin.site.urls),  # Django 관리자 페이지
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT 로그인 API
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT 토큰 갱신 API
    path('api/signup/', SignupView.as_view(), name='signup'),  # 회원가입 API
    path('api/login/', LoginAPIView.as_view(), name='login'),  # 로그인 API
]