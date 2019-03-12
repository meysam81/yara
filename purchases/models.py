from django.db import models
from django.core.validators import validate_email, RegexValidator


class Purchase(models.Model):
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchase_name = models.CharField(max_length=150)
    user_id = models.IntegerField()
    username = models.CharField(max_length=150)
    phone_number = models.CharField(null=False, blank=False, max_length=20,
                                    validators=[RegexValidator(
                                        regex=r'^\+?1?\d{9,20}$'),
                                    ])
    email = models.CharField(max_length=150, validators=[validate_email])
    address = models.TextField()
