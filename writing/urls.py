from rest_framework import routers
from .views import WritingViewSet

router = routers.DefaultRouter()
router.register(r'writing', WritingViewSet, basename='writing')

urlpatterns = router.urls
