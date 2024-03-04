from django.db import models
from django.utils import timezone
# id (primary key)
# First_name (st), last_name(str), phone(str)
#email(email), created_date (date), description (text).
#DEPOIS
#category (foreign Key), show (boolean), owner (foreign key)
# picture (imagem)

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    