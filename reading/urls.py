from rest_framework import routers
from .views import ReadingTestViewSet, OptionViewSet, QuestionViewSet, SegmentViewSet, ParagraphViewSet, HeadingViewSet

router = routers.DefaultRouter()
router.register(r'tests', ReadingTestViewSet)
router.register(r'options', OptionViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'segments', SegmentViewSet)
router.register(r'paragraphs', ParagraphViewSet)
router.register(r'headings', HeadingViewSet)

# 🔹 Bu yerda faqat router.urls ishlatiladi
urlpatterns = router.urls
