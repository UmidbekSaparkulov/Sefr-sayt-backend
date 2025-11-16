from rest_framework import routers
from .views import (
    TestInfoViewSet,
    TestTipViewSet,
    ExpectationViewSet,
    SampleQuestionViewSet,
    SampleQuestionGuidelineViewSet
)

router = routers.DefaultRouter()
router.register(r'test-info', TestInfoViewSet)
router.register(r'test-tips', TestTipViewSet)
router.register(r'expectations', ExpectationViewSet)
router.register(r'sample-questions', SampleQuestionViewSet)
router.register(r'sample-question-guidelines', SampleQuestionGuidelineViewSet)

urlpatterns = router.urls
