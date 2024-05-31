from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("User should have an Email!")
        if not password:
            raise ValueError("User should have a Valid Password!")
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, full_name=None, password=None):
        user = self.create_user(
            email=email,
            full_name=full_name,
            password=password,
            is_staff=True,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, full_name=None):
        user = self.create_user(
            email=self.normalize_email(email),
            full_name=full_name,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=264, unique=True)
    full_name = models.CharField(max_length=264, null=True, blank=True)
    is_active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=False)  # is a staff
    admin = models.BooleanField(default=False)  # is a superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    # address = models.TextField(blank=True)
    # phone = models.CharField(max_length=15, blank=True)
    USERNAME_FIELD = 'email'    # assign the email field as the username field
     # by default when declaring own user model USERNAME and password is required we can add extra required by
    REQUIRED_FIELDS = []  # [ 'field_name' ]

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        try:
            sn = self.full_name.split(' ')[0]
        except AttributeError:
            sn = None
        return sn

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff
    

class ShippingAddress(models.Model):
	customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=225, null=False)
	phone_no = models.CharField(max_length=15,)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	is_active = models.BooleanField(default=True)
	date_added = models.DateTimeField(auto_now_add=True)
    

	def __str__(self):
		return self.address