from django.db import models
from django.urls import reverse
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save

# Create your models here.
GENDER_CHOICES = (('male','male'),
                  ('female','female'),
                  ('Unisex','Unisex'))


class Category(models.Model):
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories' 

    def get_absolute_url(self):
        return reverse("category_list", args=[self.slug])
    
    def __str__(self):
        return self.slug


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/placeholder.png')
    slug = models.SlugField(max_length=255, blank = True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    page_views = models.IntegerField(default=0)   ### NEW ADDED
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products' ## change the model name in the admin panel when more than one obejct is created (Added).
        ordering = ('-created',)         ## in which order we want to display the products. (- means in reverse order -> descending order.)

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug])
    
    @property                            # property decorator this method will act as an attribute
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url    
   
    def __str__(self):                   ## How you want to see the obj name in the database (admin panel)
        return self.title
    

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender = Product)