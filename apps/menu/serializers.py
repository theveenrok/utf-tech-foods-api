from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from apps.menu.models import Food, FoodCategory


class FoodSerializer(ModelSerializer):
    additional = SlugRelatedField(many=True, read_only=True, slug_field="internal_code")

    class Meta:
        model = Food
        fields = (
            "internal_code",
            "code",
            "name_ru",
            "description_ru",
            "description_en",
            "description_ch",
            "is_vegan",
            "is_special",
            "cost",
            "additional",
        )


class FoodListSerializer(ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ("id", "name_ru", "name_en", "name_ch", "order_id", "foods")
