from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass



#aqui ja tem um username, password, email e etc..., que vem de AbstractUser