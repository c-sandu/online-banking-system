import random
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, name, user_type, password=None):
        """
        Creates and saves a User with the given username, name, user_type and
        password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            name=name,
            user_type=user_type,
            auth_seed=random.randint(1, 999999999),
        )
        user.set_password(password)
        user.save(using=self._db)
        return  user

    def create_superuser(self, username, name, user_type, password=None):
        """
        Creates and saves a superuser with the given username, name and password
        """
        user = self.create_user(
        username,
        name=name,
        user_type=user_type,
        password=password,
        )
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    CUSTOMER = 'CST'
    VENDOR   = 'VND'
    BANKER   = 'BNK'
    ADMIN    = 'ADM'
    USER_TYPE_CHOICES = (
            (CUSTOMER, 'Customer'),
            (VENDOR, 'Vendor'),
            (BANKER, 'Banker'),
            (ADMIN, 'ADMIN'),
    )

    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=40)
    user_type = models.CharField(
            max_length=3,
            choices=USER_TYPE_CHOICES,
            default=CUSTOMER,
    )
    auth_seed = models.BigIntegerField()
    created = models.DateTimeField('date creation', auto_now_add=True)
    updated = models.DateTimeField('date updated', auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'user_type']

    objects = UserManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.user_type == User.ADMIN

    def check_auth_code(self, auth_code):
        if auth_code == 'test':
            return True
        return False


class Account(models.Model):
    CURRENT = 'CUR'
    SAVINGS = 'SVG'
    ACCOUNT_TYPE_CHOICES = (
            (CURRENT, 'Current'),
            (SAVINGS, 'Savings'),
    )
    iban = models.CharField(max_length=34, unique=True)
    acc_type = models.CharField(
            max_length=3,
            choices=ACCOUNT_TYPE_CHOICES,
            default=CURRENT,
    )
    owner = models.ForeignKey(User)
    balance = models.DecimalField(max_digits=15, decimal_places=6)
    currency = models.CharField(max_length=3)
    date_creation = models.DateTimeField('date creation', auto_now_add=True)
    date_last_touch = models.DateTimeField('date last touch', auto_now=True)


class Transaction(models.Model):
    trans_id = models.CharField(max_length=10, unique=True)
    src_acc = models.ForeignKey(Account, related_name='transaction_src_acc')
    dst_acc = models.ForeignKey(Account, related_name='transaction_dst_acc')
    amount = models.DecimalField(max_digits=15, decimal_places=6)
    currency = models.CharField(max_length=3)
    date = models.DateTimeField('date transaction')
    message = models.CharField(max_length=255)

