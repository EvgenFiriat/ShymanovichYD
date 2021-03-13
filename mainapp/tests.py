from django.test import TestCase, Client
from .models import Customer, ContentType, Smartphone, Category, Cart
from django.contrib.auth import get_user_model

User = get_user_model()


class AddToCardTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create(email='test@test.test', username='test', password='testtest')
        self.client.force_login(user=self.user)
        self._prepare_product()

    def test_add_to_card(self):
        self.client.get('add-to-card/smartphone/test')
        self.assertEqual(self.cart.total_products, 1)

    def _prepare_product(self):
        self.category = Category.objects.create(
            name='test',
            slug='test'
        )

        self.customer = Customer.objects.create(
            user=self.user,
            phone='+375291896089',
            address='test'
        )

        self.cart = Cart.objects.create(owner=self.customer)

        self.content_type = ContentType.objects.create(
            app_label='mainapp',
            model='smartphone'
        )

        self.iphone = Smartphone.objects.create(
            diagonal='14',
            display_type='жк',
            resolution='test',
            accum_volume='test',
            ram='test',
            sd=False,
            main_cam_mp='test',
            frontal_cam_mp='test',
            title='test',
            slug='test',
            category=self.category,
            price=2000
        )

