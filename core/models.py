from django.db import models

# Create your models here

class Librarian(models.Model):
    staffID = models.AutoField(primary_key=True) # Unique identifier for each librarian. Auto-incremented.
    name = models.CharField(max_length=250) # Full name of the librarian. Max length 250 characters.
    username = models.CharField(max_length=250, unique=True) # Username for librarian login. Max length 250 characters. Must be unique.
    email = models.EmailField(unique=True) # Email address of the librarian. Must be unique.
    password = models.CharField(max_length=128, unique=True) # Password for librarian login. Max length 128 characters. Must be unique.

    class Meta:
        db_table = "librarians" # Specifies the database table name for this model.

class Library_Member(models.Model):
    memberID = models.AutoField(primary_key=True) # Unique identifier for each library member. Auto-incremented.
    name = models.CharField(max_length=250) # Full name of the librarian. Max length 250 characters.
    username = models.CharField(max_length=250, unique=True) # Username for librarian login. Max length 250 characters. Must be unique.
    DOB = models.DateField() # Date of Birth of the library member.
    address = models.CharField(max_length=500) # Address of the library member. Max length 500 characters.
    phone = models.IntegerField(max_length=15, unique=True) # Phone number of the library member. Max length 15 digits. Must be unique.
    email = models.EmailField(unique=True) # Email address of the librarian. Must be unique.
    password = models.CharField(max_length=128, unique=True) # Password for librarian login. Max length 128 characters. Must be unique.

    class Meta:
        db_table = "library members" # Specifies the database table name for this model.
        
