from django.db import models
from django.contrib.auth.models import User as DjangoUser

import datetime


class User(DjangoUser):
    # user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    dob = models.DateField(default=datetime.date.today)
    image = models.ImageField(null=True, blank=True, upload_to="profile_image")


    @property
    def photo_url(self):
        if self.image  and hasattr(self.image , 'url'):
            return self.image .url