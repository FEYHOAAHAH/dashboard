from django.db import models


class Bottle(models.Model):
    quantity = models.IntegerField()


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
    ]

    bottle = models.ForeignKey(Bottle, on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date_created = models.DateTimeField(auto_now_add=True)


class Employee(models.Model):
    STATUS_CHOICES = [
        ('free', 'Free'),
        ('busy', 'Busy'),
    ]

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='free')
    date_hired = models.DateField()



class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()



class Revenue(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

