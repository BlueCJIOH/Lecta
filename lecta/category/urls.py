from rest_framework import routers

from category.api.v1.views.category import CategoryViewSet

router = routers.SimpleRouter()
router.register("category", CategoryViewSet, basename="category")

urlpatterns = router.urls
