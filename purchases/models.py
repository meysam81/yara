from django.db import models
from django.core.validators import validate_email, RegexValidator


class Purchase(models.Model):
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchase_name = models.CharField(max_length=150)
    purchase_id = models.AutoField(name='id', primary_key=True)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=150)
    phone_number = RegexValidator(regex=r'^\+?1?\d{9,20}$',
                                  message="Phone number must be entered in the "
                                          "format: '+999999999'. Up to 20 "
                                          "digits allowed.",)
    email = models.CharField(max_length=150, validators=[validate_email])
    address = models.TextField()
