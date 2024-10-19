from django.db import models


class User(models.Model):
    user_fname = models.CharField(max_length=50)
    user_lname = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    user_phone = models.CharField(max_length=12)
    user_pw = models.CharField(max_length=50)
    user_loggedIn = models.BooleanField(default=False)

    def __str__(self):
        return self.user_email
