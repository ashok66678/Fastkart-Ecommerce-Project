from django.db import models
from account.models import User
from store.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def get_total_value(self):
        return float(self.product.selling_price) * int(self.quantity)

