from django.test import Client, TestCase
from rest_framework.reverse import reverse

from apps.menu.models import Food, FoodCategory


class FoodListAPI(TestCase):
    def setUp(self) -> None:

        # Initialize client and URL
        self.client = Client()
        self.url = reverse("foods-list")

        # Categories
        # ##########

        # Category 1: Will contain both published and hidden foods
        self.category_with_published_and_hidden_foods = FoodCategory.objects.create(
            name_ru="Category 1, published and hidden foods", order_id=10
        )

        # Category 2: Only hidden foods
        self.category_with_only_hidden_foods = FoodCategory.objects.create(
            name_ru="Category 2, only hidden foods", order_id=20
        )
        # Category 3, without foods
        self.category_without_foods = FoodCategory.objects.create(
            name_ru="Category 3, no foods", order_id=30
        )

        published_food = Food.objects.create(
            category=self.category_with_published_and_hidden_foods,
            code=1,
            internal_code=100,
            name_ru="Published food",
            cost=100.00,
            is_publish=True,
        )

        hidden_food = Food.objects.create(
            category=self.category_with_only_hidden_foods,
            code=2,
            internal_code=200,
            name_ru="Hidden food",
            cost=50.00,
            is_publish=False,
        )

        # Foods for category with published and hidden foods
        Food.objects.create(
            category=self.category_with_published_and_hidden_foods,
            code=1,
            internal_code=105,
            name_ru="Published food without additional",
            cost=100.00,
            is_publish=True,
        )

        Food.objects.create(
            category=self.category_with_published_and_hidden_foods,
            code=2,
            internal_code=103,
            name_ru="Published food with additional hidden food",
            cost=50.00,
            is_publish=True,
        ).additional.add(hidden_food)

        Food.objects.create(
            category=self.category_with_published_and_hidden_foods,
            code=2,
            internal_code=104,
            name_ru="Published food with additional published food",
            cost=50.00,
            is_publish=True,
        ).additional.add(published_food)

        # Foods for category with only hidden foods
        Food.objects.create(
            category=self.category_with_only_hidden_foods,
            code=2,
            internal_code=201,
            name_ru="Hidden food without additional",
            cost=50.00,
            is_publish=False,
        )

        Food.objects.create(
            category=self.category_with_only_hidden_foods,
            code=1,
            internal_code=202,
            name_ru="Hidden food with additional hidden foods",
            cost=200.00,
            is_publish=False,
        ).additional.add(hidden_food)

        Food.objects.create(
            category=self.category_with_only_hidden_foods,
            code=1,
            internal_code=203,
            name_ru="Hidden food with additional pulished foods",
            cost=200.00,
            is_publish=False,
        ).additional.add(published_food)

        self.response = self.client.get(self.url)

    def test_return_200(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_categories_without_published_foods_excluded(self) -> None:
        self.assertEqual(len(self.response.json()), 1)

    def test_unpublished_foods_excluded(self) -> None:
        published_foods_internal_codes = Food.objects.filter(
            is_publish=True
        ).values_list("internal_code", flat=True)
        for category in self.response.json():
            for food in category["foods"]:
                self.assertIn(food["internal_code"], published_foods_internal_codes)

    def test_unpublished_foods_excluded_from_additional(self) -> None:
        published_foods_internal_codes = Food.objects.filter(
            is_publish=True
        ).values_list("internal_code", flat=True)
        for category in self.response.json():
            for food in category["foods"]:
                for additional_internal_code in food["additional"]:
                    self.assertIn(
                        additional_internal_code, published_foods_internal_codes
                    )
