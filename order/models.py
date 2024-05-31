from django.db import models
from account.models import User
from store.models import Product
from account.models import ShippingAddress
from django.db.models.signals import pre_save, post_save
from .utils import unique_transaction_id_generator

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    shipping_address = models.ForeignKey(ShippingAddress,on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    is_shipped = models.BooleanField(default=False)
    is_in_transit = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    delivery_info = models.TextField(blank=True)
    est_deliver_date = models.DateField(blank=True, null=True) # in days


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def get_total_value(self):
        return float(self.product.selling_price) * int(self.quantity)


def get_data_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.transaction_id:
        instance.transaction_id = unique_transaction_id_generator(instance)

pre_save.connect(get_data_pre_save_receiver, sender=Order)