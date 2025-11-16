from rest_framework import routers

from .views import CoreLevelViewSet, CoreSkillSet

router = routers.DefaultRouter()
router.register(r'core_level', CoreLevelViewSet, basename='corelevel')
router.register(r'core_skill', CoreSkillSet, basename='coreskill')

urlpatterns = router.urls