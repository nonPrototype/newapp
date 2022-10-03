from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class ClientManager(BaseUserManager):
    def create_client(self, username, password=None):
        if not username:
            raise ValueError('Customers must have an username')
        client = self.model(username=username)
        client.set_password(password)
        client.save(using=self._db)
        return client

    def create_superuser(self, username, password):
        client = self.create_client(
            username=username,
            password=password,
        )
        client.is_admin = True
        client.save(using=self._db)
        return client

class Client(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    name = models.CharField('Name', max_length = 30)
    email = models.EmailField('Email', max_length = 100)
    age = models.IntegerField('Age')
    phone = models.IntegerField('Phone')

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN' 
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = ClientManager()
    USERNAME_FIELD = 'username'
