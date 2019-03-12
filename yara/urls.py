from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('purchases.urls', namespace='purchases')),
    path('api/login/', obtain_jwt_token),
    # path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
