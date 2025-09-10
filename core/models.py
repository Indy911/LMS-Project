from django.db import models

# Create your models here

class Librarian(models.Model):
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = "librarians"
        
class Member(models.Model):
    Name = models.CharField(max_length=250)
    Username = models.CharField(max_length=250)
    DOB = models.DateField()
    Email = models.EmailField(unique=True)
    HouseAddress = models.CharField(max_length=500)
    Password = models.CharField(max_length=128)

    class Meta:
        db_table = "library_members"

class Book(models.Model):
    Title = models.CharField(max_length=250)
    Author = models.CharField(max_length=250)
    ISBN = models.CharField(max_length=13, unique=True)
    Price = models.DecimalField(max_digits=4, decimal_places=2)
    Is_borrowed = models.BooleanField(default=False)

    class Meta:
        db_table = "books"

class Loan(models.Model):
    IssueDate = models.DateField(auto_now_add=True)
    DueDate = models.DateField()
    ReturnDate = models.DateField(null=True, blank=True)
    Fine = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)

    class Meta:
        db_table = "loans"

class Genre(models.Model):
    Genre = models.CharField(max_length=100)
    Description = models.TextField()

    class Meta:
        db_table = "genres"

class Reservation(models.Model):
    ReservationDate = models.DateField(auto_now_add=True)
    Status = models.CharField(max_length=50)

    class Meta:
        db_table = "reservations"

class Report(models.Model):
    Action = models.TextField()
    Date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "reports"
