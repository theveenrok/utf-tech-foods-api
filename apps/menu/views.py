from django.db.models import Exists, OuterRef, Prefetch
from rest_framework.generics import ListAPIView

from apps.menu.models import Food, FoodCategory
from apps.menu.serializers import FoodListSerializer


class FoodsListAPIView(ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        published_foods_qs = Food.objects.filter(is_publish=True)
        aditional_foods_prefetch = Prefetch(
            "additional",
            queryset=published_foods_qs.filter(internal_code__isnull=False),
        )
        foods_prefetch = Prefetch(
            "foods",
            queryset=published_foods_qs.prefetch_related(aditional_foods_prefetch),
        )

        category_has_published_foods = Exists(
            published_foods_qs.filter(category=OuterRef("pk"))
        )

        qs = (
            FoodCategory.objects.annotate(
                has_published_foods=category_has_published_foods
            )
            .filter(has_published_foods=True)
            .prefetch_related(foods_prefetch)
        )
        return qs
