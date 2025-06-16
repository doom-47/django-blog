from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
            TokenObtainPairView,
            TokenRefreshView,
        )
urlpatterns = [
    # Django Admin Panel
    path('admin/', admin.site.urls),

    # Include your blog_app's API URLs under the 'api/' prefix
    path('api/', include('blog_app.urls')),

    # JWT Authentication Endpoints (Project-level)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
