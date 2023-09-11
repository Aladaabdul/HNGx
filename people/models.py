from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

validators = RegexValidator(
    regex=r'^[a-zA-Z\s]*$',
    message="Name must only contain letters and spaces",
    code='invalid_name'
)
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, validators=[validators])

