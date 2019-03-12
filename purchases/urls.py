from django.urls import include, path
from rest_framework import routers
from purchases import views

app_name = 'purchases'

router = routers.DefaultRouter()
router.register(app_name, views.PurchaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
