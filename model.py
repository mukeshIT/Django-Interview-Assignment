
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser, PermissionsMixin):
    is_admin = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)

class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    librarian_firstname = models.CharField(max_length=20)
    librarian_middlename = models.CharField(max_length=20)
    librarian_lastname = models.CharField(max_length=20)
    CATEGORY_GENDER = (('Male','Male'),('Female','Female'))
    librarian_gender = models.CharField(max_length=6, choices=CATEGORY_GENDER)
    librarian_contact = models.CharField(max_length=10, unique=True, blank=True)
    librarian_photo = models.ImageField(upload_to = 'media/librarian_photo', default='media/default.webp', blank=True)
    librarian_address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.librarian_firstname)+ ' - '+(self.librarian_lastname)
    
    def save(self, *args, **kwargs):
        for field_name in ['librarian_firstname', 'librarian_middlename', 'librarian_lastname']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Librarian, self).save(*args, **kwargs)

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_firstname = models.CharField(max_length=20)
    member_middlename = models.CharField(max_length=20)
    member_lastname = models.CharField(max_length=20)
    CATEGORY_GENDER = (('Male','Male'),('Female','Female'))
    member_gender = models.CharField(max_length=6, choices=CATEGORY_GENDER)
    member_contact = models.CharField(max_length=10, unique=True, blank=True)
    member_photo = models.ImageField(upload_to = 'media/member_photo', default='media/default.webp', blank=True)
    member_address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.member_firstname)+ ' - '+(self.member_lastname)
    
    def save(self, *args, **kwargs):
        for field_name in ['member_firstname', 'member_middlename', 'member_lastname']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Member, self).save(*args, **kwargs)
    
class Books(models.Model):
    book_name = models.CharField(max_length=50)
    book_author = models.CharField(max_length=30)
    book_isbn = models.PositiveIntegerField()    

    def __str__(self):
        return str(self.book_name)