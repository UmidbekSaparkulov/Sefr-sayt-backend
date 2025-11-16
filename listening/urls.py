from rest_framework import routers
from .views import ListeningTestViewSet, ListeningQuestionViewSet, ListeningOptionViewSet

router = routers.DefaultRouter()
router.register(r'tests', ListeningTestViewSet)
router.register(r'questions', ListeningQuestionViewSet)
router.register(r'options', ListeningOptionViewSet)

urlpatterns = router.urls

