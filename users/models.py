from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	# null is database-related it can store a database entry a NULL
	# blank is validation-related, then a form will allow an empty value
	age = models.PositiveIntegerField(null=True, blank=True)
