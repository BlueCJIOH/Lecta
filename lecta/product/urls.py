from rest_framework import routers

from product.api.v1.views.product import ProductViewSet

router = routers.SimpleRouter()
router.register("product", ProductViewSet, basename="product")

urlpatterns = router.urls
