from rest_framework import routers
from .api import ApiViewSet

router = routers.DefaultRouter()
router.register('api/work', ApiViewSet, 'work_api')
urlpatterns = router.urls
