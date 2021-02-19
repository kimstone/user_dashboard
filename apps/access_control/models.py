from django.db import models

import re           # the regex module
import bcrypt

class UserManager(models.Manager):

    def validate_registration_form(self, data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        errors = {}

        if len(data['f_name']) < 3:
            errors['first_name'] = "First name must be at least 2 characters."

        if data['f_name'].isalpha():
            pass
        else:
            errors['first_name'] = "First name must be letters only."

        if len(data['l_name']) < 3:
            errors['last_name'] = "Last name must be at least 2 characters."

        if data['l_name'].isalpha():
            pass
        else:
            errors['last_name'] = "Last name must be letters only."

        if not EMAIL_REGEX.match(data['email_add']):
            errors['email'] = ("Invalid email address!")

        # CHECK FOR UNIQUE EMAIL
        email_check = User.objects.filter(email=data['email_add']).exists()
        if email_check:
            errors['email'] = "That email address has been taken, choose another."

        if len(data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."

        if data['password'] != data['pw_confirm']:
            errors['password'] = "Passwords do not match."

        return errors


    def register_new_user(self, data):
        hashed_pw = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name=data['f_name'],
            last_name=data['l_name'],
            email=data['email_add'],
            password=hashed_pw,
        )


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"