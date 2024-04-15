from django.db.models import Max, F

from product.api.v1.serializers.product import ProductSuggestionSerializer
from product.models import SearchHistory
from user_session.models import UserSession


def get_suggestion(queryset, request):
    session = request.session
    user = request.user
    product_ids = queryset.values("id")
    serializer = ProductSuggestionSerializer
    first_three = serializer(queryset.values("title", "price")[:3], many=True)
    curr_session_views = serializer(
        SearchHistory.objects.select_related("product")
        .values(title=F("product__title"), price=F("product__price"))
        .annotate(datetime=Max("timestamp"))
        .filter(session_id=session.session_key, product_id__in=product_ids)
        .order_by("-datetime")[:3],
        many=True,
    )
    all_session_views = serializer(
        SearchHistory.objects.select_related("product")
        .values(title=F("product__title"), price=F("product__price"))
        .annotate(datetime=Max("timestamp"))
        .filter(
            session_id__in=UserSession.objects.filter(user_id=user.id).values("session_id"),
            product_id__in=product_ids,
        )
        .order_by("-datetime")[:3],
        many=True
    )
    return {
        "first_three": first_three.data,
        "curr_session_views": curr_session_views.data,
        "all_session_views": all_session_views.data,
    }
