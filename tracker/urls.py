from rest_framework import routers
from .views import CompanyViewSet, ApplicationViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = router.urls